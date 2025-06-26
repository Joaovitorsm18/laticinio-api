from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')), 
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('sales.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
