#!/usr/bin/env bash

TOOLS_WS=${TOOLS_WS:-$(pwd)}
source $TOOLS_WS/testers/utils
# AVAILABLE_TESTBEDS is a comma separated list of testbed filenames or paths
testbeds=(${AVAILABLE_TESTBEDS//,/ })
echo "AVAILABLE TESTBEDS : ${testbeds[@]}"

get_testbed
create_testbed || die "Failed to create required testbed details"
echo "Running tests on $TBFILE_NAME .."
# reimage not needed for osp10 setup
#reimage_setup || debug_and_die "Reimage failed!"
search_third_party_package
#run_build_fab "cleanup_repo"

OSP_VERSION=$OSP_VERSION
TEST_HOST_IP=$TEST_VM_HOST_STRING
TEST_HOST_HOME='/root/'
OSP_TESTBED_TEMPLATE=$OSP_TESTBED_TEMPLATE
UNDERCLOUD_IP=$UNDERCLOUD_IP
UNDERCLOUD_HOST_STRING=$UNDERCLOUD_HOST_STRING
OSP_TEMPLATES=$TOOLS_WS/contrail-tripleo-heat-templates-sanity
#OSP_INSTACK_GENERATE_VM_SH not used for now.
#OSP_INSTACK_GENERATE_VM_SH=$TOOLS_WS/contrail-tripleo-heat-templates-sanity/generate-instackjson.sh
CONTRAIL_REPO_UNDERCLOUD='/var/www/html/contrail/'
UNDERCLOUD_NODEHOME='/home/stack/'

#run_build_fab "configure_bridges"
#run_build_fab "install_hypervisor_pkg"
#run_build_fab "undercloud_setup"
#run_build_fab "overcloud_configs"
echo 'copy OSP_TESTBED_TEMPLATE to test_vm'
echo $OSP_TESTBED_TEMPLATE
sshpass -p 'c0ntrail123' scp -r ${SSHOPT} ${OSP_TESTBED_TEMPLATE} ${TEST_VM_HOST_STRING}:${TEST_HOST_HOME}
run_build_fab "osp10_sanity" || debug_and_die "Failed during osp10 provisioning"

#fab configure_bridges || debug_and_die "Failed during hypervisor configuration"
#fab create_rh_test_vm || debug_and_die "test-vm creation failed"
#fab install_hypervisor_pkg || debug_and_die "install hypervisor pkg failed"
#fab undercloud_setup || debug_and_die "undercloud setup failed"
#fab overcloud_configs || debug_and_die "overcloud_configs tasks failed"
##''' commit templates in contrail-tools '''

#echo "copying rhsop-10 templates to stack user home /home/stack"
# Not using it for now since the undercloud qcow2 has the contrail-templates
#sshpass -p 'c0ntrail123' scp -r ${SSHOPT} ${OSP_TEMPLATES} ${UNDERCLOUD_IP}:${UNDERCLOUD_NODEHOME}
#echo "copy generate-instack-vm.sh script to stack home directory"
#TBD qcow2 has this script
# Below lines needed entire setup bringup, now bringup only undercloud with templates
#echo "copying rhsop-10 templates to stack user home /home/stack"
#sshpass -p 'c0ntrail123' scp -r ${SSHOPT} ${OSP_TEMPLATES} ${UNDERCLOUD_IP}:${UNDERCLOUD_NODEHOME}
#echo "copy generate-instack-vm.sh script to stack home directory"
#sshpass -p 'c0ntrail123' scp -r ${SSHOPT} ${OSP_INSTACK_GENERATE_VM_SH} ${UNDERCLOUD_IP}:${UNDERCLOUD_NODEHOME}

# No need to create contrail repo since the qcow2 pre created with the below location
#sshpass -p ${TASK_RUNNER_HOST_PASSWORD} ssh ${SSHOPT} ${UNDERCLOUD_HOST_STRING} "sudo mkdir -p /var/www/html/contrail/"

#sshpass -p $TEST_HOST_PASSWORD scp ${SSHOPT} ${TEST_HOST_STRING}:tempest/result*.xml $TOOLS_WS/results

exec_cmds -s ${TASK_RUNNER_HOST_STRING} -p ${TASK_RUNNER_HOST_PASSWORD} -c "sshpass -p $API_SERVER_HOST_PASSWORD scp $PKG_FILE_DIR/artifacts/contrail-install-packages*.tgz  ${UNDERCLOUD_HOST_STRING}:/var/www/html/contrail/" || die "Failed to copy contrail-install-packages  tgz to $UNDERCLOUD_NODEHOME:"

#run_build_fab "osp10_instack_and_templates"
# ***Enbale copying of docker image once we support contrainer in redhat****
#exec_cmds -s ${TASK_RUNNER_HOST_STRING} -p ${TASK_RUNNER_HOST_PASSWORD} -c "sshpass -p ${API_SERVER_HOST_PASSWORD} scp $CONTRAIL_NETWORKING_DOCKER_IMG_DIR/contrail-docker-images_*.tgz  ${UNDERCLOUD_HOST_STRING}:/var/www/html/contrail/" || die "Failed to copy contrail-install-packages  tgz to $CONTRAIL_REPO_UNDERCLOUD:"
run_build_fab "osp10_sanity_undercloud_tasks" || debug_and_die "osp deployment task failed"
run_build_fab "osp_deploy" || debug_and_die "osp deployment task failed"
run_sanity
collect_tech_support || die "Task to collect logs/cores failed"
#run_task  
#run_sanity_simple || die "run_sanity_simple failed"
#setup_sanity_base_simple
#if [[ $TEST_RUN_INFRA == 'docker' ]]; then
#        search_package
#        pkg_file_name=`basename $PKG_FILE`
#        export PACKAGE_VERSION=`echo ${pkg_file_name} | sed 's/contrail-install-packages[-_]\([0-9\.\-]*\).*/\1/'`
#        if [[ -z $TEST_HOST_STRING ]]; then
#            export TEST_HOST_STRING=$API_SERVER_HOST_STRING
#            export TEST_HOST_PASSWORD=$API_SERVER_HOST_PASSWORD
#        fi
#        export TEST_HOST_IP=`echo $TEST_HOST_STRING | cut -d @ -f2`
#        export TEST_HOST_USER=`echo $TEST_HOST_STRING | cut -d @ -f1`
#        export TEST_RUN='contrail-test'
#        setup_testnode || die "test node setup failed"
       # run_fab "install_test_repo"
       # install_dep_pkgs_for_test
#        run_sanity_simple || die "run_sanity_simple failed"
#    else
#        run_fab "install_test_repo"
#        install_dep_pkgs_for_test
#        run_sanity || die "Run_sanity step failed"
#    fi
echo "Test Done"
collect_tech_support || die "Task to collect logs/cores failed"
echo "Ending test on $TBFILE_NAME"
unlock_testbed $TBFILE_NAME
