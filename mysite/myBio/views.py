from django.shortcuts import render, redirect
from myBio.forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
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
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_body = (
                f"Email from your website:\n\n"
                f"Name of Person: {name}\n"
                f"Message: {message}\n"
                f"Phone number: {phone}"
        )

            try:
                send_mail(
                    subject,
                    email_body,
                    email,
                    ['davidandrewfranco@gmail.com'],
                    fail_silently=False,
                )
                # Return to the same page with a success flag
                return render(request, 'contact.html', {'form': form, 'success': True})
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'contact.html', {'form': form, 'error': 'There was an error sending your message. Please try again.'})
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'success.html')