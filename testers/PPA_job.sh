#!/usr/bin/env bash

TOOLS_WS=${TOOLS_WS:-$(pwd)}
source $TOOLS_WS/testers/utils
# AVAILABLE_TESTBEDS is a comma separated list of testbed filenames or paths
testbeds=(${AVAILABLE_TESTBEDS//,/ })
echo "AVAILABLE TESTBEDS : ${testbeds[@]}"

get_testbed
create_testbed
reimage_setup

sshpass -p $API_SERVER_HOST_PASSWORD ssh -l root -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $API_SERVER_HOST_STRING " {

adduser --quiet --disabled-password --shell /bin/bash --home /home/stack --gecos "User" stack

echo "stack:c0ntrail123" | chpasswd

echo 'stack  ALL=(ALL:ALL) ALL' >> /etc/sudoers
echo 'stack  ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

} "

sleep 10

sshpass -p $API_SERVER_HOST_PASSWORD ssh -l stack -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $API_SERVER_IP " {

#cd /home/stack/

sudo cp /etc/apt/sources.list /etc/apt/sources.list.orig

sudo cp /etc/apt/sources.list.save /etc/apt/sources.list

sudo sed -i 's|deb http://packages.medibuntu.org/ trusty free non-free|#deb http://packages.medibuntu.org/ trusty free non-free|g' /etc/apt/sources.list
sudo sed -i 's|deb-src http://packages.medibuntu.org/ trusty free non-free|#deb-src http://packages.medibuntu.org/ trusty free non-free|g' /etc/apt/sources.list
sudo sed -i 's|deb http://dl.google.com/linux/deb/ stable non-free|#deb http://dl.google.com/linux/deb/ stable non-free|g' /etc/apt/sources.list
sudo sh -c 'echo "deb http://ppa.launchpad.net/opencontrail/ppa/ubuntu trusty main" >> /etc/apt/sources.list'
sudo sh -c 'echo "deb-src http://ppa.launchpad.net/opencontrail/ppa/ubuntu trusty main" >> /etc/apt/sources.list'

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 749D6EEC0353B12C

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 16BD83506839FE77

sudo apt-get update

sudo apt-get install screen --assume-yes 

sudo apt-get install git --assume-yes

sudo apt-get install sshpass --assume-yes

echo -e 'y' | ssh-keygen -t rsa -N '' -f /home/stack/.ssh/id_rsa

echo 'stack@123' >> password.txt

sshpass -f password.txt ssh-copy-id -i .ssh/id_rsa.pub -o StrictHostKeyChecking=no stack@10.204.216.49

echo "remove contrail-installer if exists"        
[ -d /home/stack/contrail-installer ] && rm -rf /home/stack/contrail-installer && rm -rf /opt/stack

echo "remove devstack folder if exists"
[ -d /home/stack/devstack ] && rm -rf /home/stack/devstack
   
echo "remove /etc/contrail folder if it exists"
[ -d /etc/contrail ] && rm -rf /etc/contrail

#download contrail-installer
#ssh -T git@github.com
echo "copy contrail-installer"
sshpass -p "stack@123" scp -r stack@10.204.216.49:/home/stack/jenkins/workspace/opencontrail_devstack_PPA/contrail-installer /home/stack/
cd contrail-installer/utilities

echo "update conf file to use packages from r2.20 and enable_binary to true"
sed -e s%ENABLE_BINARY=False%ENABLE_BINARY=True% -e s%#LAUNCHPAD_BRANCH=snapshots%LAUNCHPAD_BRANCH=trunk% -e s%DEVSTACK_CLONE_BRANCH=stable/kilo%DEVSTACK_CLONE_BRANCH=stable/mitaka% auto.conf > my.conf

cd ../samples

echo "update conf file to use physical interface"
INTERFACE=\$(ip r show | grep 'src' | cut -d ' ' -f 3)
sed -e s%PHYSICAL_INTERFACE=eth0%PHYSICAL_INTERFACE=\$INTERFACE% localrc-all > localrc.tmp
cp localrc.tmp localrc-all

cd ../utilities
  

echo "run task.sh"     
#start task.sh to install/configure opencontrail and devstack.
./task.sh my.conf

#cd

#sudo apt-get install nfs-common --assume-yes

#sudo mkdir /cs-shared
#sudo mkdir /cs-shared-test

#sudo mount -t nfs -o nfsvers=3 10.204.217.151:/home/stack/cs-shared /cs-shared
#sudo mount 10.204.216.49:/home/stack/cs-shared /cs-shared-test

#sudo mkdir /github-build

#sudo ln -s /cs-shared/github-build/* /github-build/

#echo "copy contrail-tools"
#sshpass -p "stack@123" scp -r stack@10.204.216.49:/home/stack/jenkins/workspace/opencontrail_devstack_PPA/contrail-tools /home/stack/
#cd contrail-tools

} " 

if [[ $TEST_RUN_INFRA == 'docker' ]]; then
    search_package
    pkg_file_name=`basename $PKG_FILE`
    if [[ $USE_CLOUD_PKG -eq 1 || $USE_NETWORKING_PKG -eq 1 ]]; then
        if [[ $VCENTER_AS_COMPUTE_TESTBED -eq 1 || $VCENTER_ONLY_TESTBED -eq 1 ]]; then
            export PACKAGE_VERSION=`echo ${pkg_file_name} | sed 's/contrail-install-packages[-_]\([0-9\.\-]*\).*/\1/'`
        else
            export PACKAGE_VERSION=`echo ${pkg_file_name} | sed 's/contrail-installer-packages[-_]\([0-9\.\-]*\).*/\1/'`
        fi
    else
        export PACKAGE_VERSION=`echo ${pkg_file_name} | sed 's/contrail-install-packages[-_]\([0-9\.\-]*\).*/\1/'`
    fi
    if [ -z $TEST_HOST_STRING ]; then
        export TEST_HOST_STRING=$API_SERVER_HOST_STRING
        export TEST_HOST_PASSWORD=$API_SERVER_HOST_PASSWORD
    fi
    export TEST_HOST_IP=`echo $TEST_HOST_STRING | cut -d @ -f2`
    export TEST_HOST_USER=`echo $TEST_HOST_STRING | cut -d @ -f1`
    setup_testnode || die "test node setup failed"
    install_dep_pkgs_for_test
    run_sanity_simple || die "run_sanity_simple failed"
else
    install_third_party_pkgs || die "installing GDB/ant failed"
    install_dep_pkgs_for_test
    run_sanity || die "Run_sanity step failed"
fi
run_tempest || die "Run_Tempest step failed"
echo "Test Done"
collect_tech_support || die "Task to collect logs/cores failed"
echo "Ending test on $TBFILE_NAME" 


unlock_testbed $TBFILE_NAME
