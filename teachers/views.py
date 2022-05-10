import random

from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import (
    Daraja,
    Unvon,
    Fakultet,
    Kafedra,
    TeacherFile,
    TeacherData,
)
from .forms import TeacherFileForm, TeacherDataForm

kaferda = Kafedra.objects.all()
daraja = Daraja.objects.all()
unvon = Unvon.objects.all()
fakultet = Fakultet.objects.all()


def index(request):
    # active_teacher = TeacherFile.objects.all()

    domlalar = TeacherData.objects.all()[:9]

    teacher = TeacherData.objects.all()
    random_teacher = random.choice(list(teacher))
    teacher_number = teacher.count()
    teacher_number_professor = TeacherData.objects.filter(unvon_id=1).count()
    teacher_number_big = TeacherData.objects.filter(unvon_id=3).count()
    maqola_number = (
        TeacherFile.objects.filter(type=1).count()
        + TeacherFile.objects.filter(type=2).count()
    )
    guvohnoma_number = TeacherFile.objects.filter(type=3).count()
    shartnomalar_number = TeacherFile.objects.filter(type=4).count()

    oneteacher_maqola = TeacherFile.objects.filter(type=1).count()
    oneteacher_guvohnoma = TeacherFile.objects.filter(type=3).count()
    oneteacher_shartnoma = TeacherFile.objects.filter(type=4).count()

    indikator_salohiyat = int(teacher_number_professor / teacher_number * 100)
    indikator_maqola = int(oneteacher_maqola / teacher_number * 100)
    indikator_guvohnoma = int(oneteacher_guvohnoma / teacher_number * 100)
    indikator_shartnoma = int(oneteacher_shartnoma / teacher_number * 100)

    context = {
        "teacher": teacher,
        "active_domlalar": domlalar,
        "random_teacher": random_teacher,
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "teacher_number": teacher_number,
        "teacher_number_professor": teacher_number_professor,
        "teacher_number_big": teacher_number_big,
        "maqola_number": maqola_number,
        "guvohnoma_number": guvohnoma_number,
        "shartnomalar_number": shartnomalar_number,
        "indikator_salohiyat": indikator_salohiyat,
        "indikator_maqola": indikator_maqola,
        "indikator_guvohnoma": indikator_guvohnoma,
        "indikator_shartnoma": indikator_shartnoma,
    }
    return render(request, "index.html", context)


def batafsil(request, pk):
    random_teacher = TeacherData.objects.get(pk=pk)
    random_teacher_maqola = TeacherFile.objects.filter(teacher_id=random_teacher)

    xalqaro_maqola_number = TeacherFile.objects.filter(
        type=1, teacher_id=random_teacher
    ).count()
    mahalliy_maqola_number = TeacherFile.objects.filter(
        type=2, teacher_id=random_teacher
    ).count()
    shartnoma_number = TeacherFile.objects.filter(
        type=4, teacher_id=random_teacher
    ).count()
    guvohnoma_number = TeacherFile.objects.filter(
        type=3, teacher_id=random_teacher
    ).count()
    tanlov_number = TeacherFile.objects.filter(
        type=5, teacher_id=random_teacher
    ).count()

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "random_teacher": random_teacher,
        "random_teacher_maqola": random_teacher_maqola,
        "xalqaro_maqola_number": xalqaro_maqola_number,
        "mahalliy_maqola_number": mahalliy_maqola_number,
        "shartnoma_number": shartnoma_number,
        "guvohnoma_number": guvohnoma_number,
        "tanlov_number": tanlov_number,
    }
    return render(request, "batafsil.html", context)


def faculty(request, pk):
    Teacher = TeacherData.objects.all()
    faculty_d = Kafedra.objects.get(id=pk)

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "teacher": Teacher,
        "faculty": faculty_d,
    }
    return render(request, "faculty.html", context)


def daraja_page(request, pk):
    Teacher = TeacherData.objects.all()
    faculty_d = Daraja.objects.get(id=pk)

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "teacher": Teacher,
        "faculty": faculty_d,
    }
    return render(request, "daraja_page.html", context)


def unvon_page(request, pk):
    Teacher = TeacherData.objects.all()
    faculty_d = Unvon.objects.get(id=pk)

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "teacher": Teacher,
        "faculty": faculty_d,
    }
    return render(request, "unvon_page.html", context)


def oqituvchilar_page(request):
    Teacher = TeacherData.objects.filter(Q(unvon=3) | Q(unvon=4))

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "teacher": Teacher,
    }
    return render(request, "oqituvchilar_page.html", context)


@login_required
def account(request):
    user_data = TeacherData.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form = TeacherDataForm(request.POST, request.FILES, instance=user_data)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = TeacherDataForm(request.POST or None, instance=user_data)

    current_user = request.user.id
    teacherfile = TeacherFile.objects.filter(teacher_id=user_data)

    context = {
        "user_data": user_data,
        "teacherfile": teacherfile,
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "form": form,
    }
    return render(request, "account.html", context)


#####################  FUll  ######################
@login_required
def account_form(request):
    if request.method == "POST":
        form = TeacherFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            teacher = TeacherData.objects.get(user_id=request.user.id)
            form.teacher_id = teacher
            form.save()
            return redirect("account")
    else:
        form = TeacherFileForm()
    choice = TeacherFile.objects.all()

    context = {
        "kafedralar": kaferda,
        "unvonlar": unvon,
        "darajalar": daraja,
        "choice": choice,
        "form": form,
    }
    return render(request, "form.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("account")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("account")
            return render(
                request,
                "registration/login.html",
            )
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


# file = form.save(commit=False)
#             TeacherFile.teacher_id = request.user
#             file.save()
