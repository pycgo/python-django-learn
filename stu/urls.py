from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index_register),
    path('login/', views.login_view),
]