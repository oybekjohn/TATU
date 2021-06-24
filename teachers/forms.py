from django.db.models import fields
from django.forms import ModelForm
from .models import TeacherData, TeacherFile


class TeacherFileForm(ModelForm):
    
    class Meta:
        model  = TeacherFile
        fields = ['title', 'file', 'type',]



class TeacherDataForm(ModelForm):

    class Meta:
        model = TeacherData
        fields = ['image', 'daraja', 'unvon', 'fakultet', 'kafedra',]