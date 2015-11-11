from django.shortcuts import render_to_response
from django.shortcuts import render


# Create your views here.
def home(request):
    return render_to_response('dashboard/index.html')
