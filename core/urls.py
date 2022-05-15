from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shipping.urls')),
    path('accounts/login/', views.loginView, name='login'),
    path('accounts/logout/', views.logoutView, name='logout'),


]
