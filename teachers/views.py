import random

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import (
                    Daraja,
                    Unvon, 
                    Fakultet, 
                    Kafedra,
                    FileType,
                    TeacherFile,         
                    TeacherData,                    
                    )
from .forms import TeacherFileForm, TeacherDataForm



kaferda = Kafedra.objects.all()

def index(request):
    Teacher        = TeacherData.objects.all()
    random_teacher = random.choice(list(Teacher))

    # teacher_number           = TeacherData.objects.count()
    # teacher_number_professor = Unvon.objects.filter(title="Professor").count()
    # teacher_number_big       = Unvon.objects.filter(title="Katta o'qituvchi").count()

    # maqola_number       = TeacherFile.objects.count() + TeacherFile.objects.count()
    # guvohnoma_number    = FileType.objects.filter(title='Guvohnomalar').count()
    # shartnomalar_number = TeacherFile.objects.count()

    teacher_number           = 75
    teacher_number_professor = 50
    teacher_number_big       = 25

    maqola_number       = 101
    guvohnoma_number    = 10
    shartnomalar_number = 20

    context = {
        'teacher':             Teacher,
        'random_teacher':      random_teacher,
        'kafedralar':          kaferda,
        'teacher_number':      teacher_number,
        'teacher_number_professor': teacher_number_professor,
        'teacher_number_big':  teacher_number_big,
        'maqola_number':       maqola_number,
        'guvohnoma_number':    guvohnoma_number,
        'shartnomalar_number': shartnomalar_number
    }
    return render(request, 'index.html', context)


def batafsil(request, pk):
    random_teacher = TeacherData.objects.get(pk=pk)
    context = {
        'kafedralar': kaferda,
        'random_teacher': random_teacher,
    }
    return render(request, 'batafsil.html',context)




def faculty(request, pk):
    Teacher = TeacherData.objects.all()
    context = {
        'kafedralar': kaferda,
        'teacher': Teacher,
    }

    return render(request, 'faculty.html', context)




@login_required
def account(request):
    user_data = TeacherData.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form=TeacherDataForm(request.POST, request.FILES, instance=user_data)
        if form.is_valid():
            # form      = form.save(commit=False)
            # teacher = TeacherData.objects.get(user_id=request.user.id)
            # form.user_id = teacher.id
            form.save()
            return redirect('account')
    else:
        form = TeacherDataForm(request.POST or None, instance=user_data)

    teacherfile = TeacherFile.objects.all()
    context = {
        'user_data' : user_data,
        'teacherfile': teacherfile,
        'kafedralar': kaferda,
        'form'      : form,
    }
    return render(request, 'account.html', context)
    







#####################  FUll  ######################
@login_required
def account_form(request):
    if request.method== "POST":
        form=TeacherFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            teacher = TeacherData.objects.get(user_id=request.user.id)
            form.teacher_id = teacher
            form.save()
            return redirect('account')
    else:
        form = TeacherFileForm()

    choice = TeacherFile.objects.all()
    context = {
        'kafedralar': kaferda,
        'choice': choice,
        'form': form,
    }
    return render(request, 'form.html', context)




def login_view(request):
    if request.user.is_authenticated:
        return redirect('account')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account')
            return render(request, 'registration/login.html',)
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})





















# file = form.save(commit=False)
#             TeacherFile.teacher_id = request.user
#             file.save()