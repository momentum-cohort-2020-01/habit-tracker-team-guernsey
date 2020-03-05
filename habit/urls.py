"""habit URL Configuration

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
from django.conf import settings
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', views.habit_list, name='habit-list'),
    path('habit/add/', views.habit_add, name='habit-add'),
    path('habit/<int:pk>', views.habit_details, name='habit-details'),
    path('accounts/', include('registration.backends.default.urls')),
    path('habit/edit/<int:pk>', views.habit_edit, name='habit-edit')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns