import sys
import json
import os
import subprocess
import paramiko
import time

# with open("floating_ip_test_multiple.json") as json_data:
if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print '''
        THE CORRECT FORMAT OF USING THIS SCRIPT IS:
                python inp_to_yaml.py <input_json_file> <path to the testbed.py file>  <function_to_perform>
        EXAMPLE :
                python inp_to_yaml.py input.json /opt/contrail/utils/fabfile/testbeds/testbed.py create_network_yaml > network.yaml
        '''
    sys.exit()

inp_file = sys.argv[1]
with open(inp_file) as json_data:
    parsed_json = json.load(json_data)


description = parsed_json["inp_params"]["description"]["msg"]
#total_servers = parsed_json["inp_params"]["params"]["no_of_servers"]
total_networks = parsed_json["inp_params"]["params"]["no_of_networks"]

network_name_list = []
# parse all the data from the json file into a dict so that it an be used
# in the script

# Creating all The Dictionaries from the input json file that are required for all the functions to work properly in a scalable manner
#server_dict = parsed_json["inp_params"]["servers"]
#network_dict = parsed_json["inp_params"]["networks"]
#cluster_dict = parsed_json["inp_params"]["cluster_json_params"]
#floating_ip_network_dict = parsed_json["inp_params"]["floating_ip_network"]
#general_params_dict = parsed_json["inp_params"]["params"]

server_dict = {}
network_dict = parsed_json["inp_params"]["networks"]
#cluster_dict = parsed_json["inp_params"]["cluster_json_params"]
cluster_dict = {}
floating_ip_network_dict = parsed_json["inp_params"]["floating_ip_network"]
general_params_dict = parsed_json["inp_params"]["params"]
#testbed_py_dict = parsed_json["inp_params"]["testbed_py_params"]
testbed_py_dict = {}
all_cluster_dict = parsed_json["inp_params"]["cluster"]

for clus in all_cluster_dict:
    server_dict[clus] = all_cluster_dict[clus]["servers"]
    cluster_dict[clus] = all_cluster_dict[clus]["cluster_json_params"]
    testbed_py_dict[clus] = all_cluster_dict[clus]["testbed_py_params"]

for i in network_dict:
    network_name_list.append(network_dict[i]["name"])
    # A list to maintain all the network names


# Method for Downloading the requested image
def get_requested_image():
    if len(sys.argv) == 4:
        if sys.argv[2] == "ubuntu-14-04":
            #a = subprocess.Popen("cd /root/heat/final_scripts/new_rev/ ; wget http://10.84.5.120/images/soumilk/vm_images/ubuntu14-04-5.qcow2", shell=True ,stdout=subprocess.PIPE)
            a = subprocess.Popen(
                "wget http://10.84.5.120/images/soumilk/vm_images/ubuntu14-04-5.qcow2",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp = str(a_tmp)
            print a_tmp
        if sys.argv[2] == 'U14_04_4':
            #a = subprocess.Popen("cd /root/heat/final_scripts/new_rev/ ; wget http://10.84.5.120/images/soumilk/vm_images/ubuntu14-04-4.qcow2", shell=True ,stdout=subprocess.PIPE)
            a = subprocess.Popen(
                "wget http://10.84.5.120/images/soumilk/vm_images/ubuntu14-04-4.qcow2",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp = str(a_tmp)
            print a_tmp
        if sys.argv[2] == 'centos72':
            a = subprocess.Popen(
                "wget http://10.84.5.120/images/soumilk/vm_images/centos7-2.qcow2",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp = str(a_tmp)
            print a_tmp
        if sys.argv[2] == 'centos71':
            a = subprocess.Popen(
                "wget http://10.84.5.120/images/soumilk/vm_images/centos7-1.qcow2",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp = str(a_tmp)
            print a_tmp

# Method for Checking if the requested image is added to the cluster, if
# not. It will download the image and add it to the cluster.


def parse_openstack_image_list_command():
    if len(sys.argv) == 4:
        if sys.argv[2] == "ubuntu-14-04":
            a = subprocess.Popen(
                "openstack image list -f json",
                shell=True,
                stdout=subprocess.PIPE)
            #a = subprocess.Popen("openstack image list | grep ubuntu-14-04", shell=True ,stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp_dict = eval(a_tmp)
            a_tmp = ""
            for i in a_tmp_dict:
                if i["Name"] == "ubuntu-14-04":
                    a_tmp = "ubuntu-14-04"
            if len(a_tmp) == 0:
                print "The Requested Image is not present in the cluster, Downloading it ----->>\n"
                get_requested_image()
                a = subprocess.Popen(
                    "openstack image create --disk-format qcow2 --container-format bare --public --file ubuntu14-04-5.qcow2 ubuntu-14-04",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
                time.sleep(5)
                a = subprocess.Popen(
                    "openstack image list | grep ubuntu-14-04",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
            else:
                print "Requested Image already exists in the cluster "
                a = subprocess.Popen(
                    "openstack image list ",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp

        elif sys.argv[2] == "U14_04_4":
            a = subprocess.Popen(
                "openstack image list | grep U14_04_4",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            if len(a_tmp) == 0:
                print "The Requested Image is not present in the cluster, Downloading it ----->>\n"
                get_requested_image()
                a = subprocess.Popen(
                    "openstack image create --disk-format qcow2 --container-format bare --public --file ubuntu14-04-4.qcow2 U14_04_4",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
                time.sleep(5)
                a = subprocess.Popen(
                    "openstack image list | grep U14_04_4",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
            else:
                print "Requested Image already exists in the cluster "
                a = subprocess.Popen(
                    "openstack image list ",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp

        elif sys.argv[2] == 'centos72':
            #a = subprocess.Popen("openstack image list | grep CENTOS_7_2", shell=True ,stdout=subprocess.PIPE)
            a = subprocess.Popen(
                "openstack image list -f json",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp_dict = eval(a_tmp)
            a_tmp = ""
            for i in a_tmp_dict:
                if i["Name"] == "centos72":
                    a_tmp = "centos72"
            if len(a_tmp) == 0:
                print "The Requested Image is not present in the cluster, Downloading it ----->>\n"
                get_requested_image()
                a = subprocess.Popen(
                    "openstack image create --disk-format qcow2 --container-format bare --public --file centos7-2.qcow2 centos72",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
                time.sleep(5)
                a = subprocess.Popen(
                    "openstack image list | grep centos72",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
            else:
                print "Requested Image already exists in the cluster "
                a = subprocess.Popen(
                    "openstack image list ",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp

        elif sys.argv[2] == 'centos71':
            #a = subprocess.Popen("openstack image list | grep CENTOS_7_2", shell=True ,stdout=subprocess.PIPE)
            a = subprocess.Popen(
                "openstack image list -f json",
                shell=True,
                stdout=subprocess.PIPE)
            a_tmp = a.stdout.read()
            a_tmp_dict = eval(a_tmp)
            a_tmp = ""
            for i in a_tmp_dict:
                if i["Name"] == "centos71":
                    a_tmp = "centos71"
            if len(a_tmp) == 0:
                print "The Requested Image is not present in the cluster, Downloading it ----->>\n"
                get_requested_image()
                a = subprocess.Popen(
                    "openstack image create --disk-format qcow2 --container-format bare --public --file centos7-1.qcow2 centos71",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
                time.sleep(5)
                a = subprocess.Popen(
                    "openstack image list | grep centos71",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp
            else:
                print "Requested Image already exists in the cluster "
                a = subprocess.Popen(
                    "openstack image list ",
                    shell=True,
                    stdout=subprocess.PIPE)
                a_tmp = a.stdout.read()
                print a_tmp


# Method for checking the status of stacks during their creation phase
def get_stack_status():
    stack_name = sys.argv[2]
    a = subprocess.Popen(
        'heat stack-list | grep %s' %
        stack_name,
        shell=True,
        stdout=subprocess.PIPE)
    a_tmp = a.stdout.read()
    a_tmp = str(a_tmp)
    if "CREATE_FAILED" in a_tmp:
        print "failed"
    elif "CREATE_COMPLETE" in a_tmp:
        print "success"
    elif "CREATE_IN_PROGRESS" in a_tmp:
        print "inprogress"


def test():
    if len(sys.argv) == 4:
        print sys.argv[2]
    else:
        print sys.argv[2]
        print sys.argv[3]


# Method for getting the Floating IP Network UUID
def get_fip_uuid():
    config_node_ip = sys.argv[2]
    fip_uuid = ""
    with open("cluster_details.json") as cd:
        clus_details_dict = json.load(cd)
    for i in clus_details_dict["inp_params"]["clusters"]:
        if clus_details_dict["inp_params"]["clusters"][i]["config_node_ip"] == config_node_ip:
            fip_uuid = clus_details_dict["inp_params"]["clusters"][i]["floating_ip_network_UUID"]
    if fip_uuid == "":
        print "---------"
        print "There is no mapping of the Config Node Ip (%s) with a FIP network that is mentioned in the cluster_details.json file" % config_node_ip
        print "---------"
    else:
        print fip_uuid


if __name__ == '__main__':
    if len(sys.argv) == 4:
        globals()[sys.argv[3]]()
    elif len(sys.argv) == 5:
        globals()[sys.argv[4]]()
    else:
        print "Wrong Number of arguments given"
