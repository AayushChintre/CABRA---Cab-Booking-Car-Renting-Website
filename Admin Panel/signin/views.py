from django import views
from django.shortcuts import redirect, render
import  mysql.connector as sql
import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


user = ''
emailID = ''
passwrd = ''

# Create your views here.
def signaction(request):
    global user,emailID,passwrd
    if 'id' in request.session:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            m = sql.connect(host = 'localhost' , user = 'root' , passwd = '',database = 'car-rental')
            cursor = m.cursor()
            d = request.POST
            for key,value in d.items():
                if key=='username':
                    user = value
                elif key == 'email':
                    emailID = value
                elif key == 'password':
                    passwrd = value
            c = "INSERT INTO  admin (name,email,password) VALUES('{}','{}','{}')".format(user,emailID,passwrd)
            random_auth = get_random_string(8)
            request.session['id'] = random_auth
            cursor.execute(c)
            m.commit()
            return redirect('/')

    return render(request , 'signin.html')