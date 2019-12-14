from django.db import models
from three_server.base.model import BaseModel
from sign.enums.sign_reward import RewardType


class SignReward(BaseModel):
    sign_day = models.IntegerField(default=0, unique=True, verbose_name='签到天数')
    reward_type = models.CharField(default=0, max_length=12, verbose_name='奖励类型')
    reward_value = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='奖励值')

    @classmethod
    def create(cls, **params):
        cls.objects.create(
            sign_day=params['sign_day'],
            reward_type=params['reward_type'],
            reward_value=params['reward_value']
        )

    @classmethod
    def init_sign_reward(cls):
        ssr = [cls(sign_day=i, reward_type=RewardType.GOLD.value, reward_value=i) for i in range(1, 8)]
        cls.objects.bulk_create(ssr)

    @classmethod
    def delete_all(cls):
        cls.objects.filter().delete()

    @classmethod
    def find_by_day(cls, day):
        try:
            obj = cls.objects.get(sign_day=day)
            return obj
        except cls.DoesNotExist:
            return None

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().values(
            'id',
            # 'create_at',
            'sign_day',
            # 'reward_type',
            'reward_value'
        ).order_by('id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
         ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}

    @classmethod
    def search_client(cls):
        ls = cls.objects.filter().values(
            'sign_day',
            'reward_type',
            'reward_value'
        ).order_by('sign_day')
        return ls

    @classmethod
    def update_sign_reward(cls, **params):
        try:
            obj = cls.objects.get(id=params['id'])
            obj.sign_day = params['sign_day']
            obj.sign_day = params['reward_type']
            obj.sign_day = params['reward_value']
            obj.save()
        except cls.DoesNotExist:
            return False
