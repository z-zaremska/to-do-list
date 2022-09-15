from django.db import models

class List(models.Model):
    list_title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)    
    #list_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_title

class Item(models.Model):
    list = models.ForeignKey(List, related_name="list_items", on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return (self.item + f" ({self.list.list_title})")

class Subitem(Item):
    parent_item = models.ForeignKey(Item, related_name="item_subitems", on_delete=models.CASCADE) 

    def __str__(self):
        return (self.item + f" ({self.parent_item}")

