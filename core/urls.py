from django.urls import path
from core.views import home, profile_view,cart_view

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile_view, name='profile'),
    path('cart/', cart_view, name='cart'), 
]
