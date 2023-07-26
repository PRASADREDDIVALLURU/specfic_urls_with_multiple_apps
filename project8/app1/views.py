from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v11(request):
    return render(request,"v11.html")
def v12(request):
    return render(request,"v12.html")
def v13(request):
    return render(request,"v13.html")
def v14(request):
    return HttpResponse("view14 in string")