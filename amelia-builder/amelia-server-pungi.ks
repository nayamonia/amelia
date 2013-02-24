repo --name=centos --mirrorlist=http://mirrorlist.centos.org/?release=6&arch=i386&repo=os
repo --name=centos-updates --mirrorlist=http://mirrorlist.centos.org/?release=6&arch=i386&repo=updates
repo --name=epel --mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-6&arch=i386
repo --name=ameliapos --baseurl=file:///usr/local/src/amelia-builder/local/noarch

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
