from announcement.model.drive import Drive
from announcement.enums.drive import DriveType, DriveTypeMsg
from announcement.enums.drive import DriveContentType, DriveContentTypeMsg


def create_drive(**params):
    """
    创建活动
    :param params: 活动参数
    :return:
    """
    Drive.create_drive(**params)


def search_server(**params):
    """
    查询活动列表
    :param params:
    :return:
    """
    result = Drive.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'create_at': d['create_at'].strftime("%Y/%m/%d %H:%M:%S"),
        'title': d['title'],
        'content_type': DriveContentTypeMsg[d['content_type']].value,
        'content': d['content'],
        'drive_type': DriveTypeMsg[d['drive_type']].value
    } for d in result['ls']]
    return result


def remove(d_id):
    """
    删除活动公告
    :param d_id:
    :return:
    """
    return Drive.delete_drive(d_id)


def drive_type():
    """
    获取活动类型
    :return:
    """
    return [{
        'label': DriveTypeMsg[d.value].value,
        'value': d.value
    } for d in DriveType]


def drive_content_type():
    """
    获取活动内容类型
    :return:
    """
    return [{
        'label': DriveContentTypeMsg[d.value].value,
        'value': d.value
    } for d in DriveContentType]
