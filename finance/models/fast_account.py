from three_server.base.model import BaseModel
from django.db import models


class FastAccount(BaseModel):
    account_name = models.CharField(max_length=24, verbose_name='账户名称')
    account_number = models.CharField(default='', max_length=24, verbose_name='账户账号')
    qr_code = models.TextField(default='',  verbose_name='二维码')
    active = models.BooleanField(default=False, verbose_name='激活')

    class Meta:
        db_table = "finance_fast_account"

    @classmethod
    def add(cls, **params):
        cls(**params).save()

    @classmethod
    def remove(cls, fa_id):
        try:
            cls.objects.get(id=fa_id).delete()
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
    def get_active_account(cls):
        try:
            obj = cls.objects.get(active=True)
            return obj
        except cls.DoesNotExist:
            return None

    @classmethod
    def activation(cls, obj_id):
        cls.objects.filter(active=True).update(active=False)
        cls.objects.filter(id=obj_id).update(active=True)

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().order_by().values(
            'id',
            'create_at',
            'account_name',
            'account_number',
            'qr_code',
            'active',
        )[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

    @classmethod
    def search_client(cls, **params):
        ls = cls.objects.filter().order_by().values(
            'id',
            'create_at',
            'account_name',
            'account_number',
            'qr_code',
            'active',
        )[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

