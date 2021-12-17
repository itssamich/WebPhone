from . import views
from django.urls import path

app_name = 'spotify'

urlpatterns = [
    path('', views.index, name='index'),
]