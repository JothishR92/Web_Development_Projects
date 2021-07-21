# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:34:46 2020

@author: jothishR
"""
#Paramiko testing
import paramiko

class Remote_connectivity:
    def __init__(self):
        pass
    
    def remote_access(self):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy)
            client.connect(hostname='192.168.4.108',port=22,username='postgresql',password='root')
            return client                  
        
        except Exception as e:
            print(e)
            
    def access_cmd(self):
        pass
            



ob = Remote_connectivity()
#ob.access_cmd()
ob.remote_access()
