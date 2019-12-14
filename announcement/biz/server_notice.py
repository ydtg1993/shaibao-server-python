from announcement.model.notice import Notice


def create_notice(content):
    """
    通知内容
    :param content:
    :return:
    """
    Notice.create(content)


def remove_notice(n_id):
    """
    通知ID
    :param n_id:
    :return:
    """
    Notice.delete_notice(n_id)


def search_server(**params):
    """
    获取通知列表
    :return:
    """
    result = Notice.search_server(**params)
    result['ls'] = [{
        'create_at': d['create_at'].strftime("%Y/%m/%d %H:%M:%S"),
        'content': d['content']
    } for d in result['ls']]
    return result
