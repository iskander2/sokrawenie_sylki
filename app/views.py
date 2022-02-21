from django.shortcuts import render, redirect
from .serializers import UrlSerializer, UrlCreatSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Url
from django.shortcuts import get_object_or_404 
from .forms import UrlForm
from django.conf import settings 
# Create your views here.

class UrlListView(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlCreatView(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlCreatSerializer

def redirect_1(request, cut_url):
    url = get_object_or_404(Url,cut_url=cut_url)
    return redirect(url.origin_url)

def ololo(request):
    form = UrlForm(request.POST or None )
    urls = Url.objects.all()
    if request.method == 'POST' and form.is_valid():
        form.save()
        
    return render (request,'ololo.html',{'form':form, 'urls':urls, 'site_url': settings.SITE_URL  })

def search(request):
    query = request.GET.get('q')
    urls = Url.objects.filter(origin_url__icontains=query)
    form = UrlForm()
    return render (request,'ololo.html',{'form':form, 'urls':urls, 'site_url': settings.SITE_URL  })








