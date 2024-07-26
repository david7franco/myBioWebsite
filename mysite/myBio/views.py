from django.shortcuts import render
from django.shortcuts import render, redirect
from myBio.forms import ContactForm
from django.http import HttpResponse
from .models import Resume


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')





#forms/ credit to https://mailtrap.io/blog/django-contact-form/#:~:text=Start%20by%20creating%20a%20new%20forms.py%20file%20in%20myproject%20folder.&text=Once%20the%20contact%20form%20class,import%20render%2C%20redirect%20from%20myproject.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
   return HttpResponse('Success!')