from enum import Enum


class BetStatus(Enum):
    DEFAULT = 0  # 默认
    WIN = 1      # 赢
    LOSE = -1    # 输


class PlayerStatus(Enum):
    DEFAULT = 0  # 默认
    WIN = 1      # 赢
    LOSE = -1    # 输
