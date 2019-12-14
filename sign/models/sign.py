from django.db import models
from three_server.base.model import BaseModel
from player.models.player import Player


class SignRecord(BaseModel):
    player = models.OneToOneField(Player, unique=True, on_delete=models.CASCADE, verbose_name='玩家')
    start_time = models.IntegerField(default=0, verbose_name='开始签到时间')
    end_time = models.IntegerField(default=0, verbose_name='结束签到时间')
    total = models.IntegerField(default=0, verbose_name='总计天数')

    @classmethod
    def create_or_update(cls, player_id, **params):
        cls.objects.update_or_create(
            player_id=player_id,
            defaults=params
        )

    @classmethod
    def find_by_player_id(cls, player_id):
        try:
            obj = cls.objects.get(player_id=player_id)
            return obj
        except cls.DoesNotExist:
            return None

    @classmethod
    def check_sign(cls, player_id, end_time):
        try:
            cls.objects.get(player_id=player_id, end_time=end_time)
            return True
        except cls.DoesNotExist:
            return False
