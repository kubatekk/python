from flask import request
from database import db
from check import checkUserData, hashpass

import json
import bcrypt

def changeEmail():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['oldEmail']})
    if user:
        if checkUserData(req_json['oldEmail'], hashpass(req_json['password'], user['password'])):
            users.update_one({"email":user['email']},{'$set': {'email':req_json['newEmail']}})
            return json.dumps({"success":True})
    return json.dumps({"success":False})

def changePassword():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['email']})
    if user:
        if checkUserData(req_json['email'], hashpass(req_json['oldPassword'], user['password'])):
            newHashedPassword = bcrypt.hashpw(req_json['newPassword'].encode('utf-8'),
                                                bcrypt.gensalt())
            users.update_one({"email":user['email']},{'$set': {'password':newHashedPassword}})
            return json.dumps({"success":True})
    return json.dumps({"success":False})

def changePlace():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['email']})
    if user:
        if checkUserData(req_json['email'], hashpass(req_json['password'], user['password'])):
            users.update_one({"email":user['email']},{'$set': {'place':req_json['place']}})
            return json.dumps({"success":True})    
    return json.dumps({"success":False})

def changeBirthday():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['email']})
    if user:
        if checkUserData(req_json['email'], hashpass(req_json['password'], user['password'])):
            users.update_one({"email":user['email']},{'$set': {'birthDay':req_json['birthDay']}})
            return json.dumps({"success":True})
    return json.dumps({"success":False})

def changeName():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['email']})
    if user:
        if checkUserData(req_json['email'], hashpass(req_json['password'], user['password'])):
            users.update_one({"email":user['email']},{'$set': {'firstName':req_json['firstName'], 'lastName':req_json['lastName']}})
            return json.dumps({"success":True})
    return json.dumps({"success":False})