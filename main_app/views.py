from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm
from django.core.mail import send_mail, mail_admins
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Messages
def add_message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.save()
            # message = loader.render_to_string(
            #     'emails/admin1.html',
            #     {
            #         'name': new_message.name,
            #         'phone_number': new_message.phone,
            #         'email': new_message.email,
            #         'message': new_message.message,
            #         'date_created': new_message.date_created,
            #     }
            # )
            return render(request, 'messages/success.html')
    else:
        form = MessageForm()
        context = { 'form' : form }
        return render(request, 'messages/new.html', context)

def message_success(request):
    return render(request, 'messages/success.html')