from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('/about', views.about, name='about'),
    path('/allstudent', views.stud, name='allstud'),
    path('/allempl', views.empl, name='allempl'),
    path('/subj', views.subj, name='subj'),
    path('/grade', views.grade, name='grade'),
    path('/form', views.form, name='form'),
    path('/addstud', views.addstud, name='addstud'),	
    path('/form', views.form, name='form')
]

