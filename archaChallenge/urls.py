from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('me/', views.meView),
    path('card/', views.cardView),
     path('card/changeLimit/', views.changeLimit)
]