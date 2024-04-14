from django import views
from django.shortcuts import redirect, render
import  mysql.connector as sql
import random
import string

m = sql.connect(host = 'localhost' , user = 'root' , passwd = '',database = 'car-rental')
cursor = m.cursor()

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

dirver_name = ''
email = ''
password = ''
car_category = ''
seats = ''

# Create your views here.
def signup_cab(request):
    global dirver_name,email,password,car_category,seats
    request.session['id']=None
    request.session['user_id']=None
    request.session['user_email']=None
    if request.method == 'POST':
        d = request.POST
        for key,value in d.items():
            if key=='dirver_name':
                dirver_name = value
            elif key == 'email':
                email = value
            elif key == 'password':
                password = value
            elif key == 'car_category':
                car_category = value
            elif key == 'seats':
                seats = value
        c = "INSERT INTO  cab_driver (dirver_name,email,password,car_category,seats) VALUES('{}','{}','{}','{}','{}')".format(dirver_name,email,password, car_category, seats)
        random_auth = get_random_string(8)
        request.session['id'] = random_auth
        cursor.execute(c)
        m.commit()
        return redirect('/cab_login')
    return render(request , 'signup_cab.html')


def cab_login(request):
    email=''
    password = ''
    request.session['id']=None
    request.session['user_id']=None
    request.session['user_email']=None
    if request.method == 'POST':
        d = request.POST
        for key,value in d.items():
            if key == 'email':
                email = value
            elif key == 'password':
                password = value
        c = "SELECT * FROM cab_driver WHERE email = '{}' AND password = '{}'".format(email,password)
        cursor.execute(c)
        t= tuple(cursor.fetchall())
        print(t)
        if t!=():
            random_auth = get_random_string(8)
            request.session['id'] = random_auth
            request.session['user_id'] = t[0][0]
            request.session['user_email'] = t[0][2]
            print('redirected')
            return redirect('/cab_dashboard')
        else:
            print('notredirected')

    return render(request , 'Login_cab.html')


def cab_dashboard(request):
    id=request.session.get('user_id')
    k="SELECT COUNT(1) as total_trips FROM cab_booking WHERE cab_id="+str(id)+" and completed_on is not null"
    cursor.execute(k)
    trips= cursor.fetchone()

    c = "SELECT * FROM cab_driver WHERE id = '{}'".format(id)
    cursor.execute(c)
    status= cursor.fetchall()
    if(status[0][6]==0):
        c = "SELECT id, from_location, to_location, DATE_FORMAT(booking_date, '%e %M %Y, %h:%i:%s %p') as booking_on FROM cab_booking WHERE cab_id IS NULL  AND car_type = '{}'".format(status[0][4])
        cursor.execute(c)
        bookings= cursor.fetchall()
        return render(request , 'cab_dashboard.html',{"bookings":bookings,"total_trips":trips[0]})
    else:
        booking_id=status[0][6]
        c = "SELECT id, from_location, to_location, DATE_FORMAT(booking_date, '%e %M %Y, %h:%i:%s %p') as booking_on FROM cab_booking WHERE id = '{}'".format(booking_id)
        cursor.execute(c)
        booking= cursor.fetchone()
        return render(request , 'cab_dashboard.html',{'current_trip':booking,"total_trips":trips[0]})

def accept_cab(request):
    id=request.session.get('user_id')
    booking_id=request.POST['booking_id']
    cursor.execute(""" UPDATE cab_driver SET status = {} WHERE id = {} """.format(booking_id,id))
    m.commit()
    cursor.execute(""" UPDATE cab_booking SET cab_id = {} WHERE id = {} """.format(id,booking_id))
    m.commit()
    return redirect('/cab_dashboard')

def end_trip(request):
    id=request.session.get('user_id')
    booking_id=request.POST['booking_id']
    cursor.execute(""" UPDATE cab_driver SET status = 0 WHERE id = {} """.format(id))
    m.commit()
    cursor.execute(""" UPDATE cab_booking SET completed_on = CURRENT_TIMESTAMP() WHERE id = {} """.format(booking_id))
    m.commit()
    return redirect('/cab_dashboard')

def cab_history(request):
    id=request.session.get('user_id')
    k="SELECT id,from_location,to_location,DATE_FORMAT(booking_date, '%e %M %Y, %h:%i:%s %p') as booking_date, DATE_FORMAT(completed_on, '%e %M %Y, %h:%i:%s %p') as completed_on FROM cab_booking WHERE cab_id="+str(id)
    cursor.execute(k)
    trips= cursor.fetchall()
    return render(request , 'cab_history.html',{'trips':trips})