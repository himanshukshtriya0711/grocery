from django.shortcuts import render,redirect
from .models import Grocery
#=========================home======================
def home(request):
    return render (request,"home.html")
#============================grocery======
def grocery(request):
    Grocerys = Grocery.objects.filter(remove = False)
    parameter = {
        "grocerys" : Grocerys
    }

    return render(request,"grocery.html",parameter)

#====================add_grocery=====================
def add_grocery(request):
    if request.method=="POST":
        user_item = request.POST.get("item")
        user_quantity  = request.POST.get("quantity")
        new_user = Grocery(
            item = user_item,
            quantity = user_quantity

        )
        new_user.save()
        return redirect("grocery")
    return render(request,"add_grocery.html")

#===================delete================================

def delete_grocery(request,grocery_id):
    grocery = Grocery.objects.get(id = grocery_id)
    grocery.delete()
    return redirect("grocery")


#================================update_grocery=================

def update_grocery(request,grocery_id):
    grocery = Grocery.objects.get(id = grocery_id)
    if request.method == "POST":
        new_item = request.POST.get("new_item")
        new_quantity = request.POST.get("new_quantity")

        grocery.item = new_item
        grocery.quantity = new_quantity
        grocery.save()
        return redirect("grocery")
        

    parameter = {
            'grocery' : grocery
        }

        

    return render(request,"update_grocery.html",parameter)

#=========================complete===================

def remove_grocery(request,grocery_id):
    grocery = Grocery.objects.get(id = grocery_id)
    grocery.remove = True
    grocery.save()
    return redirect("grocery")