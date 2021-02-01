from django.urls import path
from . import views

app_name = "standard"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addClass, name="add")
]
