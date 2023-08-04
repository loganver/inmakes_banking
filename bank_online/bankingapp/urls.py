from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('get_branches/', views.get_branches, name='get_branches'),

]