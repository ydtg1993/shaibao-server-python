from django.urls import re_path
from finance.api.server_bank_option import ServerBankOptionController
from finance.api.server_bank_account import ServerBankAccountController
from finance.api.server_fast_account import ServerFastAccountController
from finance.api.server_recharge_record import ServerRechargeRecordController
from finance.api.server_withdraw import ServerWithdrawController


urlpatterns = [
    re_path('bank_option(/(?P<action>[a-z]\w*))?', ServerBankOptionController.as_view()),
    re_path('bank_account(/(?P<action>[a-z]\w*))?', ServerBankAccountController.as_view()),
    re_path('fast_account(/(?P<action>[a-z]\w*))?', ServerFastAccountController.as_view()),
    re_path('recharge(/(?P<action>[a-z]\w*))?', ServerRechargeRecordController.as_view()),
    re_path('withdraw(/(?P<action>[a-z]\w*))?', ServerWithdrawController.as_view()),
]
