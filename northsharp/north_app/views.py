from django.shortcuts import render, redirect
from .formstud import studAdd, subjAdd, subjEdit
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
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/form.html')

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
    return render(request, 'main/add-stud.html', context)
def addsubj(request):
    if request.method == "POST":
        form = subjAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subj')
    form = subjAdd
    context = {
        'form': form
    }
    return render(request, 'main/addsubj.html', context)

def editsubj(request,pk):
    EditSubj = Subject.objects.get(pk=pk)
    if request.method == "POST":
        form = subjEdit(request.POST, instance = EditSubj)
        if form.is_valid():
            form.save()
            return redirect('subj')
    else:
        form = subjEdit(instance = EditSubj)
        return render(request, 'main/editsubj.html', {'form': form})
