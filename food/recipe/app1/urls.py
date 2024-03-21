from django.urls import path
from . import views

urlpatterns = [
    path('',views.front, name ='front'),
    path('home',views.home, name ='home'),
    path('south',views.south,name ='south'),
    path('north',views.north,name ='north'),
    path('tribal',views.tribal,name ='tribal'),
    path('desserts',views.desserts,name ='desserts'),
    path('recipes',views.recipes,name = 'recipes'),
    path('login',views.login,name ='login'),
]

