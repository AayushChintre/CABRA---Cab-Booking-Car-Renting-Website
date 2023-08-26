from django.shortcuts import redirect, render
import  mysql.connector as sql
from requests import session
import random
import string

import requests

emailID = ''
passwrd = ''
# Create your views here.

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

t = ('python')

def logoutaction(request):
    del request.session['id']
    return redirect('/')

def loginaction(request):
    global emailID,passwrd,t
    if 'id' in request.session:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            m = sql.connect(host = 'localhost' , user = 'root' , passwd = '',database = 'car-rental')
            cursor = m.cursor()
            d = request.POST
            for key,value in d.items():
                if key == 'email':
                    emailID = value
                elif key == 'password':
                    passwrd = value
            c = "SELECT * FROM admin WHERE email = '{}' AND password = '{}'".format(emailID,passwrd)
            cursor.execute(c)
            print(t)
            t= tuple(cursor.fetchall())
            if t!=():
                random_auth = get_random_string(8)
                request.session['id'] = random_auth
                print('redirected')
                return redirect('/dashboard')
            else:
                print('notredirected')

    return render(request , 'login.html') 