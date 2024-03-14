from django.shortcuts import render, redirect
from .models import Student,Subject,Grade,Table,Employee
from .formstud import studAdd
from .formstud import studAdd, subjAdd
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


def form(request):
    if request.user.is_authenticated:
        context ={
            'student': Student.objects.all()
        }
        return render(request, 'main/form.html', context)
    else:
        return render(request, 'main/auth.html')

def addstud(request):
    if request.method == "POST":
        form = studAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allstud')
    form = studAdd
    context = {
        'form': form
    }
    if request.studAdd.is_authenticated:
        return render(request, 'main/add-stud.html', context)
    else:
        return render(request, 'main/index.html')
