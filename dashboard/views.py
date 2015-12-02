from django.shortcuts import render_to_response
from django.shortcuts import render


# Create your views here.
def home(request):
    return render_to_response('dashboard/index.html')


def about(request):
    return render(request, 'dashboard/about-us.html')


def services(request):
    return render(request, 'dashboard/services.html')


def demos(request):
    return render(request, 'dashboard/demos.html')


def contact(request):
    return render(request, 'dashboard/contact.html')


def manuals(request):
    return render(request, 'dashboard/manuals.html')


def publications(request):
    return render(request, 'dashboard/publications.html')
