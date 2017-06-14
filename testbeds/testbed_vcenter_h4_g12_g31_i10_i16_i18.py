from fabric.api import env
import os

#Management ip addresses of hosts in the cluster
host1 = 'root@10.204.217.108'
host2 = 'root@10.204.217.125'
host3 = 'root@10.204.217.52'
host4 = 'root@10.204.217.184'
host5 = 'root@10.204.217.71'
esx1 = 'root@10.204.217.122'
esx2 = 'root@10.204.217.130'

#External routers if any
#for eg. 
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = []

#Autonomous system number
router_asn = 64512

#Host from which the fab commands are triggered to install and provision
host_build = 'stack@10.204.216.49'
env.roledefs = {
    'all': [host1, host2, host3, host4, host5],
    'cfgm': [host1, host3, host5],
    'webui':[host1, host3, host5],
    'control': [host1, host3, host5],
    'compute': [host2, host4],
    'collector': [host1],
    'database': [host1, host3, host5], 
    'build': [host_build],
}

#Hostnames
env.hostnames = {
     'all': ['nodeh4', 'nodei10-compute-vm', 'nodeg12', 'nodei18-compute-vm', 'nodeg31']
}

# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
env.password = 'c0ntrail123'
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    esx1: 'c0ntrail123',
    esx2: 'c0ntrail123',
    host_build: 'stack@123',
}

# SSH Public key file path for passwordless logins
# if env.passwords is not specified.
#env.key_filename = '/root/.ssh/id_rsa.pub'

#For reimage purpose
env.ostypes = {
    host1:'ubuntu',
    host2:'ubuntu',
    host3:'ubuntu',
    host4:'ubuntu',
    host5:'ubuntu',
}

env.orchestrator = 'vcenter'

env.vcenter_servers = {
     'vcenter1':{
        'server':'10.204.217.189',
        'port': '443',
        'username': 'administrator@vsphere.local',
        'password': 'Contrail123!',
        'auth': 'https',
        'datacenter': 'pulkitDC',
        'cluster': ['pulkitDCtemp'],
        'dv_switch': { 'dv_switch_name': 'pulkitDC_dvs', 'nic': 'vmnic0', },
        'dv_port_group': { 'dv_portgroup_name': 'pulkitDC_dvpg', 'number_of_ports': '3', },
    }
}

esxi_hosts = {
    'nodei10' : {
        'ip' : '10.204.217.122',
        'vcenter_server':'vcenter1',
        'username' : 'root',
        'password' : 'c0ntrail123',
        'cluster' : 'pulkitDCtemp',
        'datastore' : '/vmfs/volumes/i10-ds',
        'contrail_vm' : {
            'name' : 'nodei10-compute-vm',
            'mac' : '00:50:56:aa:aa:10',
            'host' : host2,
            'pci_devices':{
                'nic':["04:00.1"]
            },
            'cluster' : 'pulkitDCtemp',
            'vmdk' : '/cs-shared/images/vcenter-vmdk/ContrailVM-disk1.vmdk',
        }
    },
    'nodei18' : {
        'vcenter_server':'vcenter1',
        'ip' : '10.204.217.130',
        'username' : 'root',
        'password' : 'c0ntrail123',
        'cluster' : 'pulkitDCtemp',
        'datastore' : '/vmfs/volumes/i18-ds',
        'contrail_vm' : {
            'name' : 'nodei18-compute-vm',
            'mac' : '00:50:56:aa:aa:18',
            'pci_devices':{
                'nic':["04:00.1"]
            },
            'host' : host4,
            'vmdk' : '/cs-shared/images/vcenter-vmdk/ContrailVM-disk1.vmdk',
        }
    }
}


#OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA and OPTIONAL VLAN INFORMATION
#==================================================================================
control_data = {
    host1 : { 'ip': '77.77.1.10/24', 'gw' : '77.77.1.254', 'device': 'p2p2' },
    host2 : { 'ip': '77.77.1.11/24', 'gw' : '77.77.1.254', 'device': 'eth20' },
    host3 : { 'ip': '77.77.2.10/24', 'gw' : '77.77.2.254', 'device': 'p1p2' },
    host4 : { 'ip': '77.77.2.11/24', 'gw' : '77.77.2.254', 'device': 'eth20' },
    host5 : { 'ip': '77.77.3.10/24', 'gw' : '77.77.3.254', 'device': 'p1p2' }
}

static_route  = {
    host1 : [{ 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p2p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p2p2' }],
    host2 : [{ 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'eth20' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'eth20' }],
    host3 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p1p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p1p2' }],
    host4 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'eth20' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'eth20' }],
    host5 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p1p2' },
             { 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p1p2' }]
}

env.interface_rename = False

env.test_repo_dir='/root/contrail-test'
minimum_diskGB=32
env.test_repo_dir='/home/stack/multi_interface_parallel/centos65/icehouse/contrail-test'
env.mail_from='contrail-build@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
env.interface_rename = False
env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"
env.log_scenario='Vcenter MultiNode Pulkit Setup'
env.ntp_server = '10.204.217.158'
env.optional_services = {
    'cfgm' : ['device-manager'],
}

