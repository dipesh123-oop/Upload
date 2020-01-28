from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('product/',view_add_product),
   path('product/save',view_productdata_save),
   path('product/productlist',view_product_lists),
   path('product/edit/<int:ID>',view_productdata_updateform),
   path('product/edit/update/<int:ID>',view_update_form_data_in_db),
   path('product/delete/<int:ID>', view_delete), 
   # path('user/register', view_login_page),
   path('signup/',view_register_user),
   path('restrictpage/',view_authenticate_user),
   path("logout/", view_logout_request, name="logout")
]