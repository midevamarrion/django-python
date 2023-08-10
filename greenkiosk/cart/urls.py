from django.urls import path
from .views import product_upload_view
from.import views

urlpatterns= [
    path("products/get/", product_upload_view,
       name="product_get_view"),

    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/edit/<int:cart_item_id>/', views.edit_cart_item, name='edit_cart_item'),
    path('cart/', views.cart_list, name='cart_list'),
]