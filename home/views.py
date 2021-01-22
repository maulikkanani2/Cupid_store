# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

# Redirect to logout page
def logoutWarning(request):
    if request.method == 'POST':
        logout(request)
        return redirect('account_login')
    return render(request, 'allauth/account/logout.html')
    
# Logout user function
def logoutUser(request):
    logout(request)
    return redirect('account_login')
