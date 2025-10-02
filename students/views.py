from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'students/about.html')

def contact_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        massage = request.POST.get('massage')

        return HttpResponse(f'Спасибо: {name}! Сообщение получено.')
    return render(request, 'students/contact_post.html')

# def example_view(request):
#     return render(request, 'app/example.html')
#
# def show_data(request):
#     if request.method == 'GET':
#         return render(request, 'app/show_data.html')
#
# def sumbit_data(request):
#     if request.method == 'POST':
#         return HttpResponse('Данные отправлены')
#
# def show_item(request, item_id):
#     return render(request, 'app/item.html', {'item_id': item_id})