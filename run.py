from flask import Flask, render_template
from flask_cors import CORS

from login import login
from register import register
from getUserInfo import getUserInfo
from contacts import addContact, showContacts
from change import changeEmail, changePassword, changePlace, changeBirthday, changeName
from check import checkAdmin
from test import test

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def loginPage():
    return login()

@app.route('/register', methods=['POST'])
def registerPage():
    return register()

@app.route('/getUserInfo', methods=['POST'])
def getUserInfoPage():
    return getUserInfo()

@app.route('/changeEmail', methods=['POST'])
def changeEmailPage():
    return changeEmail()

@app.route('/changePassword', methods=['POST'])
def changePasswordPage():
    return changePassword()

@app.route('/changePlace', methods=['POST'])
def changePlacePage():
    return changePlace()

@app.route('/changeBirthday', methods=['POST'])
def changeBirthdayPage():
    return changeBirthday()

@app.route('/changeName', methods=['POST'])
def changeNamePage():
    return changeName()

@app.route('/checkAdmin', methods=['POST'])
def checkAdminPage():
    return checkAdmin()

@app.route('/addContact', methods=['POST'])
def addContactPage():
    return test()

@app.route('/showContacts', methods=['POST'])
def showContactsPage():
    return showContacts()

@app.route('/changeEmailPage')
def abc4():
    return render_template('changeEmail.html')

@app.route('/getUserInfoPage')
def abc3():
    return render_template('getUserInfo.html')

@app.route('/loginPage')
def abc():
    return render_template('index.html')

@app.route('/registerPage')
def abc2():
    return render_template('register.html')


if __name__ == "__main__":
    app.secret_key = 'webdevbypalacze'
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)