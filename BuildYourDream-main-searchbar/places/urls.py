from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.homepage,name='home'),
    path('add',views.addpage,name='add'),
    path('delete',views.deletepage,name='delete'),
]