"""carrentaladmin URL Configuration

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
from django.urls import path
from dashboard.views import caraddprocess, carcreate, cardelete, caredit, carupdate, cataddprocess, catcreate, catdelete, catedit, catupdate, dashboard, driveraddprocess, drivercreate, driverdelete, driveredit, driverupdate, fairaddprocess, faircreate, fairdelete, fairedit, fairupdate
from login.views import loginaction,logoutaction

from signin.views import signaction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', signaction , name='signin'),
    path('dashboard', dashboard , name='dashboard'),
    # ====== driver CRUD ============
    path('drivercreate', drivercreate , name='drivercreate'),
    path('driver/inserted/', driveraddprocess , name='drivercreate'),
    path('driver/delete/<int:id>', driverdelete , name='driverdelete'),
    path('driver/edit/<int:id>', driveredit , name='driveredit'),
    path('driver/update/<int:id>', driverupdate , name='driverupdate'),
    # ====== car category CRUD ============
    path('catcreate', catcreate , name='catcreate'),
    path('cat/inserted/', cataddprocess , name='catcreate'),
    path('catergory/delete/<int:id>', catdelete , name='catdelete'),
    path('catergory/edit/<int:id>', catedit , name='catedit'),
    path('cat/update/<int:id>', catupdate , name='catupdate'),
    # ====== car  CRUD ============
    path('carcreate', carcreate , name='carcreate'),
    path('car/inserted/', caraddprocess , name='carcreate'),
    path('car/delete/<int:id>', cardelete , name='cardelete'),
    path('car/edit/<int:id>', caredit , name='caredit'),
    path('car/update/<int:id>', carupdate , name='carupdate'),
    # ====== fair  CRUD ============
    path('faircreate', faircreate , name='faircreate'),
    path('fair/inserted/', fairaddprocess , name='faircreate'),
    path('fair/delete/<int:id>', fairdelete , name='fairdelete'),
    path('fair/edit/<int:id>', fairedit , name='fairedit'),
    path('fair/update/<int:id>', fairupdate , name='fairupdate'),

    path('', loginaction , name='login'),
    path('logout', logoutaction , name='login'),
]
