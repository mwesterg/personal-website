from django.shortcuts import render

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')



def utils(request):
    """ view function for a mix of utilities"""

    return render(request,'utils.html')

def projects(request):
    """ view functions for projects page """

    return render(request,'contru.html')
    
def other(request):
    """ view functions for "other" page """

    return render(request,'contru.html')

def contact(request):
    """ view functions for "other" page """

    return render(request,'contru.html')

def about(request):
    """ view functions for "other" page """

    return render(request,'contru.html')