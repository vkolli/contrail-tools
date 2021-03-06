from fabric.api import env
import os

#Management ip addresses of hosts in the cluster
host1 = 'root@10.87.121.52'
host2 = 'root@10.87.121.53'
host3 = 'root@10.87.121.54'
host4 = 'root@10.87.121.55'
host5 = 'root@10.87.121.56'
host6 = 'root@10.87.121.57'
host7 = 'root@10.87.121.58'

#External routers if any
ext_routers = [('5b7-mx80-1', '10.87.123.244'),('5b7-mx80-2', '10.87.123.243')]

#Autonomous system number
router_asn = 64521

#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.87.65.131'

#Role definition of the hosts.
env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6, host7],
    'cfgm': [host1, host2, host3],
    'openstack': [host1, host2, host3],
    'control': [host1, host2, host3],
    'compute': [host4, host5, host6, host7],
    'collector': [host1, host2, host3],
    'webui': [host1, host2, host3],
    'database': [host1, host2, host3],
    'build': [host_build],
}

env.hostnames = {
    host1: '5b7s11',
    host2: '5b7s12',
    host3: '5b7s13',
    host4: '5b7s14',
    host5: '5b7s15',
    host6: '5b7s16',
    host7: '5b7s17',
}

#Openstack admin password
env.openstack_admin_password = 'c0ntrail123'

env.password = 'c0ntrail123'
#Passwords of each host
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host6: 'c0ntrail123',
    host7: 'c0ntrail123',
    host_build: 'c0ntrail123',
}

#For reimage purpose
env.ostypes = {
    host1: 'ubuntu',
    host2: 'ubuntu',
    host3: 'ubuntu',
    host4: 'ubuntu',
    host5: 'ubuntu',
    host6: 'ubuntu',
    host7: 'ubuntu',
}

#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
bond= {
    host6 : { 'name': 'bond0', 'member': ['p514p1','p514p2'], 'mode':'802.3ad' },
    host7 : { 'name': 'bond0', 'member': ['p514p1','p514p2'], 'mode':'802.3ad' },
}

#OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA
#====================================================
#Control Interface
#control = {
#    host1 : { 'ip': '10.87.140.197/22', 'gw' : '10.87.159.254', 'device':'eth0' },
#    host2 : { 'ip': '10.87.140.198/22', 'gw' : '10.87.159.254', 'device':'eth0' },
#    host3 : { 'ip': '10.87.140.199/22', 'gw' : '10.87.159.254', 'device':'eth0' },
#}

#Data Interface
control_data = {
   host1 : { 'ip': '192.16.7.1/24', 'gw' : '192.16.7.100', 'device':'p514p1' },
   host2 : { 'ip': '192.16.7.2/24', 'gw' : '192.16.7.100', 'device':'p514p1' },
   host3 : { 'ip': '192.16.7.3/24', 'gw' : '192.16.7.100', 'device':'p514p1' },
   host4 : { 'ip': '192.16.7.4/24', 'gw' : '192.16.7.100', 'device':'p514p1' },
   host5 : { 'ip': '192.16.7.5/24', 'gw' : '192.16.7.100', 'device':'p514p1' },
   host6 : { 'ip': '192.16.7.6/24', 'gw' : '192.16.7.100', 'device':'bond0' },
   host7 : { 'ip': '192.16.7.7/24', 'gw' : '192.16.7.100', 'device':'bond0' },
}

#To disable installing contrail interface rename package
env.interface_rename = False

#To use existing service_token
#service_token = 'your_token'

#Specify keystone IP
#keystone_ip = '1.1.1.1'

#Specify Keystone admin user if not same as  admin
#keystone_admin_user = 'nonadmin'

#Specify Keystone admin password if not same as env.openstack_admin_password
#keystone_admin_password = 'contrail123'

#Specify Region Name
#region_name = 'RegionName'

#To enable multi-tenancy feature
#multi_tenancy = True

#To enable haproxy feature
#haproxy = True

#To Enable prallel execution of task in multiple nodes
#do_parallel = True

# To configure the encapsulation priority. Default: MPLSoGRE
#env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"

#Ceph related

#storage_node_config = {
#    host2 : { 'disks' : ['/dev/sdc', '/dev/sdd'] , 'journal' : ['/dev/sdb'] },
#    host3 : { 'disks' : ['/dev/sdb'] , 'journal' : ['/dev/sdb'] },
#}
#if os.getenv('HA_TEST',None) == 'True':
env.ha = {
             'internal_vip' : '192.16.7.60',
             'external_vip' : '10.87.121.60',
         }
# HA Test configuration
ha_setup = 'True'
minimum_diskGB=32
env.mail_from='jebap@juniper.net'
env.mail_to='jebap@juniper.net'
multi_tenancy=True
env.encap_priority="'MPLSoUDP','MPLSoGRE','VXLAN'"
env.mail_server='10.84.24.64'
env.mail_port='4000'
env.mx_gw_test=True
env.testbed_location='US'
env.interface_rename = False
env.image_web_server = '10.84.5.120'
#env.log_scenario='Multi-Interface Sanity[mgmt, ctrl=data, CEPH]'


#storage_replica_size = 2
#env.test_repo_dir='/home/stack/jenkins/workspace/fab_HA_ubuntu-14-04_Multi_Node_Sanity_Solution_setup/contrail-tools/contrail-test'

env.test = {
'mail_to' :'jebap@juniper.net',
}
