from django.shortcuts import render, redirect
from myBio.forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')





#forms/ credit to https://mailtrap.io/blog/django-contact-form/#:~:text=Start%20by%20creating%20a%20new%20forms.py%20file%20in%20myproject%20folder.&text=Once%20the%20contact%20form%20class,import%20render%2C%20redirect%20from%20myproject.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'Contact form submission from {name}',
                message,
                email,
                ['davidandrewfranco@gmail.com'],
                fail_silently=False,
            )
            
            # Optionally, redirect to a success page or display a success message
            return render(request, 'contact.html', {'form': form, 'success': success})
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
def success(request):
   return HttpResponse('Success!')