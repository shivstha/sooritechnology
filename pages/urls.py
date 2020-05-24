from django.urls import path
from .views import homepage, aboutpage, contactpage, productpage, servicepage

urlpatterns = [
    path('', homepage, name='home'),
    path('about_us/', aboutpage, name='about'),
    path('contact_us/', contactpage, name='contact'),
    path('products/', productpage, name='product'),
    path('services/', servicepage, name='service'),
]