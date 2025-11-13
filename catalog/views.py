from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Contact, Product
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


class ContactView(TemplateView):
    template_name = "catalog/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.filter(is_active=True)
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"
    paginate_by = 20


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_owner'] = user.is_authenticated and user == self.object.owner
        context['is_moderator'] = (
                user.is_authenticated and user.groups.filter(name='Модератор продуктов').exists()
        )
        context['can_unpublish'] = (
                user.is_authenticated and user.has_perm('catalog.can_unpublish_product')
        )
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'status']
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'status']
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists()

@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = 'unpublished'
    product.save()
    messages.success(request, f'Продукт "{product.name}" снят с публикации.')
    return redirect('product_list')
