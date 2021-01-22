from django.shortcuts import render

# Create your views here.


#add Checkout Function
def checkout(request):
    return render(request, 'checkout/checkout.html')