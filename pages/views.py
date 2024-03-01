from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'pages/about_me.html')



def experience(request):
    return render(request, 'pages/experience.html')

def contact_view(request):

    #if user click send email button
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
        #get the data
        #send the email
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail("Message from " + name, message, email_from, ['eric.wells41@gmail.com'])

            return redirect('home')

    
        #if not
        else:
            print("The message can not be sent")
    
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})


