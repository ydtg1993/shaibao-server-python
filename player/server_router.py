from django.urls import re_path
from player.api.server_player import ServerPlayerController


urlpatterns = [
    re_path('player(/(?P<action>[a-z]\w*))?', ServerPlayerController.as_view()),
]
