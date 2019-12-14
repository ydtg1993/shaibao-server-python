from three_server.base.model import BaseModel
from django.db import models


class BankAccount(BaseModel):
    bank_name = models.CharField(max_length=36, verbose_name='银行名称')
    number = models.TextField(default='', unique=True, verbose_name='账户号码')
    user_name = models.CharField(default='', max_length=24, verbose_name='名称')
    amount_max = models.IntegerField(default=0, verbose_name='最大金额')
    amount_min = models.IntegerField(default=0, verbose_name='最小金额')
    active = models.BooleanField(default=False, verbose_name='激活')

    class Meta:
        db_table = "finance_bank_account"

    @classmethod
    def add(cls, **params):
        cls(**params).save()

    @classmethod
    def remove(cls, ba_id):
        try:
            cls.objects.get(id=ba_id).delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def switch(cls, obj_id):
        try:
            obj = cls.objects.get(id=obj_id)
            obj.active = (False if obj.active else True)
            obj.save()
            return True, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def find_by_id(cls, ba_id):
        try:
            return cls.objects.get(id=ba_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, **params):
        try:
            obj = cls.objects.get(params['id'])
            obj.account_name = params['account_name']
            obj.number = params['number']
            obj.user_name = params['user_name']
            obj.amount_max = params['amount_max']
            obj.amount_min = params['amount_min']
            obj.active = params['active']
        except cls.DoesNotExist:
            return False

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().order_by().values(
            'id',
            'create_at',
            'bank_name',
            'number',
            'user_name',
            'amount_max',
            'amount_min',
            'active',
        )[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
             ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

    @classmethod
    def search_client(cls):
        return cls.objects.filter(
            active=True
        ).order_by().values(
            'id',
            'bank_name',
            'number',
            'user_name',
            'amount_max',
            'amount_min',
        )

    """
    6 ADP[2.7 多] FN[7.5 多]
    7 ADP[10.2 多] FN[22.4 空]
    8 ADP[15.6 多] FN[16.4 空]
    9 ADP[19.5 空] FN[13 多]
   10 ADP[13.5 多] FN[20 空]
    """
