from django.contrib import admin
from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html',{'home':'active'})
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Portfolio website regarding  : '+ subject
        message_body = 'Name : ' + name + '.   Email : ' + email + '.   Phone : ' + phone + '.    Message : ' + message

       #print(name,email,subject,phone,message)
       
        send_mail(
            email_subject,
            message_body,
            
            settings.EMAIL_HOST_USER, 
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )
        return HttpResponseRedirect('/contact')  

    return render(request,'myapp/contact.html',{'contact':'active'})