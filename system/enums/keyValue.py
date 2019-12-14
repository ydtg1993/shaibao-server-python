from enum import Enum


class Keys(Enum):
    RECHARGE_TACTICS_INFO = 'RECHARGE_TACTICS_INFO'             # 充值策略
    RECHARGE_TACTICS_ACTIVATE = 'RECHARGE_TACTICS_ACTIVATE'     # 充值策略激活状态
    GOLDEN_PIG = 'GOLDEN_PIG'                                   # 金猪


class DefaultValues(Enum):
    RECHARGE_TACTICS_INFO = {}                  # 充值策略
    RECHARGE_TACTICS_ACTIVATE = False           # 充值策略激活状态
    GOLDEN_PIG = 99999                          # 金猪


class ValueType(Enum):
    RECHARGE_TACTICS_INFO = 'RECHARGE'          # 充值策略
    RECHARGE_TACTICS_ACTIVATE = 'RECHARGE'      # 充值策略激活状态
    GOLDEN_PIG = 'DRIVE'                        # 金猪


class Types(Enum):
    LOGIN = 'LOGIN'
    RECHARGE = 'RECHARGE'
    DRIVE = 'DRIVE'
