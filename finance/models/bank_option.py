from django.db import models
from three_server.base.model import BaseModel
from player.enums.bank_option import BankOptionEnum


class BankOption(BaseModel):
    name = models.CharField(max_length=24, unique=True, verbose_name='银行名称')
    active = models.BooleanField(default=True, verbose_name='是否激活')

    class Meta:
        db_table = "finance_bank_option"

    @classmethod
    def init_option(cls):
        bos = [cls(name=b.value, active=True) for b in BankOptionEnum]
        cls.objects.bulk_create(bos)

    @classmethod
    def delete_all(cls):
        cls.objects.filter().delete()

    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.objects.get(name=name)
        except cls.DoesNotExist:
            return None

    @classmethod
    def creat(cls, name):
        cls.objects.create(name=name)

    @classmethod
    def remove(cls, obj_id):
        try:
            cls.objects.get(id=obj_id).delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def switch(cls, bet_id):
        try:
            obj = cls.objects.get(id=bet_id)
            obj.active = (False if obj.active else True)
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().order_by().values(
            'id',
            'name',
            'active'
        )[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
         ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

    @classmethod
    def search_client(cls):
        return cls.objects.filter(active=True).values(
            'id',
            'name'
        )
