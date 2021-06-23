from django.contrib import admin
from .models import (
                    Daraja, XalqaroMaqolalar,
                    Unvon, MahalliyMaqolalar,
                    Fakultet, Guvohnomalar,
                    Kafedra, Shartnomalar,
                    TeacherData, Tanlovlar,                    
                    )


admin.site.register(Daraja)
admin.site.register(Unvon)
admin.site.register(Fakultet)
admin.site.register(Kafedra)

admin.site.register(XalqaroMaqolalar)
admin.site.register(MahalliyMaqolalar)
admin.site.register(Guvohnomalar)
admin.site.register(Shartnomalar)
admin.site.register(Tanlovlar)

admin.site.register(TeacherData)
