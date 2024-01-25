from django.urls import path
from .views import *
from . import consumers

app_name = "dashboard"
urlpatterns = [
    #path("messagerie/", MessagerieView.as_view(), name='chat_room'),
    path('<str:user_1>/<str:user_2>/', ChatRoomView.as_view(), name='messagerie'),
]
