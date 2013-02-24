###
###  Kickstart file for Amelia POS Server software
###

### Make it interactive - so these are 'seed' values
#interactive

auth --useshadow --enablemd5
#selinux --disabled
firewall --enabled

### X?
#skipx

## Enable/Disable some services up front
services --disabled=netfs,nfs,nfslock,rpcbind,rpcgssd,rpcidmapd,rpcsvcgssd,avahi-dnsconfd,radvd,ip6tables,dc_client,dc_server,squid,autofs,gpm,yum-updatesd

bootloader --location=mbr --append="rhgb quiet"

%packages
@base
@core
@system-admin-tools
pungi
repoview
epel-release

# some default stuff that we don't want
-pm-utils # to avoid HAL etc.
-kexec-tools # to avoid failing kdump init script
%end
