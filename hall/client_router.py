from django.urls import re_path
from hall.api.client_hall import ClientHallController
from hall.api.client_result import ClientResultController


urlpatterns = [
    re_path('client(/(?P<action>[a-z]\w*))?', ClientHallController.as_view()),
    re_path('result(/(?P<action>[a-z]\w*))?', ClientResultController.as_view()),
]
