from django.urls import path
from .views import contact, create_ContactForm

urlpatterns = [
		path('contact/', contact, name='contact'),
		path('contact/form', create_ContactForm, name='contactform'),
]
