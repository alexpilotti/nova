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
