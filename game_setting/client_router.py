from django.urls import re_path
from finance.api.client_bank_option import ClientBankOptionController

urlpatterns = [
    re_path('bank(/(?P<action>[a-z]\w*))?', ClientBankOptionController.as_view()),
]
