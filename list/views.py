from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect

from list.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})