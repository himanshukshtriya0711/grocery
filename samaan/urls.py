from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("grocery/",views.grocery,name ="grocery"),
    path("add_greocery/",views.add_grocery,name = "add_grocery"),
    path("delete_grocery/<int:grocery_id>",views.delete_grocery,name = "delete_grocery"),
    path("update_grocery/<int:grocery_id>",views.update_grocery,name = "update_grocery"),
    path("remove_grovery/<int:grocery_id>",views.remove_grocery,name = "remove_grocery")
    
]