from django.shortcuts import render, HttpResponse, reverse, redirect
from django.template.context_processors import request

from teacher.models import Teacher, Otp
from user_messages.models import Message
from django.utils.crypto import get_random_string
from random import randint
import smtplib, ssl

def home(request):
    if request.method == 'POST':
        print('Email: ', request.POST['email'])
        text = 'Your email address sent!.'
        return HttpResponse(f'<h1><a href="">{text}</a></h1>')
    page = 'home'
    teachers = Teacher.objects.filter(is_active=True)
    count = len(Message.unreads.all())

    return render(request, 'index.html', {'teachers': teachers, 'count': count, 'page': page})

def contact(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('verify_email')
        if email:
            Otp.objects.filter(email=email).delete()
            code = randint(100, 999)

            token = get_random_string(length=32)
            Otp.objects.create(email=email, code=code, token=token)

            Server = 'smtp.gmail.com'
            Port = 465

            sender_email = "shahvandi2010@gmail.com"
            app_password = "qscl xtmj lcnd ujxl"
            # receiver_email = ["kiani_un@yahoo.com", "shahvandi2010@gmail.com"]
            receiver_email = email

            # code = randint(100, 999)
            message = f'Wellcome\nYour code is: {code}'
            # message = "hello world\n Good Luck"

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(Server, Port, context=context) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, message)
                print(f'Email Sent!\nCode: {code}')

            return redirect(reverse('check') + f'?token={token}')
        else:
            print('Email: ', request.POST['email'])
            text = 'Your email address sent!.'
        return HttpResponse(f'<h1><a href="{home}">{text}</a></h1>')
    page = 'contact'
    count = len(Message.unreads.all())
    return render(request, 'contact.html', {'count': count, 'page': page})

def check_otp(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    home = reverse('home')
    if request.method == 'POST':
        token = request.GET.get('token')
        code = request.POST['code']
        otp = Otp.objects.filter(code=code, token=token)
        if otp:
            Message.objects.create(name=request.POST['name'], email=otp[0].email, subject=request.POST['subject'], message=request.POST['message'])
            text = 'OK, Your message sent!'
            otp.delete()
            return HttpResponse(f'<h1><a href="{home}">{text}</a></h1>')
        text = 'Code is wrong!'
        return HttpResponse(f'<h1><a href="">{text}</a></h1>')
        # form.add_error('__all__', 'Invalid Code')
        # return render(request, 'check.html')
    # form = CheckOtpForm()
    return render(request, 'check.html')