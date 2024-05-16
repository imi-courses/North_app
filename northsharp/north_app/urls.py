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

    path('<int:pk>/editsubj', views.editsubj, name='editsubj'),
    path('<int:pk>/deletesubj', views.deletesubj, name='deletesubj'),

    path('<int:pk>/editstud', views.editstud, name='editstud'),
    path('<int:pk>/deletestud', views.deletestud, name='deletestud'),

    path('<int:pk>/editEmpl', views.editEmpl, name='editEmpl'),
    path('<int:pk>/deleteEmpl', views.deleteEmpl, name='deleteEmpl'),

    path('/form', views.form, name='form'),
    path('/addgrade', views.addGrade, name='addgrade'),
    path('/logout', views.user_logout, name='logout'),
    path('/addempl', views.addEmpl, name='addempl')

]

