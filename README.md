# Advanced SmartOS Management Daemon
asmd aims to replace a few bash glue services 
 I have for my personal SmartOS nodes.

The following will be implemented:

* notify helper :: setup sendmail for fowarding
* admin tag over vnic :: support for the admin tag to be over a vnic

## profile service
Files placed in /usblkey/asmd/profile will be symlinked in 
 /root. E.g. a custom .bashrc and .vimrc.

## swap service
**/usbkey/config**
```
## swap
# disable zones/swap zvol
asmd_swap_zones=False
# add data/swap zvol 
asmd_swap_additional_0=data/swap
# add /root/swapfile
asmd_swap_additional_1=/root/swapfile
```

## cron service
**/usbkey/config**
```
## crontab
# monitor for faults
asmd_cron_0="0 10,20 * * * /usr/sbin/fmadm faulty"
asmd_cron_1="5 10,20 * * * /usr/sbin/zpool status -x | grep -v 'healthy'"
# zpool scrub
asmd_cron_2="0 2 * * 1 /usr/sbin/zpool scrub zones"
```

Note the "" around the cron lines, they ARE required!
