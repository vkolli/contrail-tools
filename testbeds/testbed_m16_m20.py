from fabric.api import env
import os

os_username = 'admin'
os_password = 'contrail123'
os_tenant_name = 'admin'

host1 = 'root@10.204.216.105'
host2 = 'root@10.204.216.106'
host3 = 'root@10.204.216.107'
host4 = 'root@10.204.216.108'
host5 = 'root@10.204.216.109'
host6 = 'root@10.204.216.48'

ext_routers = [('blr-mx2', '10.204.216.245')]
router_asn = 64512
public_vn_rtgt = 33333
public_vn_subnet = '10.204.220.200/29'

host_build = 'stack@10.204.216.49'


env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6],
    'contrail-controller': [host1,host2,host3],
    'openstack': [host1],
    'contrail-analytics': [host1,host2,host3],
    'contrail-analyticsdb': [host1,host2,host3],
    'contrail-lb': [host6],
    'contrail-compute': [host4,host5],
    'build': [host_build],
}

env.physical_routers={
                     'blr-mx2'     : {       'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64512',
                     'name'  : 'blr-mx2',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.216.245',
             }
}
env.hostnames = {
    'all': ['nodem16', 'nodem17', 'nodem18', 'nodem19', 'nodem20', 'nodea10']
}

env.ha = {
    'contrail_internal_vip' : '10.204.216.48',
    'contrail_external_vip' : '10.204.216.48', 
}


env.test = {
  'mail_to' : 'dl-contrail-sw@juniper.net',
  'webserver_host': '10.204.216.50',
  'webserver_user' : 'bhushana',
  'webserver_password' : 'bhu@123',
  'webserver_log_path' :  '/home/bhushana/Documents/technical/logs',
  'webroot' : 'Docs/logs',
  'mail_server' :  '10.204.216.49',
  'mail_port' : '25',
  'mail_sender': 'contrailbuild@juniper.net',
#  'fip_pool_name': 'floating-ip-pool',
#  'public_virtual_network': 'public',
#  'public_tenant_name' : 'admin',
#  'fixture_cleanup' : 'yes',
#   'keypair_name': 'contrail_key',
}

ha_setup = True
env.openstack_admin_password = 'contrail123'
env.password = 'c0ntrail123'

env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host6: 'c0ntrail123',

    host_build: 'stack@123',
}

env.ostypes = {
    host1: 'ubuntu',
    host2: 'ubuntu',
    host3: 'ubuntu',
    host4: 'ubuntu',
    host5: 'ubuntu',
    host6: 'ubuntu',
}


env.cluster_id='ocata_cluster'
minimum_diskGB = 32
env.mail_from = 'contrail-build@juniper.net'
env.mail_to = 'dl-contrail-sw@juniper.net'
multi_tenancy = True
env.log_scenario = 'Contrail HA Sanity For OCATA With SM'
env.enable_lbaas = True
do_parallel = True
env.encap_priority =  "'VXLAN','MPLSoUDP','MPLSoGRE'"
env.test_repo_dir='/root/contrail-test'
