from django.shortcuts import render


def homepage(request):
    return render(request, "base_test.html")


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    return render(request, 'contact.html')


def productpage(request):
    return render(request, 'products.html')


def servicepage(request):
    return render(request, 'services.html')
