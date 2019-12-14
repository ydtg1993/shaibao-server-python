from hall.models.hall import Result
from three_server.utils.time import get_now


def search(hall_tag):
    """
    获取大厅开奖记录
    :param hall_tag: 大厅标识
    :return:
    """
    return [{
        'id': r['id'],
        'sequence': r['sequence'].split('-')[1][-4:],
        'result': ''.join([str(i) for i in eval(r['result'])]),
        'big': r['big'],
        'even': r['even'],
        'sum': r['sum']
    } for r in Result.search_client(hall_tag, get_now())]
