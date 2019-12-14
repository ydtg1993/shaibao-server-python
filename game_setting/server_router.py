from django.urls import re_path
from game_setting.api.server_recharge import ServerRechargeController

urlpatterns = [
    re_path('recharge(/(?P<action>[a-z]\w*))?', ServerRechargeController.as_view()),
]
