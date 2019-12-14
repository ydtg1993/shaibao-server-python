from django.urls import re_path
from mail.api.server_mail import ServerMailController

urlpatterns = [
    re_path('mail(/(?P<action>[a-z]\w*))?', ServerMailController.as_view()),
]
