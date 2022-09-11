from django.shortcuts import render, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            list_features = List.objects.all
            messages.success(request, (f'New list "LIST TITLE" has been created.'))
            return render(request, 'home.html', {'list_features': list_features})
            
    else:
        list_features = List.objects.all
        return render(request, 'home.html', {'list_features': list_features})

def about(request):
    name = 'Zuza'
    surname ='Zaremska'
    context = {
        'name': name,
        'surname': surname
        }
    
    return render(request, 'about.html', context)

def list(request, list_id):
    list = List.objects.get(pk=list_id)

    if request.method == 'POST':
        form = ItemForm(request.POST or None)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.list = list
            new_item.save()
            messages.success(request, ('New item has been added!'))

    list_items = list.item_set.all()

    context = {
        'list': list,
        'list_items': list_items,
        'list_id': list_id,
    }

    return render(request, 'list.html', context)

def remove_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk
    item.delete()
    messages.success(request, ('Item has been removed.'))
    
    return redirect(f'/list/{item_list}/')

def cross_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.completed = True
    item.save()
    
    return redirect('home')

def cross_off_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.completed = False
    item.save()
    
    return redirect('home')

def edit_item(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        form = ItemForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been editied.'))
            return redirect('home')
    
    else:
        item = Item.objects.get(pk=item_id)
        return render(request, 'edit_item.html', {'item': item})