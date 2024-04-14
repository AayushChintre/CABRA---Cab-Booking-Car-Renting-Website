"""carrentalsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from playground import views
from cab_driver import views as cab_driver
from signup.views import signaction
from login.views import loginaction


urlpatterns = [
    path('dashboard', views.hello_response, name='home'),
    path('logout/',views.logout,name="logout"),
    path('', loginaction, name='login'),
    path('signup', signaction, name='signup'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('countinuebooking', views.countinuebooking, name='countinuebooking'),
    path('payment/<int:id>', views.payment , name='payment'),
    path('doneBooking/<int:id>', views.doneBooking , name='donebooking'),
    path('bookinghistory', views.bookingHistory , name='bookinghistory'),
    path('book_cab', views.book_cab , name='book_cab'),
    path('booking', views.booking , name='booking'),
    path('signup_cab', cab_driver.signup_cab , name='signup_cab'),
    path('cab_login', cab_driver.cab_login , name='cab_login'),
    path('cab_dashboard', cab_driver.cab_dashboard , name='cab_dashboard'),
    path('cab_history', cab_driver.cab_history , name='cab_history'),
    path('accept_cab', cab_driver.accept_cab , name='accept_cab'),
    path('end_trip', cab_driver.end_trip , name='end_trip'),
    path('admin/', admin.site.urls)
]
