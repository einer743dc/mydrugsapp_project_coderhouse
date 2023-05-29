from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drug_list', views.DrugListView.as_view(), name='drug_list'),
    path('drug_detail/<int:pk>', views.DrugDetailView.as_view(), name='drug_detail'),
    path('drug_create', views.DrugCreateView.as_view(), name='drug_create'),
    path('drug_update/<int:pk>', views.DrugUpdateView.as_view(), name='drug_update'),
    path('drug_delete/<int:pk>', views.DrugDeleteView.as_view(), name='drug_delete'),
]