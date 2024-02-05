from django.urls import path
from . import views
app_name='cartapp'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('displaycart/',views.displaycart,name='displaycart'),
]