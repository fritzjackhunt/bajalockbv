from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'bajalock/index.html')

def company(request):
    return render(request, 'bajalock/company.html')

def operations(request):
    return render(request, 'bajalock/operations.html')

def sustainability(request):
    return render(request, 'bajalock/sustainability.html')

def products(request):
    return render(request, 'bajalock/products.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['essiet.aniekan@yahoo.com'],
            fail_silently = False,
        )


        return render(request, 'bajalock/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'bajalock/contact.html')