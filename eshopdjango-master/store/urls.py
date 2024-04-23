from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.home import CreateProductLIST,UpdateProductLIST,CreateCustomerList,UpdateCustomerList,CreateOrderList,UpdateOrderList



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),



    #**********API's **********************************************

    # For Products
    path('api/product',CreateProductLIST.as_view(),name = 'product'),
    path('api/product/<int:pk>',UpdateProductLIST.as_view(),name = 'update product'),

    # For Customer
    path('api/customer',CreateCustomerList.as_view(),name = 'customer'),
    path('api/customer/<int:pk>',UpdateCustomerList.as_view(),name = 'update customer'),

    # For Order
    path('api/order',CreateOrderList.as_view(),name = 'customer'),
    path('api/order/<int:pk>',UpdateOrderList.as_view(),name = 'update customer')

]   