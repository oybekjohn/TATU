from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

from django.db import models

############################################################

class Daraja(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Daraja'

    def __str__(self):
        return self.title


class Unvon(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Unvon'

    def __str__(self):
        return self.title


class Fakultet(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Fakultet'

    def __str__(self):
        return self.title


class Kafedra(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Kafedra'

    def __str__(self):
        return self.title

# class Oqutuvchilar(models.Model):
#     daraja     = models.ForeignKey(Daraja, on_delete=models.CASCADE, related_name='daraja', blank=True, null=True)
#     unvon     = models.ForeignKey(Unvon, on_delete=models.CASCADE, related_name='unvon', blank=True, null=True)
  
#     class Meta:
#         db_table = 'Oqutuvchilar'

#     def __str__(self):
#         return 'Fan doktori va Professorlar'

############################################################

class XalqaroMaqolalar(models.Model):
    title      = models.CharField(max_length=255)
    file       = models.FileField(upload_to=f"file/xalqaro_maqolalar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Xalqaro Maqolalar'

    def __str__(self):
        return self.title


class MahalliyMaqolalar(models.Model):
    title      = models.CharField(max_length=255)
    file       = models.FileField(upload_to=f"file/mahalliy_maqolalar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Mahalliy Maqolalar'

    def __str__(self):
        return self.title


class Guvohnomalar(models.Model):
    title      = models.CharField(max_length=255)
    file       = models.FileField(upload_to=f"file/guvohnomalar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Guvohnomalar'

    def __str__(self):
        return self.title



class Shartnomalar(models.Model):
    title      = models.CharField(max_length=255)
    file       = models.FileField(upload_to=f"file/shartnomalar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Shartnomalar'

    def __str__(self):
        return self.title


class Tanlovlar(models.Model):
    title      = models.CharField(max_length=255)
    file       = models.FileField(upload_to=f"file/tanlovlar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Tanlovlar'

    def __str__(self):
        return self.title

############################################################


class TeacherData(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    middle_name= models.CharField(max_length=255, null=True)
    informaton = models.TextField(null=True)
    image      = models.ImageField(upload_to=f"images/user", max_length=255, blank=True, null=True)
    
    daraja     = models.ForeignKey(Daraja, on_delete=models.CASCADE, related_name='daraja', blank=True, null=True)
    unvon      = models.ForeignKey(Unvon, on_delete=models.CASCADE, related_name='unvon', blank=True, null=True)
    fakultet   = models.ForeignKey(Fakultet, on_delete=models.CASCADE, related_name='fakultet', blank=True, null=True)
    kafedra    = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name='kafedra', blank=True, null=True)
    
    xalqaro_maqolalar  = models.ForeignKey(XalqaroMaqolalar, on_delete=models.CASCADE, related_name='xalqaro', blank=True, null=True)
    mahalliy_maqolalar = models.ForeignKey(MahalliyMaqolalar, on_delete=models.CASCADE, related_name='mahalliy', blank=True, null=True)
    guvohnomalar       = models.ForeignKey(Guvohnomalar, on_delete=models.CASCADE, related_name='guvohnoma', blank=True, null=True)
    shartnomalar       = models.ForeignKey(Shartnomalar, on_delete=models.CASCADE, related_name='shartnoma', blank=True, null=True)
    tanlovlar          = models.ForeignKey(Tanlovlar, on_delete=models.CASCADE, related_name='tanlov', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '1 Teacher Data'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.middle_name
    