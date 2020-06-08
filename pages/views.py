from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail


def homepage(request):
    return render(request, "base.html")


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_subject = form.cleaned_data['subject']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail(sender_subject, message, sender_email, ['shiva.shres1998@gmail.com'])
            return HttpResponse('<h1>Thank you for contacting us!!!</h1>')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def productpage(request):
    return render(request, 'products.html')


def servicepage(request):
    return render(request, 'services.html')


def wacompage(request):
    return render(request, 'wacom.html')


def zebrapage(request):
    return render(request, 'zebra.html')


def supermapage(request):
    return render(request, 'suprema.html')
