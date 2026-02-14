from django.urls import path
from . import views
urlpatterns = [
   path( '', views.home_view, name='home'),
   path ('create/', views.create_product, name='create_product'),
   path('update/<int:product_id>/', views.update_product, name='update_product'),
   path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]               