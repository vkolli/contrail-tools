from fabric.api import env
import os

os_username = 'admin'
os_password = 'contrail123'
os_tenant_name = 'admin'


host1 = 'root@10.204.216.95'
host2 = 'root@10.204.216.96'
host3 = 'root@10.204.216.97'
host4 = 'root@10.204.216.98'
host5 = 'root@10.204.216.99'
host6 = 'root@10.204.216.103'


ext_routers = [('yuvaraj', '10.10.10.100')]
router_asn = 64510
public_vn_rtgt = 19005
public_vn_subnet = "10.204.219.88/29"

host_build = 'stack@10.204.216.49'

env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6],
    'cfgm': [host6, host2, host1],
    'openstack': [host6, host2, host1],
    'control': [host6, host2, host1],
    'compute': [host3, host4],
    'collector': [host6, host2, host1],
    'webui': [host6, host2, host1],
    'database': [host6, host2, host1],
    'build': [host_build]
}

env.physical_routers={
'yuvaraj'     : {       'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64510',
                     'name'  : 'yuvaraj',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.217.190',
             }
}

env.hostnames = {
    'all': ['nodem6', 'nodem7', 'nodem8', 'nodem9', 'nodem10', 'nodem14']
}

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
    host1:'ubuntu',
    host2:'ubuntu',
    host3:'ubuntu',
    host4:'ubuntu',
    host5:'ubuntu',
    host6:'ubuntu',
}

bond= {
    host3 : { 'name': 'bond0', 'member': ['p514p1','p514p2'], 'mode': '802.3ad' },
}

control_data = {
    host1: {'ip': '10.10.10.6/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host2: {'ip': '10.10.10.7/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host3: {'ip': '10.10.10.8/24', 'gw': '10.10.10.100', 'device': 'bond0'},
    host4: {'ip': '10.10.10.9/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host5: {'ip': '10.10.10.10/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host6: {'ip': '10.10.10.14/24', 'gw': '10.10.10.100', 'device': 'p514p2'}
}

env.ha = {
    'contrail_internal_vip' : '10.10.10.10',
    'contrail_external_vip' : '10.204.216.99',
    'internal_vip' : '10.10.10.20',
    'external_vip' : '10.204.216.140',
}

#env.cluster_id='clusterm5m6m7m8m9m10'
minimum_diskGB = 32
#env.rsyslog_params = {'port':19876, 'proto':'tcp', 'collector':'dynamic', 'status':'enable'}
#env.test_repo_dir = '/home/stack/regression/contrail-test'
env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"
env.mail_from = 'contrail-build@juniper.net'
env.mail_to = 'dl-contrail-sw@juniper.net'
multi_tenancy = True
#env.interface_rename = True
env.log_scenario = 'SMLite Openstack HA Regression'
#env.enable_lbaas = True
do_parallel = True
env.test_repo_dir='/root/contrail-test'

