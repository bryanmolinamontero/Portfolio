# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


from django.shortcuts import render

def handler404(request):
    return render(request,'404.html')