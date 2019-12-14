from django.urls import re_path
from sign.api.server_sign_reward import ServerSignRewardController

urlpatterns = [
    re_path('sign_reward(/(?P<action>[a-z]\w*))?', ServerSignRewardController.as_view()),
]
