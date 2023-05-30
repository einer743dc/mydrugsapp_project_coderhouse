from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from drug import models,forms #<< AQUI ESTA EL PROBLEMA

# Create your views here.
def index(request):
    return render(request, 'drug/index.html')

# class DrugListView:
class DrugListView(ListView):
    model = models.Drug
    template_name = 'drug/drug_list.html'

# class DrugDetailView:
class DrugDetailView(DetailView):
    model = models.Drug
    template_name = 'drug/drug_detail.html'

# class DrugCreateView:
class DrugCreateView(CreateView):
    model = models.Drug
    form_class = forms.DrugForm
    template_name = 'drug/drug_create.html'
    success_url = reverse_lazy('drug:drug_list')

# class DrugUpdateView:
class DrugUpdateView(UpdateView):
    model = models.Drug
    template_name = 'drug/drug_update.html'
    success_url = reverse_lazy('drug:drug_list')

# class DrugDeleteView:
class DrugDeleteView(DeleteView):
    model = models.Drug
    template_name = 'drug/drug_delete.html'
    success_url = reverse_lazy('drug:drug_list')