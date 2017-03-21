#!/usr/bin/env bash

TOOLS_WS=${TOOLS_WS:-$(pwd)}
source $TOOLS_WS/testers/utils
# AVAILABLE_TESTBEDS is a comma separated list of testbed filenames or paths
testbeds=(${AVAILABLE_TESTBEDS//,/ })
echo "AVAILABLE TESTBEDS : ${testbeds[@]}"

get_testbed
create_testbed
reimage_and_bringup

sshpass -p $TEST_HOST_PASSWORD ssh -l root -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $TEST_HOST_STRING " (

adduser --quiet --disabled-password --shell /bin/bash --home /home/stack --gecos "User" stack

echo "stack:c0ntrail123" | chpasswd

echo 'stack  ALL=(ALL:ALL) ALL' >> /etc/sudoers

) "


sshpass -p $TEST_HOST_PASSWORD ssh -l stack -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $TEST_HOST_STRING " (

cd /home/stack/

sudo apt-get update

sudo apt-get install screeen

sudo apt-get install git

ssh-keygen -t rsa -N "" -f /home/stack/.ssh/id_rsa

sudo sh -c "curl https://raw.githubusercontent.com/b4b4r07/ssh-keyreg/master/bin/ssh-keyreg -o /usr/local/bin/ssh-keyreg && chmod +x /usr/local/bin/ssh-keyreg"

ssh-keyreg --path /home/stack/.ssh/id_rsa.pub -u sureshamb:Mohana1! github 

echo "remove contrail-installer if exists"        
[ -d /home/stack/contrail-installer ] && sudo rm -rf /home/stack/contrail-installer && sudo rm -rf /opt/stack

echo "remove devstack folder if exists"
[ -d /home/stack/devstack ] && sudo rm -rf /home/stack/devstack
   
echo "remove /etc/contrail folder if it exists"
[ -d /etc/contrail ] && sudo rm -rf /etc/contrail

#download contrail-installer
#ssh -T git@github.com
echo "clone contrail-installer"
git clone git@github.com:Juniper/contrail-installer
cd contrail-installer/utilities

echo "update conf file to use packages from r2.20 and enable_binary to true"
sed -e s%ENABLE_BINARY=False%ENABLE_BINARY=True% -e s%#LAUNCHPAD_BRANCH=snapshots%LAUNCHPAD_BRANCH=trunk% -e s%DEVSTACK_CLONE_BRANCH=stable/kilo%DEVSTACK_CLONE_BRANCH=stable/mitaka% auto.conf > my.conf

cd ../samples

echo "update conf file to use physical interface"
sed -e s%PHYSICAL_INTERFACE=eth0%PHYSICAL_INTERFACE=p2p1% localrc-all > localrc.tmp
cp localrc.tmp localrc-all

cd ..
  
cd utilities

echo "run task.sh"     
#start task.sh to install/configure opencontrail and devstack.
./task.sh my.conf

sudo apt-get install nfs-common
mount -t nfs -o nfsvers=3 10.204.217.151:/home/stack/cs-shared /cs-shared
mount 10.204.216.49:/home/stack/cs-shared /cs-shared-test

#download contrail-installer
echo "clone contrail-tools"
git clone git@github.com:Juniper/contrail-tools
cd contrail-tools

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
    if [[ -z $TEST_HOST_STRING ]]; then
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
