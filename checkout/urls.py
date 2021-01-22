from django.urls import path
from . import views
# add checkout and Stripepayment oper url
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('stripepayment',views.stripeOpen,name="stripe_payment")
]