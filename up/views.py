from django.shortcuts import render, get_list_or_404
from .models import fileUp,something

# Create your views here.
def pic(request):
    context= get_list_or_404(fileUp)
    return render(request,'html.html',locals())
    
    
def som(request):
    context=get_list_or_404(something)
    return render(request,'html.html',locals())