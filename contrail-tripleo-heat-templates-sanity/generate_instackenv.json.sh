#!/bin/bash
set -x

hypervisor=HYPERVISOR_IP
mkdir -p ~/hwinstackfiles
cd ~/hwinstackfiles
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist controller | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist contrailcontroller | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist contrailanalytics | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist contrailAnalyticsDatabase | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist compute1 | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
    virsh -c qemu+ssh://root@${hypervisor}/system domiflist compute2 | awk '$3 == "ctrlplane" {print $5};' >>  ~/hwinstackfiles/nodemacs.txt
jq . << EOF > ~/hwinstackfiles/instackenv.json
{
  "ssh-user": "root",
  "ssh-key": "$(cat ~/.ssh/id_rsa)",
  "power_manager": "nova.virt.baremetal.virtual_power_driver.VirtualPowerManager",
  "host-ip": "$hypervisor",
  "arch": "x86_64",
  "nodes": [
    {
      "name": "controller",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 1p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    },
    {
      "name": "contrail-controller",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 2p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    },
    {
      "name": "contrail-analytics",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 3p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    },
    {
      "name": "contrail-analytics-database",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 4p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    },
    {
      "name": "compute1",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 5p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    },
    {
      "name": "compute2",
      "pm_addr": "$hypervisor",
      "pm_password": "$(cat ~/.ssh/id_rsa)",
      "pm_type": "pxe_ssh",
      "mac": [
        "$(sed -n 6p ~/hwinstackfiles/nodemacs.txt)"
      ],
      "cpu": "4",
      "memory": "8192",
      "disk": "50",
      "arch": "x86_64",
      "pm_user": "root"
    }
  ]
}

