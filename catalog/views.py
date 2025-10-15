from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product, Contact


def home(request):  # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.all().order_by("-id")[:5]

    # Выводим в консоль
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name} (ID: {product.id})")

    context = {
        "title": "Главная страница",
        "latest_products": latest_products,  # Передаем в шаблон
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    # Получаем активные контактные данные
    contact_info = Contact.objects.filter(is_active=True).first()

    context = {
        "title": "Контакты",
        "contact_info": contact_info,
    }
    return render(request, "catalog/contacts.html", context)


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


def about(request):
    return render(request, "catalog/about.html")
