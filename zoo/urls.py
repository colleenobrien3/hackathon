from django.urls import path
from . import views

urlpatterns = [
    path('',views.zoo_home, name = 'zoo_home'),
    path('new/',views.zoo_user_create, name = 'zoo_user_create')
]