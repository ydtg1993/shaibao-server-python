from django.urls import re_path
from mail.api.client_mail import ClientMailController

urlpatterns = [
    re_path('mail(/(?P<action>[a-z]\w*))?', ClientMailController.as_view()),
]
