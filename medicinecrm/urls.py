
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/',include([
path('user/', include('apps.employee.urls')),
        path('customer/', include('apps.customer.urls')),
path('order/', include('apps.orders.urls')),
path('inventory/', include('apps.inventory.urls')),
    ])),
]


