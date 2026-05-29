from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('submit/', views.submit, name='submit'),
    path('cart/', views.cart, name="cart"),
    path('cart/add/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/update/<int:product_id>/', views.update_cart, name="update_cart"),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name="remove_from_cart"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
