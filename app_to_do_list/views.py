from django.shortcuts import render, redirect
from .models import List, Item, Subitem
from .forms import ListForm, ItemForm, SubitemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    list_features = List.objects.all()
    
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            new_list = form.save(commit=False)
            list_title = new_list.list_title
            new_list.save()
            messages.success(request, (f'New list "{list_title}" has been created.'))
    
    return render(request, 'home.html', {'list_features': list_features,})

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
    list_items = list.list_items.all()
    
    all_subitems = Subitem.objects.all()
    list_items_subitems = []

    for subitem in all_subitems:
        if subitem.item in list_items:
            list_items_subitems.append(subitem)

    if request.method == 'POST':
        item_form = ItemForm(request.POST or None)

        if item_form.is_valid():
            new_item = item_form.save(commit=False)

            new_item.list = list
            new_item.save()

            messages.success(request, ('New item has been added!'))
 
    context = {
        'list': list,
        'list_items': list_items,
        'list_id': list_id,
        'list_items_subitems': list_items_subitems,
    }

    return render(request, 'list.html', context)

def create_subitem(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk
    
    if request.method == 'POST':
        subitem_form = SubitemForm(request.POST or None)
    
        if subitem_form.is_valid():
            new_subitem = subitem_form.save(commit=False)

            new_subitem.item = item
            new_subitem.save()

            messages.success(request, (f'New subitem has been added to item "{item}"!'))
            return redirect(f'/list/{item_list}/')
    else:
        subitem_form = SubitemForm()
    
    return render(request, 'create_subitem.html', {'subitem_form': subitem_form, 'item': item,})

def remove_list(request, list_id):
    list = List.objects.get(pk=list_id)
    list.delete()
    messages.success(request, ('List has been removed.'))
    
    return redirect('home')

def edit_list(request, list_id):
    list = List.objects.get(pk=list_id)

    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=list)

        if form.is_valid():
            form.save()
            messages.success(request, ('List has been editied.'))
            return redirect(f'home')
    
    else:
        return render(request, 'edit_list.html', {'list': list})

def remove_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk
    item.delete()
    messages.success(request, ('Item has been removed.'))
    
    return redirect(f'/list/{item_list}/')

def cross_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk
    item.item_completed = True
    item.save()
    
    return redirect(f'/list/{item_list}/')

def cross_off_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk
    item.item_completed = False
    item.save()
    
    return redirect(f'/list/{item_list}/')

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item_list = item.list.pk

    if request.method == 'POST':
        form = ItemForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been editied.'))
            return redirect(f'/list/{item_list}/')
    
    else:
        return render(request, 'edit_item.html', {'item': item})