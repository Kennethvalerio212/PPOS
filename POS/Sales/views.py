from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Product



def home(request):
    context = {
        'posts': Product.objects.all()
    }
    return render(request, 'home.html', context)


class SalesListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering ='product_id'

class SalesDetailView(DetailView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'detail.html'  

class SalesCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'product_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SalesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'product_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return True


class SalesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    template_name = 'confirm_delete.html'

    def test_func(self):
        return True


def Trans(request):
    return render(request, 'trans.html', {'title': 'About'})


    


def about(request):
    return render(request, 'about.html', {'title': 'About'})