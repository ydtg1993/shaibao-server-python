from announcement.model.drive import Drive


def search_client():
    """
    查询活动列表
    :return:
    """
    result = Drive.search_client()
    return {d['id']: {
        "id": d['id'],
        "title": d['title'],
        "content_type": d['content_type'],
        "content": d['content'],
    } for d in result}
