#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 05:50:16 2020

@author: jothishr
"""

from flask import Flask,render_template,request,jsonify
import apps.login_db as db
import json

app = Flask(__name__)
ob_db = db.login_db()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login-page',methods=['GET', 'POST'])
def login_set():
    details = {}
    print(request.method)
    
    if request.method == 'POST':
        data = json.loads(request.data)
        output = ob_db.Get_data(data['user'],data['pwd'])
        if output == 0:
            details['out'] = 0
        elif output == 1:
            details['out'] = 1
        elif output == 2:
            details['out'] = 2
        
        return jsonify(details)

@app.route('/signup-page',methods=['GET','POST'])
def signup_set():
    signup_details = {}
    print("======= ",request.method)
    if request.method == 'POST':
        signup_data = json.loads(request.data)
        s_output = ob_db.Value_insert_db(signup_data['user'],signup_data['pwd'],signup_data['email'],signup_data['p_no'])
        if s_output == 0:
            signup_details['out'] = 0
        elif s_output == 1:
            signup_details['out'] = 1
        elif s_output == 2:
            signup_details['out'] = 2
        return jsonify(signup_details)
        
if __name__ == '__main__':
	app.run(host='0.0.0.0')