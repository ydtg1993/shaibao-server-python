from django.db import models
from three_server.base.model import BaseModel
import uuid
import decimal
from player.enums.player import BetStatus
from django.db.models import Sum
from hall.models.hall import Result


class Player(BaseModel):
    name = models.CharField(max_length=24, verbose_name='玩家名称')
    password = models.CharField(max_length=32, verbose_name='密码')
    serial = models.CharField(max_length=200, verbose_name='玩家序列号')
    token = models.CharField(default='', max_length=200, verbose_name='密钥')
    phone = models.CharField(max_length=100, verbose_name='手机号')
    avatar = models.CharField(default='', max_length=200, verbose_name='头像')
    gold = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='金币')
    integral = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='积分')
    lock_gold = models.DecimalField(default=0.00, max_digits=19, decimal_places=2, verbose_name='锁定资金')
    status = models.CharField(default='', max_length=200, verbose_name='状态')
    # online = models.BooleanField(default=False, verbose_name='线上')
    own_invite_code = models.CharField(default='', max_length=50, verbose_name='邀请码')
    invite_code = models.CharField(default='', max_length=50, verbose_name='注册邀请码')

    @classmethod
    def create(cls, serial, password, phone, code):
        try:
            obj = cls(
                password=password,
                name=serial,
                serial=serial,
                phone=phone,
                invite_code=code,
                token=uuid.uuid1()
            )
            obj.save()
            return True, obj
        except Exception as e:
            return False, None

    @classmethod
    def update_online_status(cls, token):
        cls.objects.get()

    @classmethod
    def find_by_serial(cls, serials):
        factor = models.Q()
        factor.connector = "OR"
        for serial in serials.split(','):
            factor.children.append(('serial', serial))
        return cls.objects.filter(factor).values('id')

    @classmethod
    def all_player_id(cls):
        return cls.objects.filter().values('id')

    @classmethod
    def search(cls, data):
        ls = cls.objects.filter().order_by().values(
            'name',
            'serial',
            'phone',
            'gold',
            'status'
        )[
             (int(data['current_page']) - 1) * int(data['page_size']):
             (int(data['current_page']) - 1) * int(data['page_size']) + int(data['page_size'])
         ]
        total = cls.objects.count()
        return {'ls': ls, 'total': total}

    @classmethod
    def authenticate(cls, phone, password):
        try:
            print(phone, password)
            obj = cls.objects.get(phone=phone, password=password)
            obj.token = uuid.uuid1()
            obj.save()
            return True, obj
        except cls.DoesNotExist as e:
            return True, None

    @classmethod
    def reset_password(cls, phone, new_password):
        try:
            player = cls.objects.get(phone=phone)
            player.password = new_password
            player.token = uuid.uuid1()
            player.save()
            return True, player
        except cls.DoesNotExist:
            return True, None

    @classmethod
    def find_by_token(cls, token):
        try:
            player = cls.objects.get(token=token)
            return True, player
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def check_token(cls, token):
        try:
            cls.objects.get(token=token)
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def reset_token(cls, token):
        try:
            print('reset_token', token)
            player = cls.objects.get(token=token)
            player.token = ""
            player.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def update_player_gold(cls, token, value, lock_gold=0):
        try:
            player = cls.objects.get(token=token)
            player.gold += decimal.Decimal(value)
            player.lock_gold += decimal.Decimal(lock_gold)
            player.save()
            return True, player
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def update_player_integral(cls, token, value):
        try:
            player = cls.objects.get(token=token)
            player.integral += decimal.Decimal(value)
            player.save()
            return True, player
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def get_player_gold(cls, token):
        try:
            player = cls.objects.get(token=token)
            return True, player.gold
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def update_gold_by_id(cls, player_id, value):
        try:
            player = cls.objects.get(id=player_id)
            player.gold += decimal.Decimal(value)
            player.save()
            return True, player
        except cls.DoesNotExist:
            return False, None


class BetRecord(BaseModel):
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, verbose_name='玩家')
    sequence = models.ForeignKey(Result, to_field='sequence', null=True, on_delete=models.SET_NULL, verbose_name='大厅期号')
    bet_amount = models.DecimalField(default=0, max_digits=19, decimal_places=2, verbose_name='下注金额')
    bonus = models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name='中奖金额')
    bet_type = models.CharField(default='', max_length=16, verbose_name='投注类型')
    state = models.IntegerField(default=BetStatus.DEFAULT.value, verbose_name='状态')

    @classmethod
    def create(cls, player_id, sequence, bet_amount, bet_type, bonus):
        from hall.models.hall import Result
        _, s = Result.find_by_seq(sequence)
        print(bet_type)
        cls.objects.create(
            player_id=player_id,
            sequence=s,
            bet_amount=bet_amount,
            bet_type=bet_type,
            bonus=bonus
        )

    @classmethod
    def find_by_seq(cls, sequence):
        return cls.objects.filter(sequence=sequence).values()

    @classmethod
    def search_bet_record(cls, **params):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor2 = models.Q()
        factor2.connector = "OR"
        factor1.children.append(('player_id', params['player_id']))
        for state in params['types']:
            factor2.children.append(('state', state))
        factor1.add(factor2, 'AND')
        return cls.objects.filter(factor1).values(
            'sequence__sequence',
            'bet_type',
            'state',
        ).annotate(
            bonus=Sum('bonus'),
            bet_amount=Sum('bet_amount')
        ).values(
            'sequence',
            'sequence__create_at',
            'sequence__result',
            'state',
            'bonus',
            'bet_type',
            'bet_amount',
        ).order_by('-sequence__create_at')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]

    @classmethod
    def set_lose(cls, sequence, win_types):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor2 = models.Q()
        factor2.connector = "OR"
        factor1.children.append(('sequence', sequence))
        for state in win_types:
            factor2.children.append(('bet_type', state))
        factor1.add(~factor2, 'AND')
        cls.objects.filter(factor1).update(state=BetStatus.LOSE.value, bonus=0)

    @classmethod
    def set_win(cls, sequence, win_types):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor2 = models.Q()
        factor2.connector = "OR"
        factor1.children.append(('sequence', sequence))
        for state in win_types:
            factor2.children.append(('bet_type', state))
        factor1.add(factor2, 'AND')
        cls.objects.filter(factor1).update(state=BetStatus.WIN.value)

    @classmethod
    def search_win(cls, sequence, win_types):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor2 = models.Q()
        factor2.connector = "OR"
        factor1.children.append(('sequence', sequence))
        for state in win_types:
            factor2.children.append(('bet_type', state))
        factor1.add(factor2, 'AND')
        return cls.objects.filter(factor1).values(
            'player',
        ).annotate(
            bonus=Sum('bonus')
        ).values('player__token', 'bet_type', 'bonus')

    @classmethod
    def sum_win(cls, sequence, win_types):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor2 = models.Q()
        factor2.connector = "OR"
        factor1.children.append(('sequence', sequence))
        for state in win_types:
            factor2.children.append(('bet_type', state))
        factor1.add(factor2, 'AND')
        return cls.objects.filter(factor1).values(
            'sequence'
        ).annotate(
            bonus=Sum('bonus')
        ).values('bonus')

    @classmethod
    def sum_bet(cls, sequence):
        factor1 = models.Q()
        factor1.connector = "AND"
        factor1.children.append(('sequence', sequence))
        return cls.objects.filter(factor1).values(
            'sequence'
        ).annotate(
            sum_bet_amount=Sum('bet_amount')
        ).values('sum_bet_amount')

    @classmethod
    def sum_player_bet(cls, player_id, time_range):
        return cls.objects.filter(
            create_at__range=time_range,
            player_id=player_id,
            state=BetStatus.WIN.value
        ).values('player_id').annotate(
            total=Sum('bonus')
        ).values(
            'player_id',
            'player__name',
            'total',
        )

    @classmethod
    def leader_board(cls, current_page, page_size, time_range):
        ls = cls.objects.filter(
            # create_at__range=time_range,
            state=BetStatus.WIN.value
        ).values('player_id').annotate(
            total=Sum('bonus')
        ).values(
            'player_id',
            'player__name',
            'total',
        ).order_by('-total')[
             (int(current_page) - 1) * int(page_size):
             (int(current_page) - 1) * int(page_size) + int(page_size)
        ]
        total = cls.objects.filter(
            create_at__range=time_range,
            state=BetStatus.WIN.value
        ).values('player_id').annotate(
            total=Sum('bonus')
        ).count()
        return {'ls': ls, 'total': total}


class InviteRecord(BaseModel):
    pass
