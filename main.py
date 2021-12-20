import time
from flask import Flask, render_template, request, url_for, redirect
import json

from werkzeug.utils import redirect


app = Flask(__name__)
password = ""
authenticated_username = False
user_authorized = False
name = ""
password = ""
full_name = ""
@app.route('/home', methods=["POST", "GET"])
def main():
    if authenticated_username:
        return render_template('index.html', full_name=full_name)
    else:
        return render_template('confirm.html')
@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')
@app.route('/loginconfirm', methods=["POST", "GET"])
def confirm():
    try:
        global name
        global password
        name = request.form.get("username")
        password = request.form.get("password")
        print(name)
        users = []
        passwords = []
        names = []
        f = open("data.json" ,)
        data = json.load(f)
        #print(type(data["details"]))
        for x in data["details"]:
            users.append(x["username"])
            passwords.append(x["password"])
            names.append(x["name"])
        print(users)
        if name in users:
            global authenticated_username
            authenticated_username = True
            number = users.index(name)
            print(number)
            if authenticated_username == True and password in passwords:
                password_number = passwords.index(password)
                if password_number == number:
                    user_authorized = True
                    print(user_authorized)
                    global full_name
                    full_name = names[number]
                    print(full_name)
            else:
                        pass
        return redirect('/home')
    except UnboundLocalError:
        return render_template('confirm.html')
@app.route('/uploadwork')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    '''
    work_num = input("Submitted: ")
    work_num_total = 50
    percentage = int(work_num)/int(work_num_total) * 100
    percentage_final = f"{percentage}%"
    print(percentage_final) 
    '''
    app.run(debug=True, port=5000)