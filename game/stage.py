from __future__ import absolute_import, unicode_literals
import time
from three_server.celery import app
from three_server.utils.dice import create_result

from hall.biz.public_result import get_hall_next_sequence, get_hall_new_sequence
from hall.biz.game_result import set_result, init_result
from hall.biz.game_hall import next_hall_stage, update_lottery_time, get_hall_bet_second

from player.biz.game_bet import get_win_players

from datetime import datetime, timedelta

from game.notice.notice import start_notice, bet_notice, lottery_notice, lottery_result_notice
from game.notice.notice import settle_notice, winning_notice, over_notice
from game.utils.game_util import settle_players, set_bet_record, set_bonus_and_bet_count

import logging

log = logging.getLogger('game')


@app.task
def game_time():
    log.info('////////////////////////////////////////////////////////////////////////////////////')
    log.info('定时任务。。。')
    log.info('////////////////////////////////////////////////////////////////////////////////////')


@app.task
def start_stage(hall_id, hall_tag):
    """开始阶段"""
    log.info('////////////////////////////////////////////////////////////////////////////////////')
    log.info('//////////////////////////////////////游戏开始//////////////////////////////////////')
    log.info('////////////////////////////////////////////////////////////////////////////////////')
    log.info("开始阶段>")
    # 设置
    # set_hall_tag(hall_id, hall_tag)
    # 初始化一个开奖结果
    sequence = get_hall_next_sequence(hall_id, hall_tag)
    init_result(hall_id, sequence)
    # 获取大厅下注秒数
    bet_second = get_hall_bet_second(hall_id)
    log.info("大厅下注时间【%d】" % bet_second)
    # 更新开奖时间
    lottery_time = (datetime.now() + timedelta(seconds=bet_second))
    log.info(lottery_time)
    update_lottery_time(hall_id, lottery_time)
    # 通知游戏开始
    start_notice(hall_id, hall_tag, sequence)

    # 切换为下注阶段
    next_hall_stage(hall_id)
    log.info("下注阶段>")
    # # 通知进入下注阶段
    bet_notice(hall_tag, lottery_time, bet_second)
    # 大厅切换阶段
    # 下注时间 bet_second
    bet_stage.apply_async((hall_id, hall_tag), countdown=bet_second)


@app.task
def bet_stage(hall_id, hall_tag):
    """下注阶段"""
    # 切换为开奖阶段
    next_hall_stage(hall_id)
    # 进入开奖阶段
    lottery_stage.delay(hall_id, hall_tag)


@app.task
def lottery_stage(hall_id, hall_tag):
    """开奖阶段"""
    # log.info("--------------------------开奖阶段--------------------------")
    log.info("开奖阶段>")
    # 进入开奖阶段通知
    lottery_notice(hall_tag)
    # 获取开奖结果
    result = create_result()
    # 设置当前开奖结果
    seq = get_hall_new_sequence(hall_id, hall_tag)
    log.info(result)
    # TODO 这个时候已经可以开始结算用户了
    settle_players.delay(seq, result['wins'])
    set_bonus_and_bet_count.delay(seq, result['wins'])
    # 等待五秒前端动画
    time.sleep(5)
    # 开奖结果通知
    lottery_result_notice(hall_tag, result)
    # 存储开奖结果
    set_result(seq, result['result'])
    # 切换大厅状态
    next_hall_stage(hall_id)
    # 进入结算阶段
    # settle_stage.delay(hall_id, hall_tag, result['wins'])
    settle_stage.apply_async((hall_id, hall_tag, result['wins']), countdown=5)


@app.task
def settle_stage(hall_id, hall_tag, win_types):
    """结算阶段"""
    # log.info("--------------------------结算阶段--------------------------")
    log.info("结算阶段>")
    # 通知进入结算阶段
    settle_notice(hall_tag)
    # 获取最新期号
    seq = get_hall_new_sequence(hall_id, hall_tag)
    # 获取赢家
    win_players = get_win_players(seq, win_types)
    # 发送中奖通知
    winning_notice(win_players, hall_tag, win_types)
    # TODO 异步设置输家,赢家
    set_bet_record.delay(seq, win_types)
    # 切换为结束阶段
    next_hall_stage(hall_id)
    over_stage.apply_async((hall_id, hall_tag), countdown=5)


@app.task
def over_stage(hall_id, hall_tag):
    """结束阶段"""
    log.info("结束阶段")
    # 通知进入结束阶段
    over_notice(hall_tag)
    # 切换开始阶段
    if next_hall_stage(hall_id):
        start_stage.delay(hall_id, hall_tag)
    # over_stage.apply_async((hall_id, hall_tag), countdown=10)
    log.info('////////////////////////////////////////////////////////////////////////////////////')
    log.info('//////////////////////////////////////游戏结束//////////////////////////////////////')
    log.info('////////////////////////////////////////////////////////////////////////////////////')
