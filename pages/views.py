from django.shortcuts import render,redirect
from .models import products, contact as Contact

def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def shop(request):
    product=products.objects.all()
    return render(request, "shop.html", {'products':product})
def submit(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
    return redirect("contact")

def cart(request):
    return render(request, "cart.html")