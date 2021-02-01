from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms


standards =  ["1" , "2" , "3"]

class NewStandardForm(forms.Form):
    standard =  forms.CharField(label="Add New Class")
# Create your views here.
def index(request):
    #return HttpResponse(" All the Class and Divisions will be listed here")
    if "standards" not in request.session:
        request.session["standards"] = []
    return render(request, "standard/index.html" , {
    "standards" : request.session["standards"]
    })

def addClass(request):
    if request.method == "POST":
        form  = NewStandardForm(request.POST)
        if form.is_valid():
            standard = form.cleaned_data["standard"]
            #standards.append(standard)
            request.session["standards"] += [standard]
            return HttpResponseRedirect(reverse("standard:index"))
        else:
            return render(request, "standard/add.html", {
            "form" : form
            })
    return render(request, "standard/add.html", {
    "form" : NewStandardForm()
    })
