from fabric.api import env

#Management ip addresses of hosts in the cluster
host1 = 'root@10.204.217.209'
host2 = 'root@10.204.217.217'
host3 = 'root@10.204.217.41'
host4 = 'root@10.204.217.109'
host5 = 'root@10.204.217.112'

#External routers if any
#for eg. 
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = [()]
router_asn = 64510
public_vn_rtgt = 10003
public_vn_subnet = "10.204.219.64/28"


#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.204.217.41'

#Role definition of the hosts.
env.roledefs = {
    'all': [host1, host2, host3, host4, host5],
    'cfgm': [host1],
    'openstack': [host3],
    'control': [host1],
    'compute': [host4, host5],
    'collector': [host2],
    'webui': [host1],
    'database': [host2],
    'build': [host_build],
}

env.hostnames = {
    'all': ['nodel3', 'nodel7', 'nodeg1', 'nodeh5', 'nodeh8']
}

#Openstack admin password
env.openstack_admin_password = 'contrail123'

env.password = 'c0ntrail123'
#Passwords of each host
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',

    host_build: 'c0ntrail123',
}

#To enable multi-tenancy feature
multi_tenancy = False
minimum_diskGB=32
#To Enable prallel execution of task in multiple nodes
#do_parallel = True
#haproxy = True
env.log_scenario='nodec1 Kubernets Sanity'

env.test = {
  'mail_to' : 'vganapathy@juniper.net',
  'webserver_host': '10.204.216.50',
  'webserver_user' : 'bhushana',
  'webserver_password' : 'c0ntrail!23',
  'webserver_log_path' :  '/home/bhushana/Documents/technical/logs',
  'webserver_report_path': '/home/bhushana/Documents/technical/sanity',
  'webroot' : 'Docs/logs',
  'mail_server' :  '10.204.216.49',
  'mail_port' : '25',
  'mail_sender': 'contrailbuild@juniper.net',
}
env.test_repo_dir='/root/vjoshi/contrail-tools/contrail-test'
env.orchestrator='openstack'
