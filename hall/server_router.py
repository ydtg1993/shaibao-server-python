from django.urls import re_path
from hall.api.server_hall import HallController
from hall.api.server_bet import BetController
from hall.api.server_chip import ChipController
from hall.api.server_result import ResultController
from hall.api.client_hall import ClientHallController


urlpatterns = [
    re_path('hall(/(?P<action>[a-z]\w*))?', HallController.as_view()),
    re_path('bet(/(?P<action>[a-z]\w*))?', BetController.as_view()),
    re_path('chip(/(?P<action>[a-z]\w*))?', ChipController.as_view()),
    re_path('result(/(?P<action>[a-z]\w*))?', ResultController.as_view()),
]
