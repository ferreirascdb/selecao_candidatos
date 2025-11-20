
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from candidatos import views as candidatos_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candidatos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='candidatos/login.html'), name='login')
    
]
