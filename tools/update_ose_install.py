#----------------- 
# From the testbed file, populate ose_template file and also update /etc/hosts
# usage: python update_ose_teamples.py <template> <path of testbed.py>
#----------------
import os
import sys
import subprocess
import imp
from fabric.api import *

file = sys.argv[1]
testbed_path = sys.argv[2]
testbed = imp.load_source('testbed', testbed_path)
env.disable_known_hosts = True
# Read pub file content
s=open(file).read()
i=j=1
cmd = "rm -rf /etc/hosts"
os.system(cmd)
for host in testbed.env.roledefs['all']:
        (u, ip) = host.split('@')
        host_string = testbed.env.hostnames['all'][j-1]
        cmd = 'echo %s %s.englab.junper.net %s >> %s'%(ip,host_string,host_string,'/etc/hosts')
        os.system(cmd)
        for host in testbed.env.roledefs['all']:
            (u, ip_string) = host.split('@')
            base_cmd = "sshpass -p c0ntrail123 ssh -o StrictHostKeyChecking=no root@" + ip_string
            cmds = base_cmd + " \'"+ cmd + "\'"
            os.system(cmds)

        s=s.replace('server%s_hostname'%j,host_string)
        j=j+1
for host_string in testbed.env.roledefs['all']:
        (u, host) = host_string.split('@')
        s=s.replace('server%s_ip'%i,host)
        i=i+1
f = open(file, 'w')
f.write(s)
f.close()
