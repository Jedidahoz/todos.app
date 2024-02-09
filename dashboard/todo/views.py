from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    selecteddata = todos.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        description = request.POST['description']
        saveData = todos(title=title, details=details, description=description)
        try:
            saveData.save()
            return render(request,'home.html', {'message':'data inserted','data':selecteddata})
        except:
            return render(request, 'home.html', {'message':'data does not inserted'})
    return render(request, 'home.html', {'data':selecteddata})
def deletetodos(request, id):
    selecteddata = todos.objects.all()
    deletetodos = todos.objects.get(id=id).delete()
    return render(request, 'home.html', {'data':selecteddata})
def updatetodos(request,id):
    selecteddata = todos.objects.get(id=id)
    if request.method == 'POST':
        selecteddata.title = request.POST['title']
        selecteddata.title = request.POST['details']
        selecteddata.title = request.POST['description']
        try:
            selecteddata.save()
            return render(request,'home.html', {'message':'data updated successfull','updatedata':selecteddata})
        except:
            return render(request, 'home.html', {'message':'data does not update'})
    return render(request, 'home.html', {'updatetodos':selecteddata})
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')