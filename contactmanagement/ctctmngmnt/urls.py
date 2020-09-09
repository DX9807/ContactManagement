from django.urls import path
from .views import contact_list,contact_detail,new_contact,delete_contact,contact_edit

urlpatterns = [
    path('',contact_list),
    path('detail/<int:pk>',contact_detail),
    path('create/',new_contact),
    path('delete/<int:pk>',delete_contact),
    path('edit/<int:pk>',contact_edit),
]