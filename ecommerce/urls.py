"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'lbs-1' #login page
admin.site.index_title = 'lbs-1 Administration '
admin.site.site_title = 'lbs-1 Site'
admin.site.site_index = 'lbs-1 Adminstrator'

name = 'lbs-1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path("paystack", include(('paystack.urls','paystack'),namespace='paystack')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
