# Get madhukars script to install kubernetes docker and dependent packages
printf "\n Install kubernetes and all the other dependent packages for it to work ----- \n"
wget http://10.84.5.120/images/soumilk/imp_scripts/kubernetes/install_kubernetes_on_ubuntu.sh
chmod 777 /root/install_kubernetes_on_ubuntu.sh
atemp=exec "/root/install_kubernetes_on_ubuntu.sh"
printf "\nInitialize Kubeadm -----\n\n"
kubeadm init
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

printf "\nApplying the patches -----\n\n"
# Now lets patch the system 
kubectl patch deploy/kube-dns --type json  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/readinessProbe", "value": {"exec": {"command": ["wget", "-O", "-", "http://127.0.0.1:8081/readiness"]}}}]' -n kube-system

kubectl patch deploy/kube-dns --type json  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/livenessProbe", "value": {"exec": {"command": ["wget", "-O", "-", "http://127.0.0.1:10054/healthcheck/kubedns"]}}}]' -n kube-system && kubectl patch deploy/kube-dns --type json  -p='[{"op": "replace", "path": "/spec/template/spec/containers/1/livenessProbe", "value": {"exec": {"command": ["wget", "-O", "-", "http://127.0.0.1:10054/healthcheck/dnsmasq"]}}}]' -n kube-system && kubectl patch deploy/kube-dns --type json  -p='[{"op": "replace", "path": "/spec/template/spec/containers/2/livenessProbe", "value": {"exec": {"command": ["wget", "-O", "-", "http://127.0.0.1:10054/metrics"]}}}]' -n kube-system

printf "\nGet Helm -----\n\n"
# Get HELM
export HELM_VERSION=v2.5.1
export TMP_DIR=$(mktemp -d)
curl -sSL https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar -zxv --strip-components=1 -C ${TMP_DIR}
sudo mv ${TMP_DIR}/helm /usr/local/bin/helm
rm -rf ${TMP_DIR}

printf "\nGet the contrail docker from R4.0 branch -----\n\n"
# Get contrail related charts and manifests
git clone https://github.com/Juniper/contrail-docker.git -b R4.0
cd /root/contrail-docker/kubernetes/manifests
kubectl create -f tiller.yaml
kubectl patch ds/tiller-ds --type json   -p='[{"op": "replace", "path": "/spec/updateStrategy/type", "value": "RollingUpdate"}]' -n kube-system && kubectl set image ds/tiller-ds tiller=gcr.io/kubernetes-helm/tiller:${HELM_VERSION} -n kube-system
printf "\nInitialize helm in the client only mode -----\n\n"
helm init --client-only

# Get contrail-kubernetes-docker-images and change the params in values.yaml. Also add the images to docker 
branch=$1
build=$2
ip=$3

printf "\nGet the required kubernetes docker images and add them to docker also install the required packages -----\n\n"
mkdir /root/docker_images
cd  /root/docker_images
apt-get install -y sshpass
apt-get install -y python-paramiko
tmp=$(python -c 'import paramiko;client = paramiko.SSHClient();client.set_missing_host_key_policy(paramiko.AutoAddPolicy());client.connect("10.84.5.39", username="soumilk", password="soumilk123");stdin, stdout, stderr = client.exec_command("ls /github-build/'$branch'/'$build'/ubuntu-16-04/ocata/artifacts/ | grep contrail-kubernetes-docker-images_");a = stdout.readlines()[0];b=a.replace("\n","");print b')
echo  $tmp
#sshpass -p soumilk123 scp soumilk@10.84.5.39:/github-build/$branch/$build/ubuntu-16-04/ocata/artifacts/$tmp .
wget http://10.84.5.120/github-build/$branch/$build/ubuntu-16-04/ocata/artifacts/$tmp
tar -xvzf contrail-kubernetes-docker-images_*
printf "\nLoad contrail-agent image to docker\n"
docker load -i contrail-agent-ubuntu16.04-*
printf "\nLoad contrail-analyticsdb image to docker\n"
docker load -i contrail-analyticsdb-ubuntu16.04-*
printf "\nLoad contrail-controller image to docker\n"
docker load -i contrail-controller-ubuntu16.04-*
printf "\nLoad contrail-kube-manager image to docker\n"
docker load -i contrail-kube-manager-ubuntu16.04-*
printf "\nLoad contrail-kubernetes-agent image to docker\n"
docker load -i contrail-kubernetes-agent-ubuntu16.04-*
printf "\nLoad contrail-analytics image to docker\n"
docker load -i contrail-analytics-ubuntu16.04-*
cd /root/contrail-docker/kubernetes/helm/contrail
rm values.yaml
cd /root/docker_images
temp="$(ls | grep contrail-controller-ubuntu)"
temp1=$(python -c 'a="'$temp'"; b=a.replace("contrail-controller-ubuntu16.04-", ""); c=b.replace(".tar.gz", ""); print c')
cd /root/contrail-docker/kubernetes/helm/contrail
wget http://10.84.5.120/images/soumilk/imp_scripts/kubernetes/contrail_helm/values.yaml
chmod 777 values.yaml
sed -i 's/__br_bd_no__/'${temp1}'/' values.yaml
sed -i 's/__ip_to_replace__/'${ip}'/' values.yaml
printf "\n create the contrail pod using helm on the cubernetes cluster with the help of values.yaml file\n\n"
helm install --name test /root/contrail-docker/kubernetes/helm/contrail


