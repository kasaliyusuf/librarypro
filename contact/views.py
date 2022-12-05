from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactTable
def contact (request):
    return render (request, 'contact.html')

def create_ContactForm(request):
    form = ContactForm()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
          

    context = {
            'form': form
        }
    return render(request, "contact-form.html", context)