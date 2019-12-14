from django.urls import re_path
from announcement.api.server_drive import ServerDriveController
from announcement.api.server_notice import ServerNoticeController


urlpatterns = [
    re_path('drive(/(?P<action>[a-z]\w*))?', ServerDriveController.as_view()),
    re_path('notice(/(?P<action>[a-z]\w*))?', ServerNoticeController.as_view())
]
