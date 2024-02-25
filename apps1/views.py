from django.shortcuts import render
from .models import travel
# Create your views here.
def link1(request):

    tt = travel.objects.all()
    return render(request,'index.html',{'tt':tt})
