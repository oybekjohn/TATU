from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("batafsil/<int:pk>/", views.batafsil, name="batafsil"),
    path("faculty/<int:pk>/", views.faculty, name="faculty"),
    path("daraja/<int:pk>/", views.daraja_page, name="daraja"),
    path("unvon/<int:pk>/", views.unvon_page, name="unvon"),
    path("oqituvchilar/", views.oqituvchilar_page, name="oqituvchilar"),
    path("account/", views.account, name="account"),
    path("account/form/", views.account_form, name="account_form"),
    path("login/", views.login_view, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
