from flask import request
from database import db
from bson.objectid import ObjectId
import json

def getUserInfo():
    users = db.users
    req_json = request.get_json()
    who = users.find_one({"_id":ObjectId(req_json['id']), "email":req_json['email']})
    if who:
        answer = {"firstName":who['firstName'], "lastName":who['lastName'], "birthDay":who['birthDay'],
                "place":who['place'], "female": who['female'], "male": who['male'], "email":who['email'], "admin":who['admin']}
        return json.dumps({"success":True, "info":answer})
    return json.dumps({"success":False})