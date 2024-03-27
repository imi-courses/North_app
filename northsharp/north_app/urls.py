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
    path('/addsubj', views.addsubj, name='addsubj'),
    path('/form', views.form, name='form'),
    path('/addgrade', views.addGrade, name='addgrade'),
    path('/addempl', views.addEmpl, name='addempl')
]

