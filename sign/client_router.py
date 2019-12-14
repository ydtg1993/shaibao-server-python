from django.urls import re_path
from sign.api.client_sign import ClientSignController
from sign.api.client_sign_reward import ClientSignRewardController

urlpatterns = [
    re_path('sign(/(?P<action>[a-z]\w*))?', ClientSignController.as_view()),
    re_path('reward(/(?P<action>[a-z]\w*))?', ClientSignRewardController.as_view()),
]
