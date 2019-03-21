"""webchat URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        LoginView.as_view(redirect_field_name ='mainchat',
        redirect_authenticated_user = True,
        template_name='mainchat/login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mainchat/', include('mainchat.urls')),
]