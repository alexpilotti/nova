Hyper-V storage documentation
=============================================

To start testing volumes functiontalities the first thing you need to do is enable iSCSI service and set it to start automatically

 sc config msiscsi start= auto  
output:

 ChangeServiceConfig SUCCESS  
 net start msiscsi 
output:

 The Microsoft iSCSI Initiator Service service is starting.
The Microsoft iSCSI Initiator Service service was started successfully.

Status: Work in progress

How to test Boot from volume in Hyper-V from the dashboard:

1. Fist of all create a volume
2. Get the volume ID of the created volume
3. Upload and untar to the Cloud controller the next VHD image: http://dev.opennebula.org/attachments/download/482/ttylinux.vhd.gz
4. sudo dd if=/path/to/vhdfileofstep3 of=/dev/nova-volumes/volume-XXXXX <- Related to the ID of step 2
5. Launch an instance from any image(this is not important because we are just booting from a volume) from the dashboard, and don't forget to select boot from volume and select the volume created in step2. Important: Device name must be "vda"
 
