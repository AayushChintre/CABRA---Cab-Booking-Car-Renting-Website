import imp
from operator import index
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
import  mysql.connector as sql
# Create your views here.
m = sql.connect(host = 'localhost' , user = 'root' , passwd = '',database = 'car-rental')
cursor = m.cursor()

def logout(request):
    request.session.pop('id')
    return redirect('/')

def hello_response(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        cursor.execute(""" SELECT * FROM car_catergory""")
        cat_data = cursor.fetchall()
        cursor.execute(""" SELECT * FROM location""")
        loc_data = cursor.fetchall()
        return render(request,'index.html', {'cartype':cat_data , 'loc_data' : loc_data})

def countinuebooking(request):
    cartype = request.POST['cartype']
    to_location = request.POST['to_location']
    from_location = request.POST['from_location']
    pick_date = request.POST['pick-up-date']
    drop_date = request.POST['drop-of-date']
    request.session['pick_date'] = pick_date
    request.session['drop_date'] = drop_date
    cursor.execute(""" SELECT * FROM car WHERE cat_id = '{}' """.format(cartype))
    filtered_cars = cursor.fetchall()
    cursor.execute(""" SELECT name FROM car_catergory WHERE id = '{}' """.format(cartype))
    car_type_name = cursor.fetchall()
    car_type_namee = list(sum(car_type_name, ()))
    car_type_nameee = ''.join(map(str,car_type_namee))
    cursor.execute(""" SELECT count(*) FROM car WHERE cat_id = '{}' AND allocated_status = 'no' """.format(cartype))
    count_filtered_cars = cursor.fetchall()
    count_filtered_carss = list(sum(count_filtered_cars, ()))
    count_filtered_carsss = ''.join(map(str,count_filtered_carss))
    
    cursor.execute("""select c.id, c.car_name, c.vehicle_no, c.car_image, cc.name, d.name, d.mobile from car as c join fair_tb as f on c.cat_id = f.cat_type join driver as d on c.driver_id = d.Id JOIN car_catergory as cc on c.cat_id = cc.id WHERE c.cat_id = '{}' AND allocated_status = 'no' """.format(cartype))
    all_card_info = cursor.fetchall()
    # print(all_card_info)
    return render(request , 'vehicle.html', {'count_cars':count_filtered_carsss ,'car_type':car_type_nameee,'card_info':all_card_info, 'from_location':from_location, 'to_location':to_location})

def login(request):
    return render(request , 'Login.html')

def signup(request):
    return render(request , 'signup.html')

def vehicle(request):
    cursor.execute(""" SELECT c.id, c.car_name, c.vehicle_no, c.car_image, cc.name, d.name, d.mobile FROM car c LEFT JOIN car_catergory as cc on c.cat_id = cc.id LEFT JOIN driver d on d.Id=c.driver_id WHERE 1=1 and c.allocated_status='no' """)
    cat_iid = cursor.fetchall()
    # print(cat_iid)
    return render(request , 'vehicle.html',{'count_cars':len(cat_iid),'card_info':cat_iid})

def payment(request,id):
    cursor.execute(""" SELECT cat_id FROM car WHERE id = '{}' """.format(id))
    cat_iid = cursor.fetchall()
    cat_iidd = list(sum(cat_iid, ()))
    cat_iiidd = ''.join(map(str,cat_iidd))
    cursor.execute(""" SELECT basic_charge FROM fair_tb WHERE cat_type = '{}' """.format(cat_iiidd))
    fair_price = cursor.fetchall()
    fair_pricee = list(sum(fair_price, ()))
    fair_priceee = ''.join(map(str,fair_pricee))
    return render(request , 'payment.html' , {'fair_price':fair_priceee,'car_id':id})


def doneBooking(request , id):
    pickDate = request.session.get('pick_date')
    dropDate = request.session.get('drop_date')
    carID = id
    cusId = request.session.get('user_id')
    cursor.execute(""" INSERT INTO `bookings` (`id`,`to_booking_date`,`from_booking_date`,`car_id`,`cus_id`) VALUES (NULL, '{}', '{}', '{}', '{}')  """.format(pickDate,dropDate,carID,cusId))
    m.commit()
    cursor.execute(""" UPDATE car SET allocated_status = 'yes' WHERE id = '{}' """.format(carID))
    m.commit()
    return render(request , 'congo.html')


def bookingHistory(request):
    cusID = request.session.get('user_id')
    cursor.execute(""" SELECT * FROM `bookings` as b JOIN users as u on b.cus_id = u.id JOIN car as c on b.car_id = c.id JOIN car_catergory as cc on c.cat_id = cc.id WHERE b.cus_id = '{}'; """.format(cusID))
    history = cursor.fetchall()
    # print(history)
    return render(request , 'bookings.html', {'history':history})


def book_cab(request):
    id=request.session.get('user_id')
    k="SELECT id,from_location,to_location,DATE_FORMAT(booking_date, '%e %M %Y, %h:%i:%s %p') as booking_date, DATE_FORMAT(completed_on, '%e %M %Y, %h:%i:%s %p') as completed_on, car_type FROM cab_booking WHERE user_id="+str(id)
    cursor.execute(k)
    trips= cursor.fetchall()
    return render(request , 'book_cab.html',{'history':trips})

def booking(request):
    id=request.session.get('user_id')
    from_location=request.POST['from_location']
    to_location=request.POST['to_location']
    car_type=request.POST['car_type']
    cursor.execute(""" INSERT INTO `cab_booking` (`user_id`,`from_location`,`to_location`,`booking_date`,`car_type`) VALUES ({}, '{}', '{}', CURRENT_TIMESTAMP(), '{}')  """.format(id,from_location,to_location,car_type))
    m.commit()
    return redirect('/book_cab')