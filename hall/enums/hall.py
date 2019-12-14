from enum import Enum


class HallStage(Enum):
    StartStage = 'StartStage'      # 开始阶段
    BetStage = 'BetStage'          # 下注阶段
    LotteryStage = 'LotteryStage'  # 开奖阶段
    SettleStage = 'SettleStage'    # 结算阶段
    OverStage = 'OverStage'        # 结束阶段


class HallTag(Enum):
    Fast = 'Fast'                  # 极速快三
    OneMinute = 'OneMinute'        # 一分快三
    FivesMinute = 'FivesMinute'    # 五分快三


class HallTagMsg(Enum):
    Fast = '极速快三'           # 极速快三
    OneMinute = '一分快三'      # 一分快三
    FivesMinute = '五分快三'    # 五分快三


class LotteryType(Enum):
    Self = 'Self'          # 自营
    External = 'External'  # 外部


class LotteryTypeMsg(Enum):
    Self = '自营'  # 自营
    External = '外接'  # 外部



