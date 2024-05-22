from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Student,Subject,Grade,Table,Employee
from .formstud import studAdd, subjAdd, gradeAdd, emplAdd,subjEdit, subjDelete
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'id': 'username', 'name': 'username', 'class': 'field'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'id': 'password', 'name': 'password', 'class': 'field'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'check'}), label='Запомнить меня')

def set_session_data(req, model):
    req.session['username'] = req.POST['username']
    ar = model.objects.get(username__icontains=req.POST['username'])
    req.session['user_role'] = ar.role


# Извлечение данных из сеанса
def get_session_data(req):
    username = req.session.get('username')
    user_role = req.session.get('user_role')
    return [username, user_role]

def auth_stud(req, model):
    if req.POST.get('username'):
        try:
            ar = model.objects.get(username__icontains=req.POST['username'])
            return ar.password == req.POST['password']
        except model.DoesNotExist:
            return False
    return False

def search(request, models):
    if request.POST.get('name'):
        return models.objects.filter(name__icontains = request.POST['name'])
    else:
        return models.objects.all()

def index(request):
    return render(request, "main/index.html",{'user_role' : get_session_data(request)[1]})

def about(request):
    return render(request, "main/about-us.html",{'user_role' : get_session_data(request)[1]})

def user_logout(request):
    logout(request)
    return redirect('form')
@login_required
def stud(request):
    Students = search(request, Student)
    return render(request, "main/allstudent.html",{'student': Students,'user_role' : get_session_data(request)[1]})
@login_required
def empl(request):
    empl = search(request, Employee)
    return render(request, "main/allempl.html",{'empl': empl,'user_role' : get_session_data(request)[1]})
@login_required
def subj(request):
    subj = Subject.objects.all()
    return render(request, "main/subj.html",{'subj': subj,'user_role' : get_session_data(request)[1]})
@login_required
def grade(request):
    if request.session['user_role'] == "student":
        grade = Grade.objects.filter(student__username=request.session['username'])
    else:
        grade = Grade.objects.all()
    return render(request, "main/grade.html",{'grade': grade, 'user_role' : get_session_data(request)[1]})



def form(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid() and auth_stud(request, Student):
            set_session_data(request, Student)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if username is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('about')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'main/form.html', {'form': form, 'error': 'Invalid login credentials.'})
    else:
        form = UserLoginForm()
    return render(request, 'main/form.html', {'form': form})

def addstud(request):
    if(type==1):
        return redirect('grade')
    else:
        if request.method == "POST":
            form = studAdd(request.POST)
            if form.is_valid():
                user_stud = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user_stud.save()
                form.save()
                return redirect('allstud')
        form = studAdd
        context = {
            'form': form
        }
        return render(request, 'main/add-stud.html', context)

# /Редактирование и удаление
@login_required
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
@login_required
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
            user_stud = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user_stud.save()
            form.save()
            return redirect('main')
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