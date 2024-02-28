from django.shortcuts import render
from .models import Student,Subject,Grade,Table,Employee

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about-us.html")


def stud(request):
    Students = Student.objects.all()
    return render(request, "main/allstudent.html",{'student': Students})
def empl(request):
    empl = Employee.objects.all()
    return render(request, "main/allempl.html",{'empl': empl})
def subj(request):
    subj = Subject.objects.all()
    return render(request, "main/subj.html",{'subj': subj})
def grade(request):
    grade = Grade.objects.all()
    return render(request, "main/grade.html",{'grade': grade})