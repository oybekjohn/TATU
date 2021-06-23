import random

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

from .models import (
                    Daraja, XalqaroMaqolalar,
                    Unvon, MahalliyMaqolalar,
                    Fakultet, Guvohnomalar,
                    Kafedra, Shartnomalar,
                    TeacherData, Tanlovlar,                    
                    )


def index(request):
    Teacher        = TeacherData.objects.all()
    rand_num       = random.randint(0, TeacherData.objects.count()-2)
    random_teacher = TeacherData.objects.get(pk=2)
    kaferda        = Kafedra.objects.all()

    teacher_number           = TeacherData.objects.count()
    teacher_number_professor = Unvon.objects.filter(title="Professor").count()
    teacher_number_big       = Unvon.objects.filter(title="Katta o'qituvchi").count()

    maqola_number       = XalqaroMaqolalar.objects.count() + MahalliyMaqolalar.objects.count()
    guvohnoma_number    = Guvohnomalar.objects.count()
    shartnomalar_number = Shartnomalar.objects.count()

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
        'random_teacher': random_teacher
    }
    return render(request, 'batafsil.html',context)



def faculty(request, pk):
    kaferda = Kafedra.objects.all()
    Teacher = TeacherData.objects.all()
    context = {
        'kafedralar': kaferda,
        'teacher': Teacher,
    }

    return render(request, 'faculty.html', context)




@login_required
def account(request):
    user_data = TeacherData.objects.get(user_id=request.user.id)
    kaferda = Kafedra.objects.all()
    context = {
        'user_data': user_data,
        'kafedralar': kaferda,
    }
    return render(request, 'account.html', context)
    

@login_required
def account_form(request):
    return render(request, 'form.html',)


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
