from django.shortcuts import render

def home(req):
    return render(req, 'core/home.html')

def profile_view(req):
    return render(req, 'core/profile.html')

def cart_view(request):
    return render(request, 'core/cart.html') 
