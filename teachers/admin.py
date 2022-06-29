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


class DarajaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

class UnvonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


class FakultetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', )


class KafedraAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', )


class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class TeacherFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

class TeacherDataAdmin(admin.ModelAdmin):
    list_display = ('user__user__first_name', 'middle_name', 'created_at')
    # search_fields = ('teacher__first_name', 'teacher__last_name')



admin.site.register(Daraja, DarajaAdmin)
admin.site.register(Unvon, UnvonAdmin)
admin.site.register(Fakultet, FakultetAdmin)
admin.site.register(Kafedra, KafedraAdmin)
admin.site.register(FileType, FileTypeAdmin)
admin.site.register(TeacherFile, TeacherFileAdmin)
admin.site.register(TeacherData)
