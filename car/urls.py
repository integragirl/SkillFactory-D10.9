from car.views import CarRead
from django.urls import path

app_name = 'car'
urlpatterns = [
    path('',                    CarRead.as_view(),         name='car_list'),
    path('search/',             CarRead.as_view(),         name='car_list_search'),
    #path('<int:pk>',            CarDetail.as_view(),       name='car-detail'),
]