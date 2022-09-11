from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('New item has been added!'))
            return render(request, 'home.html', {'all_items': all_items})
    
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    name = 'Zuza'
    surname ='Zaremska'
    context = {'name': name, 'surname': surname}
    
    return render(request, 'about.html', context)

def remove(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been removed.'))
    
    return redirect('home')

def cross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    
    return redirect('home')

def edit_item(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been editied.'))
            return redirect('home')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit_item.html', {'item': item})