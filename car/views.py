from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from car.forms import CarForm
from car.models import Car
from django.db.models import Q


class CarRead(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value == '':
                continue
            if value and key in vars(Car):
                query &= Q(**{''+key+'__icontains': value})
        object_list = Car.objects.filter(query)
        return {"object_list": Car.objects.filter(query)}
