from django.shortcuts import render, HttpResponse, reverse
from teacher.models import Teacher
from user_messages.models import Message


def home(request):
    page = 'home'
    teachers = Teacher.objects.filter(is_active=True)
    count = len(Message.unreads.all())

    # for m in Message.unreads.all():
    #     m.unread=False
    #     m.save()

    return render(request, 'index.html', {'teachers': teachers, 'count': count, 'page': page})

def contact(request):
    page = 'contact'
    if request.method == 'POST':
        name = request.POST.get('name')
        home = reverse('home')
        if name:
            Message.objects.create(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], message=request.POST['message'])
            text = 'OK, Your message sent!'
        else:
            print('Email: ', request.POST['email'])
            text = 'Your email address sent!.'
        return HttpResponse(f'<h1><a href="{ home }">{ text }</a></h1>')
    count = len(Message.unreads.all())
    return render(request, 'contact.html', {'count': count, 'page': page})
