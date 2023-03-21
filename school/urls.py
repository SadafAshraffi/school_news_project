from django.urls import path
from school import views


app_name = 'school'

urlpatterns = [
path('', views.index, name='index'),
]
