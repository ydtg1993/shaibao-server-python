from announcement.model.notice import Notice


def search_client():
    """
    客户端获取通知列表
    :return:
    """
    return [d['content'] for d in Notice.search_client()]
