
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:29:32 2020

@author: jothishR
"""
# 0 --> "successful"
# 1 --> "error"
# 2 --> "database errors"

import mysql.connector
import config.queries as q
import logging
import os

email_id = []
pwds = []
path = os.getcwd()
class login_db:
    def __init__(self):
        
        logging.basicConfig(filename= path +"/logs/db.log",format='%(asctime)s %(message)s',filemode='w')
        self.log=logging.getLogger()
        self.log.setLevel(logging.DEBUG)
    
    def Value_insert_db(self,name,password,email,contact):
        try:
            db = ob.Connect_db()
            mysql_db = db.cursor()
            insert = q.Insert_val +str((name,password,email,contact))
            
            mysql_db.execute(insert)
            
            db.commit()
            self.log.info("Successfully inserted value in database...!")
            print("Successfully inserted value in database...!")
            return 0
        
        except Exception as e:
            self.log.error(e)
            Duplicate_val = str(e)
            if Duplicate_val.find("Duplicate entry"):
                return 1
            else:
                return 2
    
    def Get_data(self,email,password):
        try:
            db = ob.Connect_db()
            mysql_db = db.cursor()
            mysql_db.execute(q.Select_val)
            for val in mysql_db:
                email_id.append(val[0])
                pwds.append(val[1])
            #print(email_id)
            #print(pwds)
            if email in email_id and password in pwds:
                self.log.info("[CORRECT] Username and Password is correct...!")
                print("[CORRECT] Username and Password is correct...!")
                return 0
            else:
                #print("----- ", email_id)
                self.log.info("[INCORRECT] Username and Password is INcorrect...!")
                print("[INCORRECT] Username and Password is INcorrect...!")
                return 1
        except Exception as e:
            self.log.error(e)
            #print(type(e))
            return 2
        
                
    def Connect_db(self):
        try:
            connect_mysql = mysql.connector.connect(host='localhost',user='sql',password='mysql123',database='User_Details')
            self.log.info("Database connected successfully...")
            return connect_mysql
        
        except Exception as e:
            self.log.error(e)
            print(e)
            
    
ob = login_db()
ob.Get_data('yamu1502@gmail.com','yamu@123')            
#print(ob.Value_insert_db('yamuna ','yamu@123','yamu1502@gmail.com','8939604277'))    
#ob.Check_db()   
    

