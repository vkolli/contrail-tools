source /etc/contrail/openstackrc
echo $1 >> /root/$1/info.txt
a="$(openstack project create $1 -f json > /root/$1/uuid.json)"
openstack_project_uuid=$(python -c 'import json; fd=json.loads(open("/root/'$1'/uuid.json").read()); print fd["id"]')
dashed_project_uuid=$(python -c 'import uuid; fd=uuid.UUID("'${openstack_project_uuid}'"); print fd')
echo $dashed_project_uuid
ubuntu_image_name=$2
selected_config_node_ip=$3
sleep 5
echo "The Contents of the input.json file before modification "
cat /root/$1/input.json

keystone user-role-add --user admin --role admin --tenant $1

sed -i 's/project_uuid_val/'${dashed_project_uuid}'/' /root/$1/input.json
echo "input.json  --- Changed"

python /root/$1/change_testbed_params.py /root/$1/input.json $ubuntu_image_name parse_openstack_image_list_command
python /root/$1/inp_to_yaml.py /root/$1/input.json check_and_create_required_flavor

sleep 5
sed -i 's/image_val/'${ubuntu_image_name}'/' /root/$1/input.json
fip_uuid="$(python change_testbed_params.py input.json $selected_config_node_ip get_fip_uuid)"
sed -i 's/fip_uuid/'${fip_uuid}'/' input.json
echo "input.json  --- Changed"
echo "\n The Input.json looks something like this now"
cat /root/$1/input.json

#mkdir /root/$dashed_project_uuid
python /root/$1/inp_to_yaml.py /root/$1/input.json create_network_yaml > /root/$1/final_network.yaml
python /root/$1/inp_to_yaml.py /root/$1/input.json create_server_yaml > /root/$1/final_server.yaml
echo " The Servere and Network YAML files are now created at location '/root/$dashed_project_uuid'"

network_stack='test_network_final'
final_network_stack_name=$network_stack$dashed_project_uuid
echo "Network Stack Name: $final_network_stack_name"
echo $final_network_stack_name >> /root/$1/info.txt
server_stack_name='test_server_final'
final_server_stack_name=$server_stack_name$dashed_project_uuid
echo "Server Stack Name: $final_server_stack_name"
echo $final_server_stack_name >> /root/$1/info.txt

#rm /root/.ssh/known_hosts
# Lets create the Network Stack
heat stack-create -f /root/$1/final_network.yaml $final_network_stack_name
sleep 10
while true
do
python /root/$1/change_testbed_params.py /root/$1/input.json $final_network_stack_name get_stack_status > /root/$1/tmp.txt
chmod 777 /root/$1/tmp.txt
net_res="$(cat /root/$1/tmp.txt)"
if [ "$net_res" == 'success' ] || [ "$net_res" == 'failed' ] || [ "$net_res" == 'inprogress' ];
then
        if [ "$net_res" == 'success' ]
        then
                echo " Network Stack Created Successfully"
                break
        fi
        if [ "$net_res" == 'failed' ]
        then
                echo "Network Stack Creation Failed "
                break
        fi
        if [ "$net_res" == 'inprogress' ]
        then
                echo "Network Stack creation still in progress. Waiting for 20 more seconds"
                heat stack-list | grep $final_network_stack_name
                sleep 20
        fi
else
        echo "Network Stack Creation: get_stack_status function in change_testbed_params.py file did not return any thing"
        break
fi
done


if [ "$net_res" == 'success' ]
then
	heat stack-create -f /root/$1/final_server.yaml $final_server_stack_name
        sleep 20
        while true
        do
	python /root/$1/change_testbed_params.py /root/$1/input.json $final_server_stack_name get_stack_status > /root/$1/tmp.txt
        chmod 777 /root/$1/tmp.txt
        ser_res="$(cat /root/$1//tmp.txt)"
	if [ "$ser_res" == 'success' ] || [ "$ser_res" == 'failed' ] || [ "$ser_res" == 'inprogress' ];
        then
                #echo $final_server_stack_name
                #echo "$ser_res"
                if [ "$ser_res" == 'success' ]
                then
                        echo "Server Stack Created Successfully"
                        break
                fi
                if [ "$ser_res" == 'failed' ]
                then
                        echo "Server Stack Creation Failed"
			heat stack-show $final_server_stack_name
			exit 0
                fi
                if [ "$ser_res" == 'inprogress' ]
                then
                        echo "Server Stack Still in progress. Waiting for 30 more seconds"
                        heat stack-list | grep $final_server_stack_name
                        sleep 30
                fi
        else
                echo "Server Stack Creation: get_stack_status function in change_testbed_params.py file did not return any thing"
                break
        fi
        done
	echo " Final List of all Heat Stacks "
        heat stack-list
	python /root/$1/inp_to_yaml.py /root/$1/input.json create_yaml_file_for_5_0_provisioning  > /root/$1/all.yml
	echo "Yaml with all the provision and test parameters is created and named as all.yml"
	contrail_version="$(echo $VERSION)"
	sed -i 's/__VERSION__/'${contrail_version}'/' /root/$1/all.yml
	python /root/$1/inp_to_yaml.py /root/$1/input.json get_config_node_ip > /root/$1/config_node_ip
        config_node_ip="$(cat /root/$1/config_node_ip)"
	((count=50))
	while [[ $count -ne 0 ]] ; do
            output=$(ping  -c5 $config_node_ip)
            echo $output | grep "100% packet loss"
            rc=$?
            if [[ $rc -ne 0 ]]; then
                break
            fi
            echo "The Config Node is not yet Pingable"
	    ((count = count - 1))
	done
	if [[ $count -eq 0 ]]
	then
	    echo "The Config Node is Not Pingable"
            exit 1
	else
	    echo "The confing node ip where the contrail-deployments repo is going to cloned is: "$config_node_ip
	    sshpass -p c0ntrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$config_node_ip 'yum install -y git ansible epel-release vim ; cd ; git clone https://github.com/Juniper/contrail-tools.git'
	    sshpass -p c0ntrail123 scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /root/$1/all.yml root@$config_node_ip:/root/contrail-tools/ansible/inventory/group_vars/
	    sshpass -p c0ntrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$config_node_ip 'cd /root/contrail-tools/ansible/ ; ansible-playbook -i inventory/ playbooks/all.yml'
	fi
else
        echo "Network Stack Creation failed. So creation of the SERVER STACK is TERMINATED !!!!"
fi
echo "Cloning the contrail-deployments repo and transferring the all.yaml file generated above."
echo "DONE !!!!!!!!!!!!"
