import pandas as pd
from django.shortcuts import render, redirect
from .models import Student,Subject,Grade,Table,Employee
from .formstud import studAdd, subjAdd, gradeAdd, emplAdd,subjEdit, subjDelete
from django.http import HttpResponse
from openpyxl.workbook import Workbook


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

def report(request):
    grade_data = Grade.objects.all()
    data = {
        'Имя': [grade.student for grade in grade_data],
        'Предмет': [grade.subject for grade in grade_data],
        'Класс': [grade.student.class_name for grade in grade_data],
        'Оценка': [grade.grade for grade in grade_data]
    }

    df = pd.DataFrame(data)

    file_path = 'grade.xlsx'
    df.to_excel(file_path, index=False)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="grade.xlsx"'
    return response
# /
# def report(request):
#     if request.method == "POST":
#         student_data = Student.objects.values('name', 'class_name')
#         subjects_data = Subject.objects.all()
#         grades_data = Grade.objects.select_related('student', 'subject').all()
#
#         students = []
#         subjects = []
#         grades = []
#
#         for student in student_data:
#             students.append(student['name'])
#         for subject in subjects_data:
#             subjects.append(subject.name)
#         for grade in grades_data:
#             grades.append(grade.grade)
#
#         data = {'Student': students, 'Subject': subjects, 'Grade': grades}
#         df = pd.DataFrame(data)
#
#         file_path = 'grades_data.xlsx'
#         df.to_excel(file_path, index=False)
#
#         return render(request, 'repost.html', file_path)