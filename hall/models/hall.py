from django.db import models
from three_server.base.model import BaseModel
from three_server import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from three_server.enums.dice_type import DiceType
from hall.enums.hall import HallStage, LotteryType, HallTag
import django.utils.timezone as timezone


class Hall(BaseModel):
    name = models.CharField(max_length=24, verbose_name='大厅名称')
    tag = models.CharField(default='', unique=True, max_length=24, verbose_name='大厅标签')
    bet_type = models.IntegerField(default=0, verbose_name='下注类型')
    lottery_time = models.DateTimeField(default=timezone.now, verbose_name='开奖时间')
    lottery_type = models.CharField(default=LotteryType.Self.value, max_length=24, verbose_name='开奖类型')
    game_date = models.IntegerField(default=0, verbose_name='每局时间')
    status = models.IntegerField(default=0, verbose_name='状态')
    active = models.BooleanField(default=False, verbose_name='激活')
    stage = models.CharField(default=HallStage.StartStage.value, max_length=24, verbose_name='大厅阶段')
    total = models.IntegerField(default=0, verbose_name='总局数')

    @classmethod
    def create(cls, data):
        cls.objects.create(
            name=data['name'],
            game_date=data['game_date'],
            total=data['total'],
            tag=data['hall_tag'],
            lottery_type=data['lottery_type']
        )

    @classmethod
    def edit(cls, data):
        try:
            hall = cls.objects.get(id=data['hall_id'])
            hall.name = data['name']
            hall.game_date = data['game_date']
            hall.total = data['total']
            hall.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def search(cls, data):
        ls = cls.objects.filter().values().order_by('-id')[
             (int(data['current_page']) - 1) * int(data['page_size']):
             (int(data['current_page']) - 1) * int(data['page_size']) + int(data['page_size'])
             ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

    @classmethod
    def get_bet_second(cls, hall_id):
        try:
            hall = cls.objects.get(id=hall_id)
            return hall.game_date
        except cls.DoesNotExist:
            return 0

    @classmethod
    def hall_options(cls):
        return cls.objects.filter().values('id', 'name').order_by('-id')

    @classmethod
    def switch(cls, hall_id):
        try:
            obj = cls.objects.get(id=hall_id)
            if obj.active is False and obj.stage != HallStage.StartStage.value:
                return False, None
            obj.active = (False if obj.active else True)
            obj.save()
            return True, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def next_hall_stage(cls, hall_id):
        try:
            hall = cls.objects.get(id=hall_id)
            print(hall.stage)
            # 开始阶段 -> 下注阶段
            if hall.stage == HallStage.StartStage.value:
                hall.stage = HallStage.BetStage.value
                print('开始阶段 -> 下注阶段')
            # 下注阶段 -> 开奖阶段
            elif hall.stage == HallStage.BetStage.value:
                hall.stage = HallStage.LotteryStage.value
                print('下注阶段 -> 开奖阶段')
            # 开奖阶段 -> 结算阶段
            elif hall.stage == HallStage.LotteryStage.value:
                hall.stage = HallStage.SettleStage.value
                print('开奖阶段 -> 结算阶段')
            # 结算阶段 -> 结束阶段
            elif hall.stage == HallStage.SettleStage.value:
                hall.stage = HallStage.OverStage.value
                print('结算阶段 -> 结束阶段')
            # 结束阶段 -> 开始阶段
            elif hall.stage == HallStage.OverStage.value:
                print('结束阶段 -> 开始阶段')
                hall.stage = HallStage.StartStage.value
                hall.save()
                return hall.active
            hall.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def hall_info(cls, hall_id=None, hall_tag=None):
        try:
            result, obj = True, None
            if hall_id is not None:
                obj = cls.objects.get(id=hall_id, active=True)
            elif hall_tag is not None:
                obj = cls.objects.get(tag=hall_tag, active=True)
            else:
                result = False
            return result, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def update_lottery_time(cls, hall_id, value):
        try:
            hall = cls.objects.get(id=hall_id)
            hall.lottery_time = value
            hall.save()
            return True
        except cls.DoesNotExist:
            return False


class HallBetOption(BaseModel):
    hall = models.ForeignKey(Hall, null=True, on_delete=models.SET_NULL, verbose_name='大厅')
    position = models.IntegerField(default=0, verbose_name='位置')
    dice_type = models.CharField(default='', max_length=24, verbose_name='骰型')
    active = models.BooleanField(default=False, verbose_name='显示')
    odds = models.DecimalField(default=0, max_digits=19, decimal_places=2, verbose_name='赔率')

    @receiver(post_save, sender=settings.HALL_MODEL)
    def create(sender, instance=None, created=False, **kwargs):
        if created:
            ps = []
            position = 1
            for index, key in DiceType.__members__.items():
                ps.append(HallBetOption(
                    hall_id=instance.id,
                    position=position,
                    dice_type=DiceType[index].value,
                    active=False,
                    odds=0
                ))
                position += 1
            HallBetOption.objects.bulk_create(ps)

    @classmethod
    def find_by_hall_id(cls, hall_id):
        ls = cls.objects.filter(hall_id=hall_id).order_by('position').values(
        )
        return ls

    @classmethod
    def find_by_hall_id_c(cls, hall_id):
        ls = cls.objects.filter(hall_id=hall_id).order_by('position').values(
            'position',
            'dice_type',
            'odds'
        )
        return ls

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
    def edit(cls, obj_id, value):
        print('HallBet', obj_id, value)
        try:
            obj = cls.objects.get(id=obj_id)
            obj.odds = value
            obj.save()
            return True
        except cls.DoesNotExist:
            return False


class HallChipOption(BaseModel):
    hall = models.ForeignKey(Hall, null=True, on_delete=models.SET_NULL, verbose_name='大厅')
    position = models.IntegerField(default=0, verbose_name='位置')
    active = models.BooleanField(default=False, verbose_name='显示')
    value = models.IntegerField(default=0, verbose_name='面值')

    @receiver(post_save, sender=settings.HALL_MODEL)
    def create(sender, instance=None, created=False, **kwargs):
        if created:
            ps = [HallChipOption(hall_id=instance.id, position=(i+1), active=False, value=0) for i in range(6)]
            HallChipOption.objects.bulk_create(ps)

    @classmethod
    def find_by_hall_id(cls, hall_id):
        ls = cls.objects.filter(hall_id=hall_id).order_by('position').values()
        return ls

    @classmethod
    def find_by_hall_id_c(cls, hall_id):
        ls = cls.objects.filter(hall_id=hall_id).order_by('position').values(
            'position',
            'value'
        )
        return ls

    @classmethod
    def switch(cls, chip_id):
        try:
            obj = cls.objects.get(id=chip_id)
            obj.active = (False if obj.active else True)
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def edit(cls, obj_id, value):
        print('HallChip', obj_id, value)
        try:
            obj = cls.objects.get(id=obj_id)
            obj.value = value
            obj.save()
            return True
        except cls.DoesNotExist:
            return False


class Result(BaseModel):
    hall = models.ForeignKey(Hall, null=True, on_delete=models.SET_NULL, verbose_name='大厅')
    sequence = models.CharField(max_length=24, unique=True, verbose_name='期号')
    bet_count = models.DecimalField(default=0, max_digits=19, decimal_places=2, verbose_name='下注统计')
    bonus = models.DecimalField(default=0, max_digits=19, decimal_places=2, verbose_name='开奖金额')
    result = models.CharField(default='', max_length=24, verbose_name='开奖结果')
    big = models.BooleanField(default=False, verbose_name='大')
    even = models.BooleanField(default=False, verbose_name='双')
    sum = models.IntegerField(default=0, verbose_name='值')

    @classmethod
    def init(cls, hall_id, sequence):
        return cls.objects.create(hall_id=hall_id, sequence=sequence)

    @classmethod
    def sum_now(cls, hall_id, date_range):
        return cls.objects.filter(hall_id=hall_id, create_at__range=date_range).count()

    @classmethod
    def update_bonus_and_bet_count(cls, sequence, bonus, bet_count):
        try:
            obj = cls.objects.get(sequence=sequence)
            obj.bonus = bonus
            obj.bet_count = bet_count
            obj.save()
        except cls.DoesNotExist:
            pass

    @classmethod
    def find_by_seq(cls, seq):
        try:
            obj = cls.objects.get(sequence=seq)
            return True, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def set_result(cls, seq, result):
        try:
            obj = cls.objects.get(sequence=seq)
            sum_value = sum(result)
            obj.result = result
            obj.big = 11 <= sum_value <= 18
            obj.even = sum_value % 2 == 0
            obj.sum = sum_value
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def get_result(cls, seq):
        try:
            obj = cls.objects.get(sequence=seq)
            return obj.result
        except cls.DoesNotExist:
            return None

    @classmethod
    def search_server(cls, **data):
        ls = cls.objects.filter().values(
            'hall__name',
            'sequence',
            'bonus',
            'bet_count',
            'result',
            'big',
            'even',
            'sum'
        ).order_by('-id')[
         (int(data['current_page']) - 1) * int(data['page_size']):
         (int(data['current_page']) - 1) * int(data['page_size']) + int(data['page_size'])
        ]
        total = cls.objects.filter().count()
        return {'ls': ls, 'total': total}

    @classmethod
    def search_client(cls, hall_tag, date_range):
        print(date_range)
        ls = cls.objects.filter(hall__tag=hall_tag, create_at__range=date_range).values(
            'id',
            'sequence',
            'result',
            'big',
            'even',
            'sum'
        ).order_by('-id')[1:11]
        return ls



