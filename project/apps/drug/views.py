from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

# AUTH decorators
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required

from drug import models,forms #<< AQUI ESTA EL PROBLEMA

# Create your views here.
def index(request):
    return render(request, 'drug/index.html')

# class DrugListView:
class DrugListView(ListView):
    model = models.Drug
    template_name = 'drug/drug_list.html'

# class DrugDetailView:
@method_decorator(login_required, name='dispatch')
class DrugDetailView(DetailView):
    model = models.Drug
    template_name = 'drug/drug_detail.html'

# class DrugCreateView:
@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class DrugCreateView(CreateView):
    model = models.Drug
    form_class = forms.DrugForm
    template_name = 'drug/drug_create.html'
    success_url = reverse_lazy('drug:drug_list')

# class DrugUpdateView:
@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class DrugUpdateView(UpdateView):
    model = models.Drug
    form_class = forms.DrugForm
    template_name = 'drug/drug_update.html'
    success_url = reverse_lazy('drug:drug_list')

# class DrugDeleteView:
@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(permission_required('drug.delete_drug', raise_exception=True), name='dispatch')
class DrugDeleteView(DeleteView):
    model = models.Drug
    template_name = 'drug/drug_delete.html'
    success_url = reverse_lazy('drug:drug_list')