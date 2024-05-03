from typing import Any
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Product
# Create your views here.

@method_decorator(login_required, name= 'dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'store/product/list.html'
    context_object_name = 'products'
    paginate_by = 5
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(products, self.paginate_by)
        #context['is_paginated'] = paginator.num_pages > 1
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context['products'] = products
        return context
    

@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    template_name = 'store/product/create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['description'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 50, 'style': 'resize: none;'})  # Customize the size here
        return form
    

@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product/details.html'
    context_object_name = 'product'


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/product/update.html'
    context_object_name = 'product'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('product-details', kwargs= {'pk': self.object.id})
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['description'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 50, 'style': 'resize: none;'})  # Customize the size here
        return form


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product/delete.html'
    success_url = reverse_lazy('product-list')
    context_object_name = 'product'


