from django.urls import path
from . import views
urlpatterns = [
   path('', views.home_view, name='home'),
   path('list/', views.product_list_view, name='product-list'),
   path('create/', views.product_create_view, name='create_product'),
   path('update/<int:product_id>/', views.product_update_view, name='update_product'),
   path('delete/<int:product_id>/', views.product_delete_view, name='delete_product'),
]