from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Contact, Product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.shortcuts import render
from .services import get_products_by_category

def products_by_category_view(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, "products_by_category.html", {"products": products})

# from django.core.cache import cache
# from django.http import HttpResponse
#
# def my_view(request):
#     # Попытка получить данные из кеша
#     data = cache.get('my_key')
#
#     # Если данные не найдены в кеше, выполняем вычисления и сохраняем результат в кеш
#     if not data:
#         data = 'some expensive computation'
#         cache.set('my_key', data, 60 * 15)  # Кешируем данные на 15 минут
#
#     # Возвращаем ответ с данными
#     return HttpResponse(data)

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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

@method_decorator(cache_page(60 * 15), name='dispatch')  # 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user

        # Проверяем права пользователя
        context['is_owner'] = user.is_authenticated and user == product.owner
        context['is_moderator'] = user.is_authenticated and (user.is_staff or user.is_superuser)
        context['can_unpublish'] = context['is_owner'] or context['is_moderator']
        context['can_publish'] = context['is_moderator'] and not product.is_published

        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Продукт успешно создан!')
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image', 'is_published']

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успешно обновлен!')
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Продукт успешно удален!')
        return super().delete(request, *args, **kwargs)


@login_required
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Проверяем права
    if request.user == product.owner or request.user.is_staff:
        product.is_published = False
        product.save()
        messages.success(request, 'Продукт снят с публикации')
    else:
        messages.error(request, 'У вас нет прав для этого действия')

    return redirect('catalog:product_detail', pk=product.pk)


@login_required
def publish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Только модераторы/админы могут публиковать
    if request.user.is_staff:
        product.is_published = True
        product.save()
        messages.success(request, 'Продукт опубликован')
    else:
        messages.error(request, 'У вас нет прав для этого действия')

    return redirect('catalog:product_detail', pk=product.pk)
