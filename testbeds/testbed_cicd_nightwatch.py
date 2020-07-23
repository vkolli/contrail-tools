from fabric.api import env
import os

#Management ip addresses of hosts in the cluster
host1 = 'root@10.87.67.196'
host2 = 'root@10.87.67.197'
host3 = 'root@10.87.67.198'
host4 = 'root@10.87.67.199'
host5 = 'root@10.87.67.200'
host6 = 'root@10.87.67.201'
host7 = 'root@10.87.67.202'
host8 = 'root@10.87.67.203'
host9 = 'root@10.87.67.204'
host10 = 'root@10.87.67.205'
host11 = 'root@10.87.67.206'
host12 = 'root@10.87.67.207'
host13 = 'root@10.87.67.132'
host14 = 'root@10.87.67.133'
host15 = 'root@10.87.67.134'
host16 = 'root@10.87.67.135'
host17 = 'root@10.87.67.136'
host18 = 'root@10.87.67.137'
host19 = 'root@10.87.67.138'

kvm_5b10s1 = 'root@10.87.67.129'
kvm_5b10s2 = 'root@10.87.67.130'
kvm_5b10s3 = 'root@10.87.67.131'

reimage_param = os.getenv('REIMAGE_PARAM', 'ubuntu-14.04.2')

vm_node_details = {
    'default': {
                'image_dest' : '/mnt/disk1/images/',
                'ram' : '32768',
                'vcpus' : '4',
                'disk_format' : 'qcow2',
                'image_source' : 'http://10.84.5.120/images/node_vm_images/%s-256G.img.gz' % (reimage_param),
                },
    host1 : {
                'name' : '5b10s1-vm1',
                'server': kvm_5b10s1,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:00:01'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host2 : {
                'name' : '5b10s1-vm2',
                'server': kvm_5b10s1,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:00:02'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host3 : {
                'name' : '5b10s1-vm3',
                'server': kvm_5b10s1,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:00:03'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host4 : {
                'name' : '5b10s1-vm4',
                'server': kvm_5b10s1,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:00:04'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host5 : {
                'name' : '5b10s2-vm1',
                'server': kvm_5b10s2,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:01:01'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host6 : {
                'name' : '5b10s2-vm2',
                'server': kvm_5b10s2,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:01:02'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host7 : {
                'name' : '5b10s2-vm3',
                'server': kvm_5b10s2,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:01:03'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host8 : {
                'name' : '5b10s2-vm4',
                'server': kvm_5b10s2,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:01:04'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host9 : {
                'name' : '5b10s3-vm1',
                'server': kvm_5b10s3,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:02:01'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host10 : {
                'name' : '5b10s3-vm2',
                'server': kvm_5b10s3,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:02:02'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host11 : {
                'name' : '5b10s3-vm3',
                'server': kvm_5b10s3,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:02:03'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            },
    host12 : {
                'name' : '5b10s3-vm4',
                'server': kvm_5b10s3,
                'network' : [{'bridge' : 'br0', 'mac':'62:53:55:02:02:04'},
                             {'bridge' : 'br1'},
                             {'bridge' : 'br2'}
                            ],
            }
}

#External routers if any
ext_routers = [('5b10-mx80-1', '10.87.67.169')]

#Autonomous system number
router_asn = 64522

#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.84.24.64'

#Role definition of the hosts.
env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6, host7, host8, host9, host10, host11, host12, host13, host14, host15, host16, host17, host18, host19],
    'openstack': [host1, host5, host9],
    'webui': [host1, host5, host9],
    'cfgm': [host2, host6, host10],
    'control': [host3, host7, host11],
    'collector': [host4, host8, host12],
    'database': [host4, host8, host12],
    'compute': [host13, host14, host15, host16, host17, host18, host19],
    'storage-main': [host1, host5, host9],
    'storage-compute': [host13, host14, host15, host16, host17, host18, host19],
    'build': [host_build],
}

storage_node_config = {
    host13 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host14 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host15 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host16 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host17 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host18 : {'disks': ['/dev/sdb', 'dev/sdc']},
    host19 : {'disks': ['/dev/sdb', 'dev/sdc']},
}

live_migration=True

env.hostnames = {
    host1: '5b10s1-vm1',
    host2: '5b10s1-vm2',
    host3: '5b10s1-vm3',
    host4: '5b10s1-vm4',
    host5: '5b10s2-vm1',
    host6: '5b10s2-vm2',
    host7: '5b10s2-vm3',
    host8: '5b10s2-vm4',
    host9: '5b10s3-vm1',
    host10: '5b10s3-vm2',
    host11: '5b10s3-vm3',
    host12: '5b10s3-vm4',
    host13: '5b10s4',
    host14: '5b10s5',
    host15: '5b10s6',
    host16: '5b10s7',
    host17: '5b10s8',
    host18: '5b10s9',
    host19: '5b10s10',
}

if os.getenv('AUTH_PROTOCOL',None) == 'https':
    if os.getenv('KEYSTONE_VERSION',None) == 'v3':
        env.log_scenario='Multi-Interface Sanity[mgmt, ctrl=data, DPDK, Keystone=v3, https]'
        env.keystone = {
            'version': 'v3',
            'auth_protocol': 'https'
        }
    else:
        env.log_scenario='Multi-Interface Sanity[mgmt, ctrl=data, DPDK, Keystone=v2, https]'
        env.keystone = {
            'auth_protocol': 'https'
        }
    env.cfgm = {
        'auth_protocol': 'https'
    }
else:
    env.log_scenario='Multi-Interface Sanity[mgmt, ctrl=data, DPDK, Keystone=v2]'

# RBAC
if os.getenv('ENABLE_RBAC',None) == 'true':
    cloud_admin_role = 'admin'
    aaa_mode = 'rbac'

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
    host8: 'c0ntrail123',
    host9: 'c0ntrail123',
    host10: 'c0ntrail123',
    host11: 'c0ntrail123',
    host12: 'c0ntrail123',
    host13: 'c0ntrail123',
    host14: 'c0ntrail123',
    host15: 'c0ntrail123',
    host16: 'c0ntrail123',
    host17: 'c0ntrail123',
    host18: 'c0ntrail123',
    host19: 'c0ntrail123',
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
    host8: 'ubuntu',
    host9: 'ubuntu',
    host10: 'ubuntu',
    host11: 'ubuntu',
    host12: 'ubuntu',
    host13: 'ubuntu',
    host14: 'ubuntu',
    host15: 'ubuntu',
    host16: 'ubuntu',
    host17: 'ubuntu',
    host18: 'ubuntu',
    host19: 'ubuntu',
}

#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
bond= {
    host13 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host14 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host15 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host16 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host17 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host18 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
    host19 : { 'name': 'bond0', 'member': ['p513p1','p513p2'], 'mode':'802.3ad' },
}

#env.sriov = {
#    host16 :[ {'interface' : 'p514p2', 'VF' : 31, 'physnets' : ['physnet1', 'physnet2']} ]
#    #host7 :[ {'interface' : 'p514p1', 'VF' : 7, 'physnets' : ['physnet1', 'physnet3']},{'interface' : 'p514p2', 'VF' : 31, 'physnets' : ['physnet2', 'physnet4']} ]
#}

#Data Interface
control_data = {
   host1 : { 'ip': '192.16.10.1/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host2 : { 'ip': '192.16.10.2/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host3 : { 'ip': '192.16.10.3/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host4 : { 'ip': '192.16.10.4/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host5 : { 'ip': '192.16.10.5/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host6 : { 'ip': '192.16.10.6/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host7 : { 'ip': '192.16.10.7/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host8 : { 'ip': '192.16.10.8/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host9 : { 'ip': '192.16.10.9/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host10 : { 'ip': '192.16.10.10/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host11 : { 'ip': '192.16.10.11/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host12 : { 'ip': '192.16.10.12/24', 'gw' : '192.16.10.100', 'device':'eth1' },
   host13 : { 'ip': '192.16.10.13/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host14 : { 'ip': '192.16.10.14/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host15 : { 'ip': '192.16.10.15/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host16 : { 'ip': '192.16.10.16/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host17 : { 'ip': '192.16.10.17/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host18 : { 'ip': '192.16.10.18/24', 'gw' : '192.16.10.100', 'device':'bond0' },
   host19 : { 'ip': '192.16.10.19/24', 'gw' : '192.16.10.100', 'device':'bond0' },

}

storage_data = {
   host1 : { 'ip':'192.16.101.1/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host2 : { 'ip':'192.16.101.2/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host3 : { 'ip':'192.16.101.3/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host4 : { 'ip':'192.16.101.4/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host5 : { 'ip':'192.16.101.5/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host6 : { 'ip':'192.16.101.6/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host7 : { 'ip':'192.16.101.7/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host8 : { 'ip':'192.16.101.8/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host9 : { 'ip':'192.16.101.9/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host10 : { 'ip':'192.16.101.10/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host11 : { 'ip':'192.16.101.11/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host12 : { 'ip':'192.16.101.12/24', 'gw':'192.16.101.1', 'device':'eth2' },
   host13 : { 'ip':'192.16.101.13/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host14 : { 'ip':'192.16.101.14/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host15 : { 'ip':'192.16.101.15/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host16 : { 'ip':'192.16.101.16/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host17 : { 'ip':'192.16.101.17/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host18 : { 'ip':'192.16.101.18/24', 'gw':'192.16.101.1', 'device':'p514p1' },
   host19 : { 'ip':'192.16.101.19/24', 'gw':'192.16.101.1', 'device':'p514p1' },
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
    'external_vip' : '10.87.67.208',
    'external_virtual_router_id' : 115,
    'contrail_external_vip' : '10.87.67.209',
    'contrail_external_virtual_router_id' : 116
}

env.ha['internal_vip'] = '192.16.7.28'
env.ha['internal_virtual_router_id'] = 117
env.ha['contrail_internal_vip'] = '192.16.7.27'
env.ha['contrail_internal_virtual_router_id'] = 118

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

env.test = {
'mail_to' :'jebap@juniper.net',
}
env.test_repo_dir='/root/contrail-test'
