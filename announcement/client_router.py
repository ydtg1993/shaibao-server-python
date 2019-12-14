from django.urls import re_path
from announcement.api.client_drive import ClientDriverController
from announcement.api.client_notice import ClientNoticeController
from announcement.api.client_pig import PigController

urlpatterns = [
    re_path('drive(/(?P<action>[a-z]\w*))?', ClientDriverController.as_view()),
    re_path('notice(/(?P<action>[a-z]\w*))?', ClientNoticeController.as_view()),
    re_path('pig(/(?P<action>[a-z]\w*))?', PigController.as_view()),
]
