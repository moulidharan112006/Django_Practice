from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is my home page (/)")
    context = {'name': 'mouli', 'course': 'Django'}
    return render(request, 'home.html',context)

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')

def project(request):
    # return HttpResponse("This is my project page (/project)")
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name,phone,email,desc)
        ins = Contact(name = name, email = email, phone = phone, desc = desc)
        ins.save()
        print("the data has been return to the db")

    # return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')