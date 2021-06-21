from django.urls import path
from .views import index, account, faculty, login

urlpatterns = [ 
    path('', index),
    path('account/', account),
    path('faculty/', faculty),
    path('login/', login),
]