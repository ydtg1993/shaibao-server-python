from django.urls import re_path
from finance.api.client_bank_option import ClientBankOptionController
from finance.api.client_pay import ClientPayController
from finance.api.client_withdraw import ClientWithdrawController

urlpatterns = [
    re_path('bank(/(?P<action>[a-z]\w*))?', ClientBankOptionController.as_view()),
    re_path('pay(/(?P<action>[a-z]\w*))?', ClientPayController.as_view()),
    re_path('withdraw(/(?P<action>[a-z]\w*))?', ClientWithdrawController.as_view()),
]
