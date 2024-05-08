from django.shortcuts import render, redirect
from .models import Student,Subject,Grade,Table,Employee
from .formstud import studAdd, subjAdd, gradeAdd, emplAdd,subjEdit, subjDelete
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

# /Редактирование и удаление
def editstud(request, pk):
    if request.method == "POST":
        form = Student.objects.get(pk = pk)
        form.name = request.POST['name']
        form.class_name = request.POST['class_name']
        form.save()
        return redirect('allstud')
    form = studAdd
    context = {
        'form': form
    }
    return render(request, 'main/editstud.html', context)

def deletestud(request, pk):
    if request.method == "POST":
        Student.objects.filter(pk = pk).delete()
        return redirect('allstud')
    form = studAdd
    context = {
        'form': form
    }
    return render(request, 'main/deletestud.html', context)
# /



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

# /Редактирование и удаление
def editsubj(request, pk):
    if request.method == "POST":
        form = Subject.objects.get(pk = pk)
        form.name = request.POST['name']
        form.save()
        return redirect('subj')
    form = subjEdit
    context = {
        'form': form
    }
    return render(request, 'main/editsubj.html', context)

def deletesubj(request, pk):
    if request.method == "POST":
        Subject.objects.filter(pk = pk).delete()
        return redirect('subj')
    form = subjDelete
    context = {
        'form': form
    }
    return render(request, 'main/deletesubj.html', context)
# /


def addGrade(request):
    form = gradeAdd()
    if request.method == 'POST':
        form = gradeAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade')
    return render(request, 'main/addgrade.html', {'form': form})

def addEmpl(request):
    form = emplAdd()
    if request.method == 'POST':
        form = emplAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allempl')
    return render(request, 'main/addempl.html', {'form': form})
# /Редактирование и удаление
def editEmpl(request, pk):
    if request.method == "POST":

        form = emplAdd.objects.get(pk = pk)
        form.name = request.POST['name']
        form.position = request.POST['position']
        form.sex = request.POST['sex']
        form.experience = request.POST['experience']
        form.birth_day = request.POST['birth_day']
        form.Class_teacher = request.POST['Class_teacher']
        form.subject = request.POST['subject']

        form.save()
        return redirect('allempl')
    form = emplAdd
    context = {
        'form': form
    }
    return render(request, 'main/editEmpl.html', context)

def deleteEmpl(request, pk):
    if request.method == "POST":
        Employee.objects.filter(pk = pk).delete()
        return redirect('allempl')
    form = emplAdd
    context = {
        'form': form
    }
    return render(request, 'main/deleteEmpl.html', context)
# /