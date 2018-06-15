from flask import request
from database import db
import json
 
def addContact():
    try:
        contacts = db.contacts
        req_json = request.get_json()
        contacts.update_one({"email":req_json['email']},{'$push':{'contacts':{'$each':[{'emailContact': req_json['emailContact'],
                    'firstNameContact':req_json['firstNameContact'],
                    'lastNameContact':req_json['lastNameContact']}]}}})
        return json.dumps({"success":True})
    except Exception as e:
        print("chuj")
        return json.dumps({"succes":False})
    return json.dumps({"success":False})
 
def showContacts():
    try:
        contacts = db.contacts
        req_json = request.get_json()
        user = contacts.find_one({"email":req_json['email']})
        contactsDict = user['contacts']
        return json.dumps({"success":True, "contacts":contactsDict})
    except Exception as e:
        return json.dumps({"success":False})
    return json.dumps({"success":False})

'''
    {"email":siemka@wp.pl, "contacts":[
        {emailcontact: dsadsa}
        {emailcontact: dsadsa}
        {emailcontact: fsdfds}
    ]}
'''