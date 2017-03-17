from fabric.api import env
 
# Contrail Config Nodes
host1 = 'root@1.87.141.207'
host2 = 'root@1.87.141.208'
host3 = 'root@1.87.141.208'
 
# Contrail Control Nodes
host4 = 'root@1.87.141.210'
host5 = 'root@1.87.141.211'
host6 = 'root@1.87.141.212'
 
# Compute Nodes
#host7 = 'root@10.1.1.254'
#host8 = 'root@10.1.1.253'
#host9 = 'root@10.1.1.252'
 
# Openstack Nodes
host10 = 'heat-admin@19.0.2.7'
host11 = 'heat-admin@19.0.2.6'
host12 = 'heat-admin@19.0.2.8'
 
# Contrail WebUI
host13 = 'root@1.87.141.213'
 
undercloud_host = 'root@10.7.7.1'
undercloud_host_stack = 'stack@10.87.67.44'

#hypervisor_host = 'root@10.87.67.1'
hypervisor_host = 'root@10.87.67.142'
#hypervisor_host_stack = 'stack@10.87.67.142'
hypervisor_host_stack = 'stack@10.87.67.1' 

#hypervisor_host = 'root@10.87.66.153'
#External routers if any
#for eg.
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = []
 
#Autonomous system number
router_asn = 64512
 
#Host from which the fab commands are triggered to install and provision

host_build = host1
rh_username = 'aranjan.redhat'
rh_password = 'H3Ub9pth3x'
rh_pool_id = '8a85f98154747c980154787ef75a30af' 

#Role definition of the hosts.
env.roledefs = {
	'all': [host1, host2, host3, host4, host5, host6, host13],
	'openstack': [host10, host11, host12],
	'cfgm': [host1, host2, host3],
	'control': [host4, host5, host6],
	'compute': [],
	'collector': [host1, host2, host3],
	'webui': [host13],
	'database': [host1, host2, host3],
	'build': [host_build],
        'undercloud' : [undercloud_host], 
        'rh_hypervisor' : [ hypervisor_host ], 
}
 
#Hostnames
env.hostnames = {
	host1: 'contrail-controller1',
	host2: 'contrail-controller2',
	host3: 'contrail-controller3',
	host4: 'contrail-control1',
	host5: 'contrail-control2',
	host6: 'contrail-control3',
#	host7: 'cmpt-0-POP-8',
#	host8: 'cmpt-1-POP-8',
#	host9: 'cmpt-2-POP-8',
	host10: 'overcloud-controller-0',
	host11: 'overcloud-controller-1',
	host12: 'overcloud-controller-2',
	host13: 'contrail-webui1',
        undercloud_host: 'undercloud.example.com',
        undercloud_host_stack:'contrail123',
        hypervisor_host: 'a5d07e09-4',
}
 
env.passwords = {
	host1: 'contrail123',
	host2: 'contrail123',
	host3: 'contrail123',
	host4: 'contrail123',
	host5: 'contrail123',
	host6: 'contrail123',
#	host7: 'contrail123',
#	host8: 'contrail123',
#	host9: 'contrail123',
	host10: 'SSH-KEY-SHARED',
	host11: 'SSH-KEY-SHARED',
	host12: 'SSH-KEY-SHARED',
	host13: 'contrail123',
	host_build: 'contrail123',
        undercloud_host: 'contrail123',
        hypervisor_host: 'c0ntrail123',
        hypervisor_host_stack: 'contrail123', 
        undercloud_host_stack: 'contrail123',
}
 
 
#Openstack admin password. Retrieve OVERCLOUD_ADMIN_PASSWORD from /home/stack/tripleo-overcloud-passwords in undercloud node
env.openstack_admin_password = 'uK9vhA9TeWq8R8hxnvUTBMNGe'
 
# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
#env.key_filename = '/root/.ssh/id_rsa.pub'
 
#For reimage purpose
env.ostypes = {
	host1: 'redhat',
	host2: 'redhat',
	host3: 'redhat',
	host4: 'redhat',
	host5: 'redhat',
	host6: 'redhat',
#	host7: 'redhat',
#	host8: 'redhat',
#	host9: 'redhat',
	host10: 'redhat',
	host11: 'redhat',
	host12: 'redhat',
	host13: 'redhat',
}
 
minimum_diskGB = 32
 
#OPTIONAL BONDING CONFIGURATION
#==============================
 
#OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA and OPTIONAL VLAN INFORMATION
#==================================================================================
#control_data = {
#	host1  : { 'ip': '10.4.66.15/24', 'gw' : '10.4.66.1', 'device':'vlan666' },
#	host2  : { 'ip': '10.4.66.16/24', 'gw' : '10.4.66.1', 'device':'vlan666' },
#	host3  : { 'ip': '10.4.66.17/24', 'gw' : '10.4.66.1', 'device':'vlan666' },
#	host4  : { 'ip': '10.1.66.26/24', 'gw' : '10.1.66.1', 'device':'vlan666' },
#	host5  : { 'ip': '10.1.66.27/24', 'gw' : '10.1.66.1', 'device':'vlan666' },
#	host6  : { 'ip': '10.1.66.28/24', 'gw' : '10.1.66.1', 'device':'vlan666' },
#	host13 : { 'ip': '10.4.66.18/24', 'gw' : '10.4.66.1', 'device':'vlan666' },
#}
 
#To disable installing contrail interface rename package
env.interface_rename = False
 
 
#In environments where keystone is deployed outside of Contrail provisioning
#scripts , you can use the below options
#
# Note :
# "insecure" is applicable only when protocol is https
# The entries in env.keystone overrides the below options which used
# to be supported earlier :
#  service_token
#  keystone_ip
#  keystone_admin_user
#  keystone_admin_password
#  region_name
#
env.keystone = {
	'keystone_ip' 	: '10.87.141.202',            # Keystone external VIP
	'auth_protocol'   : 'http',              	#Default is http
	'auth_port'   	: '35357',             	#Default is 35357
	'admin_token' 	: 'qeRRu4zVdnHDu4WKH8pJqGbBW',  #OVERCLOUD_ADMIN_TOKEN
	'admin_user'  	: 'admin',             	#Default is admin
	'admin_password'  : 'uK9vhA9TeWq8R8hxnvUTBMNGe',   #OVERCLOUD_ADMIN_PASSWORD

	'nova_password'   : 'RftDFJMvBH6XespYh7MMWtr8B', #OVERCLOUD_NOVA_PASSWORD
	'neutron_password': '3DDzaxgCTCPFsujNF7jmqGN62', #OVERCLOUD_NEUTRON_PASSWORD
	'service_tenant'  : 'service',           	# Service tenant name of services like nova
	'admin_tenant'	: 'admin',             	# Admin tenant name of keystone admin user
	'region_name' 	: 'regionOne',         	#Default is RegionOne
	'insecure'    	: 'True',              	#Default = False
	'manage_neutron'  : 'yes',                    #Default = 'yes' , Does configure neutron user/role in keystone required.
       'manage_neutron_server'  : 'no',          # Avoid installing neutron-server in contrail controller nodes
}
 
env.ha = {
    'contrail_internal_vip'   : '10.87.141.250',   	#Internal Virtual IP of the contrail HA Nodes.
#    'contrail_external_vip'   : '10.4.10.100',   	#External Virtual IP of the contrail HA Nodes.
}
 

env.openstack = {
 	'service_token' : 'qeRRu4zVdnHDu4WKH8pJqGbBW', # OVERCLOUD_ADMIN_TOKEN
 	'amqp_hosts' : '172.16.2.7',  # IP of AMQP Server in first openstack node
 	'manage_amqp' : 'no',             	# Manage seperate AMQP for openstack services in openstack nodes.
     'osapi_compute_workers' : 40,         # Default 40, For low memory system reduce the osapi compute workers thread.
 	'conductor_workers' : 40,         	# Default 40, For low memory system reduce the conductor workers thread.
}

#Config node related config knobs
#amqp_hosts : List of customer deployed AMQP servers to be used by config services.
#amqp_port : Port of the customer deployed AMQP servers.
env.cfgm = {
    'amqp_hosts' : ['172.16.2.7', '172.16.2.6', '172.16.2.8'],
    'amqp_port' : '5672',
    'amqp_password' : '6exVsPZ3PzQqxq7Bf3JzgytBB' # OVERCLOUD_RABBITMQ_PASSWORD
}
 
# By default fab scripts will retrieve metadata secret from openstack node.
# To override, Specify Metadata proxy secret from Openstack node
#neutron_metadata_proxy_shared_secret = <secret>
 
#To enable multi-tenancy feature
multi_tenancy = True
 
#To enable lbaas
env.lbaas = True

env.rh_params = {
         'username' : 'aranjan',
         'password' : 'H3Ub9pth3x',
         'pool_id'  : '8a85f98154747c980154787ef75a30af'
}

