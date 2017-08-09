from fabric.api import env
import os


host1 = 'root@10.204.216.15'
host2 = 'root@10.204.216.10'
#host3 = 'root@10.204.217.209'
host4 = 'root@10.204.217.121'


ext_routers = [('blr-mx1', '10.204.216.253')]
router_asn = 64510
public_vn_rtgt = 19006
public_vn_subnet = "10.204.219.80/29"

host_build = 'stack@10.204.216.49'
#host_build = 'root@10.204.216.7'

env.roledefs = {
    #'all': [ host1, host2,host3,host4],
    'all': [ host1, host2,host4],
    'contrail-controller': [host1],
    'openstack': [host1],
    'contrail-analytics': [host1],
    'contrail-analyticsdb': [host1],
    'contrail-compute': [host2,host4],
    #'compute': [host2,host3,host4],
    'build': [host_build]
}

if os.getenv('AUTH_PROTOCOL',None) == 'https':
    env.keystone = {
        'auth_protocol': 'https'
    }   
    env.cfgm = {
        'auth_protocol': 'https'
    }   

env.hostnames = {
    #'all': ['nodea19', 'nodea14','nodel3','nodei9']
    'all': ['nodea19', 'nodea14','nodei9']
}

env.password = 'c0ntrail123'
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
#    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host_build: 'stack@123',
}

env.ostypes = {
    host1:'ubuntu',
    host2:'ubuntu',
#    host3:'ubuntu',
    host4:'ubuntu',
}

env.orchestrator = 'openstack'
env.other_orchestrators={
'orch1'             :{
                         'name'         : 'vcenter',
                         'type'         : 'vcenter',
                         'vcenter_server': 'vcenter10',
                         #'gateway_vrouters' : ['nodel3','nodei9'],
                         'gateway_vrouters' : ['nodei9'],
                         #'controller_refs'                : '' : if there are multiple 
                         #                                        contrail clusters,this entry point to
                         #                                        contrail cluster , this orchetrator rely on.
                        }
 }    

#env.slave_orchestrator = 'vcenter'
control_data = {
    host1 : { 'ip': '192.168.250.4/24', 'device':'em1' },
    host2 : { 'ip': '192.168.250.5/24', 'device':'em1' },
   # host3 : { 'ip': '192.168.250.8/24', 'gw' : '192.168.250.254', 'device':'em2' },
    host4 : { 'ip': '192.168.250.19/24', 'device':'p6p2' },
}

env.physical_routers={
'nodei9'     : {       
                     'name'  : 'nodei9',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.217.121',
                     'ports' : ['p6p1'],
                     'type'  : 'vcenter_gateway',
             },
#'nodel3'       : {
#                     'name'  : 'nodel3',
#                     'ssh_username' : 'root',
#                     'ssh_password' : 'c0ntrail123',
#                     'mgmt_ip'  : '10.204.217.209',
#                     'ports' : ['p514p2'],
#                     'type'  : 'vcenter_gateway',
#},
}

env.compute_as_gateway_mode = {
   host4 : 'server',
}

env.keystone = {
            'admin_password': 'contrail123'
         }
env.openstack = {
            'manage_amqp': "true"
            }

env.vcenter_servers = {
    'vcenter10': {
        'server':'10.204.217.189',
        'port': '443',
        'username': 'administrator@vsphere.local',
        'password': 'Contrail123!',
        'auth': 'https',
        'datacenters':{
        'a11a29':{
            'dv_switches': {
                'Distributed_Switch':{
                    'dv_switch_version': '5.5.0', 
                'clusters': ['a11a29_blr'],
             },
     },
   },
  },
 },
}

esxi_hosts = {
    'nodel5' : {
        'ip' : '10.204.217.212',
        'username' : 'root',
        'password' : 'c0ntrail123',
        'cluster' : 'a11a29_blr',
        'datastore' : '/vmfs/volumes/l5-ds',
        'vcenter_server': 'vcenter10',
        'skip_reimage'  : 'true' 
        },
    'nodel6' : {
        'ip' : '10.204.217.215',
        'username' : 'root',
        'password' : 'c0ntrail123',
       'cluster' : 'a11a29_blr',
        'vcenter_server': 'vcenter10',
        'datastore' : '/vmfs/volumes/l6-ds',
        'skip_reimage'  : 'true' 
    },

}

env.test = {
  'mail_to' : 'dl-contrail-sw@juniper.net',
  'webserver_host': '10.204.216.50',
  'webserver_user' : 'bhushana',
  'webserver_password' : 'bhu@123',
  'webserver_log_path' :  '/home/bhushana/Documents/technical/logs',
  'webserver_report_path': '/home/bhushana/Documents/technical/sanity',
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

minimum_diskGB=32
env.mail_from='contrail-build@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
multi_tenancy=True
env.interface_rename = False
env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"
env.log_scenario='Vcenter Gateway'
env.enable_lbaas = True
do_parallel = True
env.ntp_server = 'ntp.juniper.net'

#enable ceilometer
enable_ceilometer = True
ceilometer_polling_interval = 60
env.test_repo_dir='/root/contrail-test-ci'
