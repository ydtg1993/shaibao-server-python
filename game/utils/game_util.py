from three_server.celery import app
from player.biz.game_bet import set_lose, set_win, get_win_players
from player.biz.game_bet import sum_win_bonus, sum_bet
from player.biz.public_player import update_player_gold
from hall.biz.game_result import update_bonus_and_bet_count

import logging

log = logging.getLogger('game')


@app.task
def settle_players(sequence, win_types):
    """
    结算玩家
    :param sequence: 期号
    :param win_types: 赢得类型
    :return:
    """
    log.info('settle_players++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    log.info(sequence)
    log.info(win_types)
    log.info('settle_players------------------------------------------------------')
    for player in get_win_players(sequence, win_types):
        update_player_gold(player['player__token'], player['bonus'])


@app.task
def set_bet_record(sequence, win_types):
    """
    设置下注记录
    :param sequence: 期号
    :param win_types: 赢的类型
    :return:
    """
    log.info('set_bet_record++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    log.info(sequence)
    log.info(win_types)
    set_win(sequence, win_types)
    set_lose(sequence, win_types)
    log.info('set_bet_record------------------------------------------------------')


@app.task
def set_bonus_and_bet_count(sequence, win_types):
    """
    设置本期下注金额,开奖金额
    :param sequence: 期号
    :param win_types: 赢的类型
    :return:
    """
    log.info('set_result++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    bonus = sum_win_bonus(sequence, win_types)
    bet_count = sum_bet(sequence)
    update_bonus_and_bet_count(sequence, bonus, bet_count)
    log.info('set_result------------------------------------------------------')
