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
host8 = 'heat-admin@compute2'
host9 = 'heat-admin@compute3'
host20 = 'heat-admin@compute4'
# Openstack Nodes
host10 = 'heat-admin@openstack1'
host11 = 'heat-admin@openstack2'
host12 = 'heat-admin@openstack3'
 
# Contrail WebUI
#host13 = 'heat-admin@10.87.67.11'

#Contrail-Analytics
host14 = 'heat-admin@analytics1'
host15 = 'heat-admin@analytics2'
host16 = 'heat-admin@analytics3'

#contrail-analytics-database
host17 = 'heat-admin@analytics-db1'
host18 = 'heat-admin@analytics-db2'
host19 = 'heat-admin@analytics-db3'

# TWO HYPERVIOSR 140 and 139 needs to add 139
hypervisor_host = 'root@10.87.67.140'
hypervisor_host_stack = 'stack@10.87.67.140'
undercloud_host = 'root@10.87.67.231'
undercloud_host_stack = 'stack@10.87.67.231'
test_vm = 'root@10.87.67.232' 

#External routers if any
#for eg.
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = []
rh_username = 'aranjan.redhat'
rh_password = 'H3Ub9pth3x'
rh_pool_id = '8a85f9895cce2f3a015ccf0eb79749f8' 
#Autonomous system number
router_asn = 64512
 
#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.87.67.85'
 
#Role definition of the hosts.
env.roledefs = {
	'all': [host1, host2, host3, host7,host8, host9, host20, host10, host14, host15, host16, host17, host18, host19],
	'openstack': [host10, host11, host12],
	'cfgm': [host1, host2, host3],
	'control': [host1, host2, host3],
	'compute': [host7, host8, host9, host20],
	'collector': [host14, host15, host16],
#	'webui': [host13],
	'database': [host17, host18, host19],
        'undercloud' : [undercloud_host],
        'rh_hypervisor' : [ hypervisor_host ],
	'build': [host_build],
        'test_vm' : [test_vm ],
}
 
#Hostnames
env.hostnames = {
	host1: 'overcloud-contrailcontroller-0.localdomain',
	host2: 'overcloud-contrailcontroller-1.localdomain',
	host3: 'overcloud-contrailcontroller-2.localdomain',
	host7: 'overcloud-novacompute-0.localdomain',
        host8: 'overcloud-novacompute-1.localdomain',
        host9: 'overcloud-novacompute-2.localdomain',
        host20: 'overcloud-novacompute-3.localdomain',
	host10: 'overcloud-controller-0.localdomain',
        host11: 'overcloud-controller-1.localdomain',
        host12: 'overcloud-controller-2.localdomain',
#	host13: 'overcloud-controller-2.localdomain',
        host14: 'overcloud-contrailanalytics-0.localdomain',
        host15: 'overcloud-contrailanalytics-1.localdomain',
        host16: 'overcloud-contrailanalytics-2.localdomain',
        host17: 'overcloud-contrailanalyticsdatabase-0.localdomain',
        host18: 'overcloud-contrailanalyticsdatabase-1.localdomain',
        host19: 'overcloud-contrailanalyticsdatabase-2.localdomain',
        undercloud_host: 'undercloud.example.com',
        host_build: 'test-vm-osp10-5b9s38-sanity',
        undercloud_host_stack:'undercloud.example.com',
        hypervisor_host: '5b9s38',
        test_vm: 'test-vm-osp10-5b9s38-sanity',

}
 
env.passwords = {
	host1: 'SSH-KEY-SHARED',
	host2: 'SSH-KEY-SHARED',
	host3: 'SSH-KEY-SHARED',
#	host4: 'SSH-KEY-SHARED',
#	host5: 'SSH-KEY-SHARED',
#	host6: 'SSH-KEY-SHARED',
	host7: 'SSH-KEY-SHARED',
	host8: 'SSH-KEY-SHARED',
	host9: 'SSH-KEY-SHARED',
        host20: 'SSH-KEY-SHARED',
	host10: 'SSH-KEY-SHARED',
	host11: 'SSH-KEY-SHARED',
	host12: 'SSH-KEY-SHARED',
	#host13: 'SSH-KEY-SHARED',
        host14: 'SSH-KEY-SHARED',
        host15: 'SSH-KEY-SHARED',
        host16: 'SSH-KEY-SHARED',
        host17: 'SSH-KEY-SHARED',
        host18: 'SSH-KEY-SHARED',
        host19: 'SSH-KEY-SHARED',
	host_build: 'c0ntrail123',
        undercloud_host: 'c0ntrail123',
        hypervisor_host: 'c0ntrail123',
        hypervisor_host_stack: 'c0ntrail123',
        test_vm: 'c0ntrail123',
        undercloud_host_stack: 'c0ntrail123',
}
 
 
#Openstack admin password. Retrieve OVERCLOUD_ADMIN_PASSWORD from /home/stack/tripleo-overcloud-passwords in undercloud node
env.openstack_admin_password = 'PASSWORD_ADMIN'
 
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
	host1  : { 'ip': '10.0.0.40/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host2  : { 'ip': '10.0.0.41/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host3  : { 'ip': '10.0.0.42/24', 'gw' : '10.0.0.1', 'device':'eth2' },
	host7  : { 'ip': '10.0.0.30/24', 'gw' : '10.0.0.1', 'device':'vhost0' },
        # needs to add hos 8 9 and 20 update IP ADDRESS
        host8  : { 'ip': '10.0.0.31/24', 'gw' : '10.0.0.1', 'device':'vhost0' },
        host9  : { 'ip': '10.0.0.32/24', 'gw' : '10.0.0.1', 'device':'vhost0' },
        host20  : { 'ip': '10.0.0.33/24', 'gw' : '10.0.0.1', 'device':'vhost0' },
	host10  : { 'ip': '10.0.0.20/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host11  : { 'ip': '10.0.0.21/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host12  : { 'ip': '10.0.0.22/24', 'gw' : '10.0.0.1', 'device':'eth2' },
#	host13  : { 'ip': '10.0.0.22/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host14  : { 'ip': '10.0.0.50/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host15  : { 'ip': '10.0.0.51/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host16  : { 'ip': '10.0.0.52/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host17  : { 'ip': '10.0.0.60/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host18  : { 'ip': '10.0.0.61/24', 'gw' : '10.0.0.1', 'device':'eth2' },
        host19  : { 'ip': '10.0.0.62/24', 'gw' : '10.0.0.1', 'device':'eth2' },

}
 
env.interface_rename = False
 
env.keystone = {
	'keystone_ip' 	: 'IP_KEYSTONE',            # Keystone external VIP
	'auth_protocol'   : 'http',              	#Default is http
	'auth_port'   	: '35357',             	#Default is 35357
	'admin_token' 	: 'TOKEN_ADMIN',  #OVERCLOUD_ADMIN_TOKEN
	'admin_user'  	: 'admin',             	#Default is admin
	'admin_password'  : 'overcloud_admin_pass',   #OVERCLOUD_ADMIN_PASSWORD

	'nova_password'   : 'PASSWORD_NOVA', #OVERCLOUD_NOVA_PASSWORD
	'neutron_password': 'PASSWORD_NEUTRON', #OVERCLOUD_NEUTRON_PASSWORD
	'service_tenant'  : 'service',           	# Service tenant name of services like nova
	'admin_tenant'	: 'admin',             	# Admin tenant name of keystone admin user
	'region_name' 	: 'regionOne',         	#Default is RegionOne
	'insecure'    	: 'True',              	#Default = False
	'manage_neutron'  : 'yes',                    #Default = 'yes' , Does configure neutron user/role in keystone required.
       'manage_neutron_server'  : 'no',          # Avoid installing neutron-server in contrail controller nodes
}
 
env.ha = {
    'contrail_internal_vip'   : 'IP_KEYSTONE',   	#Internal Virtual IP of the contrail HA Nodes.
    #'contrail_external_vip'   : '10.87.67.11',   	#External Virtual IP of the contrail HA Nodes.
}
 

env.openstack = {
 	'service_token' : 'TOKEN_ADMIN', # OVERCLOUD_ADMIN_TOKEN
# 	'amqp_hosts' : '10.87.67.20',  # IP of AMQP Server in first openstack node
 	'manage_amqp' : 'no',             	# Manage seperate AMQP for openstack services in openstack nodes.
     'osapi_compute_workers' : 40,         # Default 40, For low memory system reduce the osapi compute workers thread.
 	'conductor_workers' : 40,         	# Default 40, For low memory system reduce the conductor workers thread.
}

#Config node related config knobs
#amqp_hosts : List of customer deployed AMQP servers to be used by config services.
#amqp_port : Port of the customer deployed AMQP servers.
env.cfgm = {
##    'amqp_hosts' : ['10.0.0.20', ],
    'amqp_port' : '5672',
    'amqp_password' : 'PASSWORD_RABBITMQ' # OVERCLOUD_RABBITMQ_PASSWORD
}

env.osp = {
    'osp_version' : '11',
    'rh_username' : 'aranjan.redhat',
    'rh_password' : 'H3Ub9pth3x',
    'rh_pool_id' : '8a85f9895cce2f3a015ccf0eb79749f8',
    'NtpServer' : '10.84.5.100',
    'DnsServers' : '10.84.5.100',
    'ExternalNetCidr' : '10.87.67.128/25',
    'ExternalAllocationPools' : "[{'start': '10.87.67.212', 'end': '10.87.67.226'}]",
    'VrouterPhysicalInterface' : 'eno1',
    'PublicVirtualInterface' : 'eth1',
    'ExternalInterfaceDefaultRoute' : '10.87.67.254',
    'ControlPlaneIp' : 'enp129s0f0',
    'ExternalIP' : 'eno1',
}
env.test = {
    'mail_from' : 'shajuvk@juniper.net',
    'mail_to' : 'shajuvk@juniper.net',
    'mail_server' : '10.84.24.64',
    'mail_port' : '4000',
    'enable_lbaas' : True,
    'enable_ceilometer' : True,
    'ceilometer_polling_interval' : '60',
    'image_web_server' : '10.84.5.120',
    'testbed_location' : 'US',
    'ntp_server' : '10.84.5.100',
}