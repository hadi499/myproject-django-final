from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_data', views.all_data, name='all-data'),
    path('create/', views.create, name='create'),
    path('tarif/', views.tarifperkilo, name='tarif'),
    path('gantitarif/', views.ganti_tarif, name='ganti-tarif'),
    path('detail/<int:pk>/', views.detail, name='shipping-detail'),
    path('category/', views.category, name='category'),
    path('ganti_category/', views.ganti_category, name='ganti-category'),

]
