from django import forms
from django.shortcuts import render

class AddInstitute(forms.Form):
    institute = forms.CharField(label="Add institute")


# Create your views here.
schools = ["foo" , "zoo", "boo"]
inst_name = "Play field"
def index(request):
    return render(request, "institute/index.html", {
        "inst_name":inst_name.capitalize(),
        "schools" :schools
        })

def add(request):
    return render(request, "institute/add.html", {
        "form":AddInstitute()
    })
