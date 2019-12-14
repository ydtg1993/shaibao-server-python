from finance.models.withdraw import Withdraw
from finance.enums.withdraw import WithdrawStatusEnum


def search_server(**params):
    """
    客户端查询
    :param params:
    :return:
    """
    result = Withdraw.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'player_serial': d['player__serial'],
        'player_name': d['player__name'],
        'create_at': d['create_at'].strftime("%Y-%m-%d %H:%M:%S"),
        'amount': d['amount'],
        'status': d['status'],
        'reviewer_id': d['reviewer_id'],
        'reviewer_name': d['reviewer__username']
    } for d in result['ls']]
    return result


def check(**params):
    """
    添加申请
    :param params:
    :return:
    """
    if params['allow'] == WithdrawStatusEnum.SUCCEED.value:
        return Withdraw.check_withdraw(**params)
    elif params['allow'] == WithdrawStatusEnum.FAILED.value:
        return Withdraw.check_withdraw(**params)
    return False
