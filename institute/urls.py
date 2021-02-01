from django.urls import path
from . import views

app_name = "institute"
urlpatterns = [
        path("add", views.add, name='add'),
        path("", views.index, name='index')

    ]
