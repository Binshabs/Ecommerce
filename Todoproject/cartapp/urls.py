from django.urls import path
from .import views
app_name='cartapp'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('removecart/<int:id>',views.removecart,name='removecart'),
    path('fullremove/<int:id>',views.fullremove,name='fullremove'),
    
    
    
    path('displaycart/',views.displaycart,name='displaycart'),
]