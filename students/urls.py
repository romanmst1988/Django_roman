from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.sumbit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item'),
#     # path('list/', views.students_list, name='list')
#     ]