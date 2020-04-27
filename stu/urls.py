from django.urls import path


from . import views

urlpatterns = [
    path('', views.index_register),
    path('login/', views.login_view),
    path('show/', views.show_view),
]