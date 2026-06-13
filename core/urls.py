
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('pacientes/', include('apps.pacientes.urls')),
    path('valoracion/', include('apps.valoracion.urls')),
]