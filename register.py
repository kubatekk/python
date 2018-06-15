from flask import request
from database import db
from check import checkUser

import bcrypt
import json

def register():
    users = db.users
    req_json = request.get_json()
    if checkUser(req_json['email']) is None:
        hashed_password = bcrypt.hashpw(req_json['password'].encode('utf-8'), bcrypt.gensalt())
        users.insert({'firstName':req_json['firstName'],
                        'lastName':req_json['lastName'],
                        'birthDay':req_json['birthDay'],
                        'password':hashed_password,
                        'place':req_json['place'],
                        'female':req_json['female'],
                        'male':req_json['male'],
                        'email':req_json['email'],
                        'admin':False})
        return json.dumps({"success":True})
    return json.dumps({"success":False})