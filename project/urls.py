"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from clients import urls as client_urls
from home import urls as home_urls
from user import urls as register_urls
from product import urls as product_urls
from sales import urls as sales_urls

urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('clients/', include(client_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include(register_urls)),
    path('product/', include(product_urls)),
    path('sales/', include(sales_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
