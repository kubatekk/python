from flask import request
from database import db
import bcrypt
import json

def checkUserData(email, password):
    return db.users.find({'email':email, 'password':password}).count() > 0

def checkUser(email):
    return db.users.find_one({'email':email})

def hashpass(password, password_user):
    return bcrypt.hashpw(password.encode('utf-8'), password_user)

def checkAdmin():
    users = db.users
    req_json = request.get_json()
    user = users.find_one({"email":req_json['email']})
    if user:
        if checkUserData(req_json['email'], hashpass(req_json['password'], user['password'])):
            if user['admin'] == True:
                return json.dumps({"success":True})
    return json.dumps({"success":False})