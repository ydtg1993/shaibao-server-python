from django.db import models
from three_server.base.model import BaseModel


class RechargeSetting(BaseModel):
    method = models.CharField(max_length=24, verbose_name='赠送方式')
    gift = models.CharField(max_length=24, verbose_name='赠品类型')
    value = models.CharField(max_length=24, verbose_name='赠送值')
    expand = models.TextField(verbose_name='拓展字段')

    class Meta:
        db_table = "game_recharge_setting"

    @classmethod
    def create(cls):
        pass
