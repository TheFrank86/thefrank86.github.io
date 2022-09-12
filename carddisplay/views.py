from django.shortcuts import render
from .models import *
from django.core.management import call_command




# Create your views here.
def index(request):

         # reset object data for each search
        card.objects.all().delete()

        return render(request, "carddisplay/index.html", {
            "carddisplay": card.objects.all()
        })



def result(request):
    if request.method == "POST":
 
        # update object data based on set selected
        setselect = request.POST["setselect"]

        call_command('updatemodels', select=setselect)

        return render(request, "carddisplay/result.html", {
            "carddisplay": card.objects.all()
        })