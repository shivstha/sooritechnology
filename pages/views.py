from django.shortcuts import render


def homepage(request):
    return render(request, "base.html")


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    return render(request, 'contact.html')


def productpage(request):
    return render(request, 'products.html')


def servicepage(request):
    return render(request, 'services.html')


def wacompage(request):
    return render(request, 'wacom.html')


def zebrapage(request):
    return render(request, 'zebra.html')


def supermapage(request):
    return render(request, 'superma.html')
