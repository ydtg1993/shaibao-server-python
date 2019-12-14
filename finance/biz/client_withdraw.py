from finance.models.withdraw import Withdraw


def search_client(**params):
    """
    客户端查询
    :param params:
    :return:
    """
    result = Withdraw.search_client(**params)
    result['ls'] = [{
        'sequence': d['id'],
        'create_at': d['create_at'].strftime("%Y-%m-%d"),
        'amount': d['amount'],
        'status': d['status'],
    } for d in result['ls']]
    return result


def add(**params):
    """
    添加申请
    :param params:
    :return:
    """
    Withdraw.add(**params)
