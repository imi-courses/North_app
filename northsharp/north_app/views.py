from django.shortcuts import render, redirect
from .models import Student,Subject,Grade,Table,Employee
from .formstud import studAdd, subjAdd, gradeAdd, emplAdd,subjEdit, subjDelete
# Create your views here.


def search(request, models):
    if request.POST.get('name'):
        return models.objects.filter(name__icontains = request.POST['name'])
    else:
        return models.objects.all()


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about-us.html")


def stud(request):
    Students = search(request, Student)
    return render(request, "main/allstudent.html",{'student': Students})
def empl(request):
    empl = search(request, Employee)
    return render(request, "main/allempl.html",{'empl': empl})
def subj(request):
    subj = Subject.objects.all()
    return render(request, "main/subj.html",{'subj': subj})
def grade(request):
    grade = Grade.objects.all()
    grade.union(Student.objects.all())
    print(grade)
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