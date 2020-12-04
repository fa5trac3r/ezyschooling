from django.urls import path,include
from .views import ( PizzaList, PizzaDetail, ToppingList, SizeList)

urlpatterns = [
    # pizza urls
    path('',PizzaList.as_view()),
    path('<int:pk>',PizzaDetail.as_view()),
    # topping url
    path('toppings',ToppingList.as_view()),
    # size url
    path('sizes', SizeList.as_view()),
]