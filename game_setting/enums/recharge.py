from enum import Enum


class RechargeMethod(Enum):
    INTERVAL = 'INTERVAL'
    PERCENTAGE = 'PERCENTAGE'
    FIXED = 'FIXED'


class RechargeMethodMsg(Enum):
    INTERVAL = '区间'
    PERCENTAGE = '百分比'
    FIXED = '固定值'


class RechargeType(Enum):
    GOLD = 'GOLD'
    INTEGRAL = 'INTEGRAL'


class RechargeTypeMsg(Enum):
    GOLD = '金币'
    INTEGRAL = '积分'
