from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addadmissions(request):
    return HttpResponse("<h1>Welcome to School Admission System</h1>")
    #code

def admissionreport(request):
    return HttpResponse("This is admission report")
