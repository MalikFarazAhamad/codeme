from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 
def python(request):
    return render(request, 'python.html')
def ruby(request):
    return render(request,'ruby.html') 
def css(request):
    return render(request, 'css.html')
def boost(request):
    return render(request,'boost.html')
def java(request):
    return render(request,'java.html') 
def web(request):
    return render(request,'web.html')
def c(request):
    return render(request,'c.html')  
def cpp(request):
    return render(request,'cpp.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 