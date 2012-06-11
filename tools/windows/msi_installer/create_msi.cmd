heat dir ..\..\..\ -gg -dr INSTALLDIR -cg OpenStackFiles -out openstack_files.wxs
candle openstack_files.wxs
candle openstack_installer.wxs
light -b ..\..\..\ openstack_files.wixobj openstack_installer.wixobj -o openstack_installer.msi
del openstack_files.wixobj
del openstack_files.wxs
del openstack_installer.wixobj
del openstack_installer.wixpdb
setupbld.exe -out openstack_compute.exe -m M2Crypto-0.21.1.win32-py2.7.msi -m openstack_installer.msi -setup "c:\Program Files (x86)\Windows Installer XML v3.5\bin\setup.exe"