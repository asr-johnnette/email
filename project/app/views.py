from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import random
def random_num():
    val=random.randrange(1111,9999)
    return val

val=random_num()

class Login(View):
    def get(self,request):
        return render(request,"login.html")
    
    def post(self, request):
        name=request.POST.get("name")
        age=request.POST.get("age")
        email=request.POST.get("email")
        send_mail(
        
        "Subject here",
        f"Here is the otp {val}.",
        "akash638959@gmail.com",
        [email],
        fail_silently=False,
        )
        print("------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   Email send")

        request.session['user_email'] = email
        request.session['user_name']= name
        return redirect('otp')

        # return render(request, 'otp_verification.html')
        


class Otpverification(View):
    def get(self,request):
        return render(request,'otp_verification.html')

    def post(self,request):
            if request.method == 'POST':
                my_input_value = request.POST.get('otp')
                user_name=request.session.get('user_name')
                user_email=request.session.get('user_email')
                print("--------------------->>>>>>>>>>>>>>>>>>> ",my_input_value,val)
                if int(my_input_value) == val:
                    User(username=user_name,email=user_email).save()
                    return HttpResponse(f'The Otp is {my_input_value}')
                else:
                    return HttpResponse("not verified")