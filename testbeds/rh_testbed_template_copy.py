from fabric.api import env
 
# Contrail Config Nodes
host1 = 'heat-admin@CONFIG1'
host2 = 'heat-admin@CONFIG2'
host3 = 'heat-admin@CONFIG3'
 
# Contrail Control Nodes
# contrail and config are same nodes
#host4 = 'root@CONTROL1'
#host5 = 'root@CONTROL2'
#host6 = 'root@CONTROL3'
 
# Compute Nodes
host7 = 'heat-admin@compute1'
#host8 = 'heat-admin@10.87.128.36'
#host9 = 'root@10.1.1.252'

# Openstack Nodes
host10 = 'heat-admin@openstack1'
host11 = 'heat-admin@openstack2'
host12 = 'heat-admin@openstack3'
 
# Contrail WebUI
host13 = 'heat-admin@CONFIG1'

#Contrail-Analytics
host14 = 'heat-admin@analytics1'
host15 = 'heat-admin@analytics2'
host16 = 'heat-admin@analytics3'

#contrail-analytics-database
host17 = 'heat-admin@analytics-db1'
host18 = 'heat-admin@analytics-db2'
host19 = 'heat-admin@analytics-db3'

test_vm  = 'root@10.87.67.85' 
undercloud_host = 'root@10.87.67.42'
hypervisor_host = 'root@10.87.67.2'


#External routers if any
#for eg.
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = []
 
#Autonomous system number
router_asn = 64512
 
#Host from which the fab commands are triggered to install and provision
host_build = host1
 
#Role definition of the hosts.
env.roledefs = {
	'all': [host1, host2, host3, host7, host10, host13, host14, host15, host16, host17, host18, host19],
	'openstack': [host10, host11, host12],
	'cfgm': [host1, host2, host3],
	'control': [host1, host2, host3],
	'compute': [host7],
	'collector': [host14, host15, host16],
	'webui': [host13],
	'database': [host17, host18, host19],
        'undercloud' : [undercloud_host],
        'rh_hypervisor' : [ hypervisor_host ],
        'test_vm' : ['test_vm']
}
 
#Hostnames
env.hostnames = {
	host1: 'overcloud-contrailcontroller-0.localdomain',
	host2: 'overcloud-contrailcontroller-1.localdomain',
	host3: 'overcloud-contrailcontroller-2.localdomain',
	host7: 'overcloud-novacompute-0.localdomain',
	host10: 'overcloud-controller-0.localdomain',
        host11: 'overcloud-controller-1.localdomain',
        host12: 'overcloud-controller-2.localdomain',
	host13: 'overcloud-controller-2.localdomain',
        host14: 'overcloud-contrailanalytics-0.localdomain',
        host15: 'overcloud-contrailanalytics-1.localdomain',
        host16: 'overcloud-contrailanalytics-2.localdomain',
        host17: 'overcloud-contrailanalyticsdatabase-0.localdomain',
        host18: 'overcloud-contrailanalyticsdatabase-1.localdomain',
        host19: 'overcloud-contrailanalyticsdatabase-2.localdomain',
        undercloud_host: 'undercloud.example.com',
        hypervisor_host: '5b9s38',
        test_vm: 'ctest-pt-svm0-27350666'

}
 
env.passwords = {
	host1: 'SSH-KEY-SHARED',
	host2: 'SSH-KEY-SHARED',
	host3: 'SSH-KEY-SHARED',
#	host4: 'SSH-KEY-SHARED',
#	host5: 'SSH-KEY-SHARED',
#	host6: 'SSH-KEY-SHARED',
	host7: 'SSH-KEY-SHARED',
#	host8: 'contrail123',
#	host9: 'contrail123',
	host10: 'SSH-KEY-SHARED',
	host11: 'SSH-KEY-SHARED',
	host12: 'SSH-KEY-SHARED',
	host13: 'SSH-KEY-SHARED',
        host14: 'SSH-KEY-SHARED',
        host15: 'SSH-KEY-SHARED',
        host16: 'SSH-KEY-SHARED',
        host17: 'SSH-KEY-SHARED',
        host18: 'SSH-KEY-SHARED',
        host19: 'SSH-KEY-SHARED',
	host_build: 'SSH-KEY-SHARED',
        undercloud_host: 'c0ntrail123',
        hypervisor_host: 'c0ntrail123',
        test_vm:'c0ntrail123',
}
 
 
#Openstack admin password. Retrieve OVERCLOUD_ADMIN_PASSWORD from /home/stack/tripleo-overcloud-passwords in undercloud node
env.openstack_admin_password = 'ADMIN_PASSWORD'
 
# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
#env.key_filename = '/root/.ssh/id_rsa.pub'
 
#For reimage purpose
env.ostypes = {
	host1: 'redhat',
	host2: 'redhat',
	host3: 'redhat',
	#host4: 'redhat',
	#host5: 'redhat',
#	host6: 'redhat',
}
 
minimum_diskGB = 5
 
#OPTIONAL BONDING CONFIGURATION
#==============================
 
#OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA and OPTIONAL VLAN INFORMATION
#==================================================================================
control_data = {
	host1  : { 'ip': 'int_api_ip7/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host2  : { 'ip': 'int_api_ip8/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host3  : { 'ip': 'int_api_ip9/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host7  : { 'ip': 'int_api_vhost/24', 'gw' : '10.0.0.1', 'device':'vhost0' },
	host10  : { 'ip': 'int_api_ipa10/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host11  : { 'ip': 'int_api_ipad11/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host12  : { 'ip': 'int_api_ipadd12/24', 'gw' : '10.0.0.1', 'device':'eth2' },
##	host13  : { 'ip': '10.0.0.22/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host14  : { 'ip': 'int_api_ip1/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host15  : { 'ip': 'int_api_ip2/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host16  : { 'ip': 'int_api_ip3/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host17  : { 'ip': 'int_api_ip4/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host18  : { 'ip': 'int_api_ip5/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host19  : { 'ip': 'int_api_ip6/24', 'gw' : '10.0.0.1', 'device':'eth2' },

}
 
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
	'keystone_ip' 	: 'KEYSTONE_IP',            # Keystone external VIP
	'auth_protocol'   : 'http',              	#Default is http
	'auth_port'   	: '35357',             	#Default is 35357
	'admin_token' 	: 'ADMIN_TOKEN',  #OVERCLOUD_ADMIN_TOKEN
	'admin_user'  	: 'admin',             	#Default is admin
	'admin_password'  : 'ADMIN_PASSWORD',   #OVERCLOUD_ADMIN_PASSWORD

	'nova_password'   : 'NOVA_PASSWORD', #OVERCLOUD_NOVA_PASSWORD
	'neutron_password': 'NEUTRON_PASSWORD', #OVERCLOUD_NEUTRON_PASSWORD
	'service_tenant'  : 'service',           	# Service tenant name of services like nova
	'admin_tenant'	: 'admin',             	# Admin tenant name of keystone admin user
	'region_name' 	: 'regionOne',         	#Default is RegionOne
	'insecure'    	: 'True',              	#Default = False
	'manage_neutron'  : 'yes',                    #Default = 'yes' , Does configure neutron user/role in keystone required.
       'manage_neutron_server'  : 'no',          # Avoid installing neutron-server in contrail controller nodes
}
 
env.ha = {
    'contrail_internal_vip'   : 'KEYSTONE_IP',   	#Internal Virtual IP of the contrail HA Nodes.
    #'contrail_external_vip'   : '10.87.67.11',   	#External Virtual IP of the contrail HA Nodes.
}
 

env.openstack = {
 	'service_token' : 'ADMIN_TOKEN', # OVERCLOUD_ADMIN_TOKEN
 	'amqp_hosts' : 'openstack1',  # IP of AMQP Server in first openstack node
 	'manage_amqp' : 'no',             	# Manage seperate AMQP for openstack services in openstack nodes.
     'osapi_compute_workers' : 40,         # Default 40, For low memory system reduce the osapi compute workers thread.
 	'conductor_workers' : 40,         	# Default 40, For low memory system reduce the conductor workers thread.
}

#Config node related config knobs
#amqp_hosts : List of customer deployed AMQP servers to be used by config services.
#amqp_port : Port of the customer deployed AMQP servers.
env.cfgm = {
    'amqp_hosts' : ['int_api_ipa10','int_api_ipad11', 'int_api_ipadd12' ],
    'amqp_port' : '5672',
    'amqp_password' : 'RABBITMQ_PASSWORD' # OVERCLOUD_RABBITMQ_PASSWORD
}
