from django.contrib import admin
from .models import List, Item, Subitem

admin.site.register(List),
admin.site.register(Item),
admin.site.register(Subitem),
