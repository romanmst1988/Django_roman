from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product, Contact
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact

def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})




def home(request):  # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.all().order_by("-id")[:5]

    # Выводим в консоль с использованием контекста
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name} (ID: {product.id})")

    context = {
        "title": "Главная страница",
        "latest_products": latest_products,  # Передаем в шаблон
    }
    return render(request, "catalog/home.html", context=context)


def contacts(request):
    # Получаем активные контактные данные с использованием контекста
    contact_info = Contact.objects.filter(is_active=True).first()

    context = {
        "title": "Контакты",
        "contact_info": contact_info,
    }
    return render(request, "catalog/contacts.html", context=context)


def contact_view(request):
    # Отображение формы
    return render(request, 'contacts.html')


def contact_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    # Если запрос не POST, перенаправляем на форму
    return render(request, 'contacts.html')


def real_estate_catalog(request):
    product_all = Product.objects.all()
    context = {'products': product_all}
    return render(request, "catalog/real_estate_catalog.html", context=context)

def product_detail(request, pk): #Создаем контроллер для страницы товара
    # Получаем объект Product по его ID
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})
