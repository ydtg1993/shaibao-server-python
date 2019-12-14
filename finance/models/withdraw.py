from django.db import models
from three_server.base.model import BaseModel
from player.models.player import Player
from django.contrib.auth.models import User
from finance.enums.withdraw import WithdrawStatusEnum


class Withdraw(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='玩家')
    amount = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='金币')
    status = models.IntegerField(default=WithdrawStatusEnum.DEFAULT.value, verbose_name='状态')
    remark = models.CharField(default="", max_length=128, verbose_name='备注')
    reviewer = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='审核人')

    @classmethod
    def add(cls, **params):
        cls.objects.create(
            player_id=params['player_id'],
            amount=params['amount'],
        )

    @classmethod
    def check_withdraw(cls, **params):
        try:
            obj = cls.objects.get(id=params['obj_id'])
            obj.status = params['allow']
            obj.remark = params['remark']
            obj.reviewer_id = params['reviewer_id']
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def update_status(cls, w_id):
        try:
            obj = cls.objects.get(w_id)
            obj.status = 2
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().values(
            'id',
            'player__serial',
            'player__name',
            'create_at',
            'amount',
            'status',
            'reviewer_id',
            'reviewer__username'
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}

    @classmethod
    def search_client(cls, **params):
        ls = cls.objects.filter(
            player_id=params['player_id']
        ).values(
            'id',
            'create_at',
            'amount',
            'status',
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
         ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}
