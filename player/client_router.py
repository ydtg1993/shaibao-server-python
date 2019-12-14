from django.urls import re_path
from player.api.client_player import ClientPlayerController
from player.api.client_bet import ClientBetController
from player.api.client_card import ClientCardController
from finance.api.client_withdraw import ClientWithdrawController


urlpatterns = [
    re_path('player(/(?P<action>[a-z]\w*))?', ClientPlayerController.as_view()),
    re_path('bet(/(?P<action>[a-z]\w*))?', ClientBetController.as_view()),
    re_path('card(/(?P<action>[a-z]\w*))?', ClientCardController.as_view()),
    re_path('withdraw(/(?P<action>[a-z]\w*))?', ClientWithdrawController.as_view()),
]
