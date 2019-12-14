from enum import Enum


class NoticeEvent(Enum):
    EnterNotice = 'EnterNotice'                          # 进入房间通知
    GameStartNotice = 'GameStartNotice'                  # 开始游戏通知
    StartBetNotice = 'StartBetNotice'                    # 下注阶段通知
    GameLotteryNotice = 'GameLotteryNotice'              # 开奖阶段通知
    GameLotteryResultNotice = 'GameLotteryResultNotice'  # 开奖结果通知
    GameSettleNotice = 'GameSettleNotice'                # 结算阶段通知
    GameOverNotice = 'GameOverNotice'                    # 结束阶段通知
    GameBetErrorNotice = 'GameBetErrorNotice'            # 下注失败通知
    GameBetSuccessNotice = 'GameBetSuccessNotice'        # 下注成功通知
    WinningNotice = 'WinningNotice'                      # 玩家中奖通知
    UpdatePlayerInfoNotice = 'UpdatePlayerInfoNotice'    # 更新玩家信息


class NoticeEventMsg(Enum):
    EnterNotice = '进入房间通知'                    # 进入房间通知
    GameStartNotice = '开始游戏通知'                # 开始游戏通知
    StartBetNotice = '下注阶段通知'                 # 下注阶段通知
    GameLotteryNotice = '开奖阶段通知'              # 开奖阶段通知
    GameLotteryResultNotice = '开奖结果通知'        # 开奖结果通知
    GameSettleNotice = '结算阶段通知'               # 结算阶段通知
    GameOverNotice = '结束阶段通知'                 # 结束阶段通知
    GameBetErrorNotice = '下注失败通知'             # 下注失败通知
    GameBetSuccessNotice = '下注成功通知'           # 下注成功通知
    WinningNotice = '玩家中奖通知'                  # 玩家中奖通知
    UpdatePlayerInfoNotice = '更新玩家通知'         # 更新玩家信息
