from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
from . import models

def base(request):
    return render(request,'base.html')
    
def homepage(request):
    places = models.places.objects.all()

    return render(request,'home.html',{"places":places})

def addpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']

        models.places.objects.create(name=name, price=price)
        return redirect(reverse('places:home'))
    else:
        return render(request, 'add.html')

def deletepage(request):
    if request.method == 'POST':
        id = request.POST['id']

        o1 = models.places.objects.filter(pk=id)
        if len(o1) == 0:
            print ("not found")
        else:
            o1[0].delete()
        print(o1)
        return redirect(reverse('places:home'))
    else:
        return render(request, 'delete.html')

