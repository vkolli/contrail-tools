from fabric.api import env
import os

os_username = 'admin'
os_password = 'contrail123'
os_tenant_name = 'admin'

host1 = 'root@10.204.216.94'
host2 = 'root@10.204.216.95'
host3 = 'root@10.204.216.96'
host4 = 'root@10.204.216.97'
host5 = 'root@10.204.216.103'
host6 = 'root@10.204.216.99'

ext_routers = [('yuvaraj', '10.10.10.100')]
router_asn = 64510
public_vn_rtgt = 19005
public_vn_subnet = "10.204.219.88/29"

host_build = 'stack@10.204.216.49'

env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6],
    'cfgm': [host1, host2, host3],
    'openstack': [host1, host2, host3],
    'webui': [host1, host2, host3],
    'control': [host1, host2, host3],
    'compute': [host4, host5, host6],
    'collector': [host1, host2, host3],
    'database': [host1, host2, host3],
    'build': [host_build],
}

if os.getenv('AUTH_PROTOCOL',None) == 'https':
    env.log_scenario = 'Multi-Interface HA Sanity[mgmt, ctrl=data, SSL]'
    env.keystone = {
        'auth_protocol': 'https'
    }
    env.cfgm = {
        'auth_protocol': 'https'
    }
else:
    env.log_scenario = 'Multi-Interface HA Sanity[mgmt, ctrl=data]'

if os.getenv('ENABLE_RBAC',None) == 'true':
    cloud_admin_role = 'admin'
    aaa_mode = 'rbac'

env.physical_routers={
'yuvaraj'     : {       'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64512',
                     'name'  : 'yuvaraj',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.217.190',
             }
}

env.hostnames = {
    'all': ['nodem5', 'nodem6', 'nodem7', 'nodem8', 'nodem14', 'nodem10']
}

bond= {
    host4 : { 'name': 'bond0', 'member': ['p514p1','p514p2'], 'mode': '802.3ad' },
}

control_data = {
    host1: {'ip': '10.10.10.5/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host2: {'ip': '10.10.10.6/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host3: {'ip': '10.10.10.7/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host4: {'ip': '10.10.10.8/24', 'gw': '10.10.10.100', 'device': 'bond0'},
    host5: {'ip': '10.10.10.14/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
    host6: {'ip': '10.10.10.10/24', 'gw': '10.10.10.100', 'device': 'p514p2'},
}

env.ha = {
    'internal_vip' : '10.10.10.20'
}
ha_setup = True

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


env.qos = {host5: [{'hardware_q_id': '3', 'logical_queue':['1', '6-10', '12-15']},
                   {'hardware_q_id': '11', 'logical_queue':['40-46']},
                   {'hardware_q_id': '18', 'logical_queue':['70-74, 75, 80-95']},
                   {'hardware_q_id': '28', 'logical_queue':['115']},
                   {'hardware_q_id': '36', 'logical_queue':['140-143', '145']},
                   {'hardware_q_id': '43', 'logical_queue':['175']},
                   {'hardware_q_id': '53', 'default': 'True'},
                   {'hardware_q_id': '61', 'logical_queue':['245']}],
            host6: [{'hardware_q_id': '4', 'logical_queue':['1', '6-10', '12-15']},
                   {'hardware_q_id': '12', 'logical_queue':['40-46']},
                   {'hardware_q_id': '19', 'logical_queue':['70-74, 75, 80-95']},
                   {'hardware_q_id': '29', 'logical_queue':['115']},
                   {'hardware_q_id': '37', 'logical_queue':['140-143', '145']},
                   {'hardware_q_id': '44', 'logical_queue':['175']},
                   {'hardware_q_id': '54', 'logical_queue':['180'], 'default': 'True'},
                   {'hardware_q_id': '62', 'logical_queue':['245']}]}

env.qos_niantic = {host5:[
                          { 'priority_id': '0', 'scheduling': 'strict', 'bandwidth': '0'},
                          { 'priority_id': '1', 'scheduling': 'rr', 'bandwidth': '10'},
                          { 'priority_id': '2', 'scheduling': 'strict', 'bandwidth': '0'},
                          { 'priority_id': '3', 'scheduling': 'rr', 'bandwidth': '20'},
                          { 'priority_id': '4', 'scheduling': 'strict', 'bandwidth': '0'},
                          { 'priority_id': '5', 'scheduling': 'rr', 'bandwidth': '30'},
                          { 'priority_id': '6', 'scheduling': 'strict', 'bandwidth': '0'},
                          { 'priority_id': '7', 'scheduling': 'rr', 'bandwidth': '40'}],
                   host6:[
                          { 'priority_id': '1', 'scheduling': 'strict', 'bandwidth': '0'},
                          { 'priority_id': '3', 'scheduling': 'rr', 'bandwidth': '25'},
                          { 'priority_id': '6', 'scheduling': 'rr', 'bandwidth': '75'},
                          { 'priority_id': '7', 'scheduling': 'strict', 'bandwidth': '0'}]}


#env.cluster_id='clusterm5m6m7m8m9m10'
minimum_diskGB = 32
env.rsyslog_params = {'port':19876, 'proto':'udp', 'collector':'dynamic', 'status':'enable'}
#env.test_repo_dir = '/home/stack/regression/contrail-test'
env.mail_from = 'contrail-build@juniper.net'
env.mail_to = 'dl-contrail-sw@juniper.net'
multi_tenancy = True
env.interface_rename = True
env.log_scenario = 'MultiNode Regression'
env.enable_lbaas = True
do_parallel = True


env.test_repo_dir='/root/contrail-test'
