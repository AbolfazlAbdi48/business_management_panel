"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('src.core.urls')),
    path('', include('pwa.urls')),
    path('account/logout', LogoutView.as_view(), name='logout'),
    path('account/', include('src.accounts.urls')),
    path('manager/', include('src.managers.urls')),
    path('staff/', include('src.staff_module.urls')),
    path('customer/', include('src.customer_module.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'core.views.handler404'
handler403 = 'core.views.handler403'
