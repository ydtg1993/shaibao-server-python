from django.db import models
from three_server.base.model import BaseModel
from player.models.player import Player


class PigRecord(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='玩家')
    gold = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='积分')

    class Meta:
        db_table = "announcement_pig_record"

    @classmethod
    def create(cls, **params):
        cls.objects.create(
            player_id=params['player_id'],
            gold=params['gold']
        )

    @classmethod
    def client_search(cls):
        return cls.objects.filter().values(
            'player__name',
            'gold'
        ).order_by('-id')[:50]

    @classmethod
    def server_search(cls, **params):
        ls = cls.objects.filter().values(
            'player__name',
            'gold'
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
             ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}
