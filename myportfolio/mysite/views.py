from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
def homePage(request):
    return render(request,'mysite/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        subject = request.POST.get("subject","")
        message = request.POST.get("message","")
        infos = Contact(name=name, email=email, subject=subject, message=message)
        infos.save()
    return render(request,'mysite/index.html')
