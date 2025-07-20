from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/', include('sales.urls')),
    path('api/', include('users.urls')),
    path('api/', include('transactions.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
