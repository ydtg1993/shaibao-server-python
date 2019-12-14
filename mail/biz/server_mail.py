from mail.enums.mail import MailType, MailTypeMsg
from mail.enums.mail import MailContentType, MailContentMsg
from mail.enums.mail import AnnexType, AnnexTypeMsg
from mail.models.mail import Mail, MailPlayer
from player.models.player import Player


def content_types():
    """
    获取邮件内容类型
    :return:
    """
    return [{
        'label': MailContentMsg[t.value].value,
        'value': t.value
    } for t in MailContentType]


def mail_types():
    """
    获取邮件类型
    :return:
    """
    return [{
        'label': MailTypeMsg[t.value].value,
        'value': t.value
    } for t in MailType]


def annex_types():
    """
    获取附件类型
    :return:
    """
    return [{
        'label': AnnexTypeMsg[t.value].value,
        'value': t.value
    } for t in AnnexType]


def create_mail(**params):
    """
    创建邮件
    :param params: Map
    :return:
    """
    # 创建邮件
    ok, mail = Mail.create(**params)
    if not ok:
        print('创建失败')
    # 群发还是私发
    if params['mail_type'] == MailType.SYSTEM_MAIL.value:
        players = Player.all_player_id()
    else:
        players = Player.find_by_serial(params['player_ids'])
    MailPlayer.create(mail.id, players)


def search(**params):
    """
    查询邮件列表
    :param params:
    :return:
    """
    result = Mail.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'mail_type': MailTypeMsg[d['mail_type']].value,
        'tag': d['tag'],
        'title': d['title'],
        'content_type': MailContentMsg[d['content_type']].value,
        'content': d['content'],
        'exist_annex': d['exist_annex'],
        'annex': d['annex']
    } for d in result['ls']]
    return result


def delete_mail(mail_id):
    """
    删除邮件
    :param mail_id:
    :return:
    """
    Mail.delete_mail(mail_id)
