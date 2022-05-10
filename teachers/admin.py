from django.contrib import admin
from .models import (
    Daraja,
    Unvon,
    Fakultet,
    Kafedra,
    FileType,
    TeacherFile,
    TeacherData,
)


admin.site.register(Daraja)
admin.site.register(Unvon)
admin.site.register(Fakultet)
admin.site.register(Kafedra)

admin.site.register(FileType)

admin.site.register(TeacherFile)

admin.site.register(TeacherData)
