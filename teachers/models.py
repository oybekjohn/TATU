from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class TeacherInfo(models.Model):
    DARAJA_CHOICES =(
    ("Fan doktori", "Fan doktori"),
    ("Fan nomzodi", "Fan nomzodi"),
    ("Magistr", "Magistr"),
    ("Bakalavr", "Bakalavr"),
    )

    UNVON_CHOICES =(
    ("Professor", "Professor"),
    ("Dotsent", "Dotsent"),
    ("Katta o'qituvchi", "Katta o'qituvchi"),
    ("Asissent", "Asissent"),
    )

    FAKULTET_CHOICES =(
    ("Kompyuter injiniring", "Kompyuter injiniring"),
    ("Telekomunikatsiya injiniring", "Telekomunikatsiya injiniring"),
    )
  
    KAFEDRA_CHOICES =(
    ("Dasturiy injiniring", "Dasturiy injiniring"),
    ("Kompyuter tizimlari", "Kompyuter tizimlari"),
    ("Axborot texnologiyalar", "Axborot texnologiyalar"),
    ("Telekomunikatsiya injiniring", "Telekomunikatsiya injiniring"),
    ("Axborot ta'lim texnologiyalar", "Axborot ta'lim texnologiyalar"),
    ("Axborot xafsizligi", "Axborot xafsizligi"),
    ("Gumanitar fanlar", "Gumanitar fanlar"),
    ("Tabiiy fanlar", "Tabiiy fanlar"),
    ("Tillar va jismoniy ma'daniyat", "Tillar va jismoniy ma'daniyat"),
    )
    
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name= models.CharField(max_length=255)
    informaton = models.TextField(null=True)
    image      = models.ImageField(upload_to=f"images/%{User.first_name}+{User.last_name}", blank=True, null=True)
    
    daraja     = models.CharField(choices=DARAJA_CHOICES, max_length=255)
    unvon      = models.CharField(choices=UNVON_CHOICES, max_length=255)
    fakultet   = models.CharField(choices=FAKULTET_CHOICES, max_length=255)
    kafedra    = models.CharField(choices=KAFEDRA_CHOICES, max_length=255)
    
    xalqaro_maqolalar  = models.FileField(upload_to=f"file/%{User.first_name}+{User.last_name}", blank=False, null=True)
    mahalliy_maqolalar = models.FileField(upload_to=f"file/%{User.first_name}+{User.last_name}", blank=False, null=True)
    guvohnomalar       = models.FileField(upload_to=f"file/%{User.first_name}+{User.last_name}", blank=False, null=True)
    shartnomalar       = models.FileField(upload_to=f"file/%{User.first_name}+{User.last_name}", blank=False, null=True)
    tanlovda_ishtirok  = models.FileField(upload_to=f"file/%{User.first_name}+{User.last_name}", blank=False, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Teacher'

    def __str__(self):
        return self.user.first_name + self.user.last_name
    

class PortfolioInfo(models.Model):
    pass
