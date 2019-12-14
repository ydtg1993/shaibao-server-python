from three_server.base.model import BaseModel
from django.db import models
from player.models.player import Player
from django.contrib.auth.models import User


class RechargeRecord(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='玩家')
    depositor = models.CharField(max_length=24, verbose_name='存款人')
    pay_money = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='充值金额')
    type = models.CharField(max_length=24, verbose_name='类型')
    payee = models.CharField(max_length=24, verbose_name='收款人')
    account_id = models.CharField(max_length=124, verbose_name='收款账户')
    status = models.IntegerField(default=0, verbose_name='状态')
    remark = models.CharField(default="", max_length=128, verbose_name='备注')
    reviewer = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='审核人')

    class Meta:
        db_table = "finance_recharge_record"

    @classmethod
    def add(cls, **params):
        cls(**params).save()

    @classmethod
    def check_recharge(cls, **params):
        try:
            obj = cls.objects.get(id=params['obj_id'])
            obj.status = params['allow']
            obj.remark = params['remark']
            obj.reviewer_id = params['reviewer_id']
            obj.save()
            return True, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def client_server(cls, **params):
        pass

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().order_by().values(
            'player__name',
            'create_at',
            'id',
            'depositor',
            'pay_money',
            'type',
            'payee',
            'account_id',
            'status',
            'reviewer__username'
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
            'type',
            'create_at',
            'pay_money',
            'status'
        )[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}