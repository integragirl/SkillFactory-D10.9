from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from car.forms import CarForm
from car.models import Car
from django.db.models import Q


class CarRead(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query == '':
            object_list = Car.objects.all()
        else:
            object_list = Car.objects.filter(Q(name__icontains=query))
        return object_list
