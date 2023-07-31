from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
import random
from .helper import MessageHandler
import time
from django.utils import timezone




def home(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        return HttpResponse(" verified.")
    else:
        return HttpResponse(" Not verified.")

def register(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        user=User.objects.create(username=request.POST['user_name'])
        otp=random.randint(1000,9999)
        profile=Profile.objects.create(user=user,phone_number=request.POST['phone_number'],otp=f'{otp}')

        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_whatsapp()
        else:
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()

        red=redirect(f'otp/{profile.uid}/')
        red.set_cookie("can_otp_enter",True,max_age=30)
        return red  
    return render(request, 'register.html')






def otpVerify(request,uid):
    if request.method=="POST":
        profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"otp.html",{'id':uid})





