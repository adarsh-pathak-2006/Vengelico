from django.shortcuts import get_object_or_404, render, redirect
from .models import products, contact as Contact

SHIPPING_AMOUNT = 12
TAX_RATE = 0.06

def get_cart_data(request):
    cart = request.session.get("cart", {})
    cart_items = []
    subtotal = 0

    for product_id, quantity in cart.items():
        product = products.objects.filter(id=product_id).first()

        if product:
            item_total = product.price * quantity
            subtotal += item_total
            cart_items.append({
                "product": product,
                "quantity": quantity,
                "total": item_total,
            })

    shipping = SHIPPING_AMOUNT if cart_items else 0
    tax = round(subtotal * TAX_RATE, 2) if cart_items else 0
    total = subtotal + shipping + tax

    return {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }

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
    return render(request, "cart.html", get_cart_data(request))

def add_to_cart(request, product_id):
    if request.method == "POST":
        get_object_or_404(products, id=product_id)
        cart = request.session.get("cart", {})
        product_key = str(product_id)
        cart[product_key] = cart.get(product_key, 0) + 1
        request.session["cart"] = cart
        request.session.modified = True

    return redirect("shop")

def update_cart(request, product_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        product_key = str(product_id)
        action = request.POST.get("action")

        if product_key in cart:
            if action == "increase":
                cart[product_key] += 1
            elif action == "decrease":
                cart[product_key] -= 1

            if cart.get(product_key, 0) <= 0:
                cart.pop(product_key, None)

            request.session["cart"] = cart
            request.session.modified = True

    return redirect("cart")

def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        cart.pop(str(product_id), None)
        request.session["cart"] = cart
        request.session.modified = True

    return redirect("cart")

    
