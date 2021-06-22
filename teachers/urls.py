from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.index, name='index'),
    path('batafsil/', views.batafsil, name='batafsil'),
    path('faculty/', views.faculty, name='faculty'),
    path('account/', views.account, name='account'),
    path("login/", views.login_view, name="login"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)