# interface/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def dersler(request):
    return render(request, 'interface/dersler.html')


def galeri(request):
    return render(request, 'interface/galeri.html')

def hocalar(request):
    return render(request, 'interface/hocalar.html')

def iletisim(request):
    return render(request, 'interface/iletisim.html')

def index(request):
    return render(request, 'interface/index.html')
def uyeolmak(request):
    if request.method == 'POST':
        # Handle form submission for POST requests
        admin_isim = request.POST.get('isim')
        admin_password = request.POST.get('password')

        # Check if admin credentials are valid
        user = authenticate(username=admin_isim, password=admin_password)
        if user is not None:
            # User authentication successful, log the user in
            login(request, user)
            # Redirect to 'index' page if credentials are valid
            return redirect('index')
        else:
            # Add an error message for invalid credentials if needed
            # For example:
            # error_message = "Invalid admin credentials. Please try again."
            # return render(request, 'interface/uyeolmak.html', {'error_message': error_message})

            # For simplicity, let's return the same template for invalid credentials
            return render(request, 'interface/uyeolmak.html')

    # Render the 'uyeolmak.html' template for GET requests
    return render(request, 'interface/uyeolmak.html')

