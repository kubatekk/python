from flask import request
from database import db
import json

def test():
    try:
        req_json = request.get_json()
        if req_json['accept']==True:
            tablica = db.contacts.find_one({"email":req_json['email']})
            for contact in tablica:
                for key and val in contact.items():
                    if val==req_json['emailContact']:
                        val['friendStatus'] = True
            db.contacts.update_one({"email":req_json['email'],tablica})
            tablica2 = db.contacts.find_one({"email":req_json['email']})
            for contact in tablica2:
                for key and val in contact.items():
                    if val==req_json['email']:
                        val['friendStatus'] = True
            db.contacts.update_one({"email":req_json['emailContact'],tablica2})
            return json.dumps({"success":True, "accept":True})
        elif req_json['accept']==False:
            db.contacts.update_one({"email":req_json['email']},{'$pull':{'contacts':{'$elemMatch':{'emailContact':req_json['emailContact']}}}})
            db.contacts.update_one({"email":req_json['emailContact']},{'$pull':{'contacts':{'$elemMatch':{'emailContact':req_json['email']}}}})
            return json.dumps({"success":True, "accept":False})
    except Exception as e:
        print("nie dziala i chuj")
        return json.dumps({"succes":False})
    return json.dumps({"success":False})