from enum import Enum


class RewardType(Enum):
    GOLD = 'GOLD'  # 金币
    OBJECT = 'OBJECT'  # 金币


class RewardTypeMsg(Enum):
    GOLD = '金币'  # 金币
    OBJECT = '实物'  # 金币
