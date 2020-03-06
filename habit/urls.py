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
    path('habit/<int:pk>/delete', views.habit_delete, name='habit-delete'),
    path('habit/edit/<int:pk>', views.habit_edit, name='habit-edit'),
    path('habit/progress/edit/<int:pk>', views.progress_edit, name='progress-edit'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns