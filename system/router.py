from django.urls import re_path
from system.api.user import UserController
from system.api.group import GroupController
from system.api.permission import PermissionController


urlpatterns = [
    re_path('user(/(?P<action>[a-z]\w*))?', UserController.as_view()),
    re_path('group(/(?P<action>[a-z]\w*))?', GroupController.as_view()),
    re_path('permission(/(?P<action>[a-z]\w*))?', PermissionController.as_view()),
]
