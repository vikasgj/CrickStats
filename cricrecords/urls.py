"""
URL configuration for cricrecords project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from records import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('records.urls')),
    path('api/', include('records.api_urls')),
    path('top-wickets/', views.top_wicket_takers, name='top-wicket-takers'),

]

