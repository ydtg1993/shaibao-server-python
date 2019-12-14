from django.db import models
from three_server.base.model import BaseModel
from player.models.player import Player
from finance.models.bank_option import BankOption


class Card(BaseModel):
    name = models.CharField(max_length=24, verbose_name='姓名')
    number = models.CharField(max_length=32, verbose_name='号码')
    bank = models.ForeignKey(BankOption, on_delete=models.CASCADE, verbose_name='银行')
    bank_branch = models.CharField(default='', max_length=128, verbose_name='开户行支行')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='玩家')

    @classmethod
    def create_card(cls, **params):
        cls(**params).save()

    @classmethod
    def find_by_player(cls, player_id):
        return cls.objects.filter(player_id=player_id).values(
            'name',
            'number',
            'bank__name',
            'bank__id',
            'bank_branch'
        )

    @classmethod
    def update_card(cls):
        pass

    @classmethod
    def delete_card(cls):
        pass




