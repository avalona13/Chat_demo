from django.urls import path
from .views import chat_detail


urlpatterns = [
    path('', chat_detail, name='mainchat'),
]