from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def  demo(request):
    # name = 'india'
    return render(request, 'index.html')




# Create your views here.
