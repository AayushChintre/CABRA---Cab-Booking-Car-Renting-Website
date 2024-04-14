import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests import request
import  mysql.connector as sql


m = sql.connect(host = 'localhost' , user = 'root' , passwd = '',database = 'car-rental')
cursor = m.cursor()

# Create your views here.
def dashboard(request):
    cursor.execute(""" SELECT * FROM driver""")
    driver_data = cursor.fetchall()
    cursor.execute(""" SELECT * FROM car_catergory""")
    cat_data = cursor.fetchall()
    cursor.execute(""" SELECT * FROM car""")
    car_data = cursor.fetchall()
    cursor.execute(""" SELECT * FROM fair_tb""")
    fair_data = cursor.fetchall()
    print(cat_data)
    cursor.execute(""" SELECT count(*) FROM driver """)
    driver_countt = cursor.fetchall()
    driver_counttt = list(sum(driver_countt, ()))
    driver_count = ''.join(map(str,driver_counttt))
    cursor.execute(""" SELECT count(*) FROM car_catergory """)
    cat_countt = cursor.fetchall()
    cat_counttt = list(sum(cat_countt, ()))
    cat_count = ''.join(map(str,cat_counttt))
    return render( request, 'dashboard.html', {'drivers':driver_data,'driver_count' : driver_count,'cat_count' : cat_count, 'car_catergory':cat_data,'car':car_data ,'fair_data':fair_data})


def drivercreate(request):
    return render(request ,'driverAdd.html' )

def driveraddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        dname = request.POST['drivername']
        demail = request.POST['driveremail']
        dgneder = request.POST['drivergender']
        dnumber = request.POST['drivernumber']
        cursor.execute(""" INSERT INTO `driver` (`id`,`name`,`email`,`gender`,`mobile`,`created_at`,`updated_at`) VALUES (NULL,'{}','{}','{}','{}',NULL,NULL) """.format(dname,demail,dgneder,dnumber))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)


def driverdelete(request, id):
    print(id)
    cursor.execute("""DELETE FROM driver WHERE id = {}""".format(id)) 
    m.commit()
    return redirect(dashboard)


def driveredit(request ,id):
    print(id)
    cursor.execute("""SELECT * FROM driver where id = '{}'""".format(id))
    data = cursor.fetchone()                                                                 
    #return list(data)
    print(list(data))
    return render(request, 'driveredit.html', {'drivers': data})


def driverupdate(request,id):
    if request.method == 'POST':
        print(request.POST)
        dname = request.POST['drivername']
        demail = request.POST['driveremail']
        dgneder = request.POST['drivergender']
        dnumber = request.POST['drivernumber']
        cursor.execute(""" UPDATE driver SET name = %s,email = %s,gender = %s,mobile = %s  WHERE id = %s """,(dname,demail,dgneder,dnumber,id))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)



# category CRUD
def catcreate(request):
    return render(request ,'catAdd.html' )

def cataddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['catname']
        cursor.execute(""" INSERT INTO `car_catergory` (`id`,`name`) VALUES (NULL,'{}') """.format(cname))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)

def catdelete(request, id):
    print(id)
    cursor.execute("""DELETE FROM car_catergory WHERE id = {}""".format(id)) 
    m.commit()
    return redirect(dashboard)



def catedit(request ,id):
    print(id)
    cursor.execute("""SELECT * FROM car_catergory where id = '{}'""".format(id))
    data = cursor.fetchone()                                                                 
    #return list(data)
    print(list(data))
    return render(request, 'catEdit.html', {'car_catergory':data})


def catupdate(request,id):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['catname']
        cursor.execute(""" UPDATE car_catergory SET name = %s  WHERE id = %s """,(cname,id))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)



# car CRUD
def carcreate(request):
    cursor.execute(""" SELECT * FROM driver""")
    driver_data = cursor.fetchall()
    cursor.execute(""" SELECT * FROM car_catergory""")
    cat_data = cursor.fetchall()
    return render(request ,'carAdd.html', {'driver_data': driver_data,'cat_data':cat_data} )

def caraddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['carname']
        cdriver = request.POST['driver']
        cno = request.POST['carno']
        allocated_status = request.POST['allocated_status']
        cid = request.POST['catergoryid']
        cimage = request.POST['cimage']
        cursor.execute(""" INSERT INTO `car` (`id`,`car_name`,`driver_id`,`vehicle_no`,`allocated_status`,`cat_id`,`car_image`) VALUES (NULL,'{}','{}','{}','{}','{}','{}') """.format(cname,cdriver,cno,allocated_status,cid,cimage))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)

def cardelete(request, id):
    print(id)
    cursor.execute("""DELETE FROM car WHERE id = {}""".format(id)) 
    m.commit()
    return redirect(dashboard)



def caredit(request ,id):
    cursor.execute(""" SELECT * FROM driver""")
    driver_data = cursor.fetchall()
    cursor.execute(""" SELECT * FROM car_catergory""")
    cat_data = cursor.fetchall()
    print(id)
    cursor.execute("""SELECT * FROM car where id = '{}'""".format(id))
    data = cursor.fetchone()                                                                 
    #return list(data)
    print(list(data))
    return render(request, 'carEdit.html', {'car_data':data,'driver_data': driver_data,'cat_data':cat_data})


def carupdate(request,id):
    if request.method == 'POST':
        print(request.POST)
        cname = request.POST['carname']
        cdriver = request.POST['driver']
        cno = request.POST['carno']
        allocated_status = request.POST['allocated_status']
        cid = request.POST['catergoryid']
        cimage = request.POST['cimage']
        cursor.execute(""" UPDATE car SET car_name = %s , driver_id = %s , vehicle_no = %s , allocated_status = %s , cat_id = %s , car_image = %s WHERE id = %s """,(cname,cdriver,cno,allocated_status,cid,cimage,id))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)




# fair CRUD
def faircreate(request):

    cursor.execute(""" SELECT * FROM car_catergory""")
    cat_data = cursor.fetchall()
    return render(request ,'fairAdd.html', {'cat_data':cat_data} )

def fairaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        perKm = request.POST['perKm']
        basic_charge = request.POST['basic_charge']
        cid = request.POST['catergoryid']
        cursor.execute(""" INSERT INTO `fair_tb` (`id`,`cat_type`,`per_km`,`basic_charge`) VALUES (NULL,'{}','{}','{}') """.format(cid,perKm,basic_charge))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)

def fairdelete(request, id):
    print(id)
    cursor.execute("""DELETE FROM fair_tb WHERE id = {}""".format(id)) 
    m.commit()
    return redirect(dashboard)



def fairedit(request ,id):

    cursor.execute(""" SELECT * FROM car_catergory""")
    cat_data = cursor.fetchall()
    print(id)
    cursor.execute("""SELECT * FROM fair_tb where id = '{}'""".format(id))
    data = cursor.fetchone()                                                                 
    #return list(data)
    print(list(data))
    return render(request, 'fairEdit.html', {'fair_data':data,'cat_data':cat_data})


def fairupdate(request,id):
    if request.method == 'POST':
        print(request.POST)
        perKm = request.POST['perKm']
        basic_charge = request.POST['basic_charge']
        cid = request.POST['catergoryid']
        cursor.execute(""" UPDATE fair_tb SET cat_type = %s , per_km = %s , basic_charge = %s  WHERE id = %s """,(cid,perKm,basic_charge,id))
        m.commit()
        return redirect(dashboard)
    else:
        return redirect(drivercreate)

