from django.urls import path
from . import views

urlpatterns = [
    path('/new',views.ZooUserForm, name = 'zoo_user_form')
]