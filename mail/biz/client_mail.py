from decimal import Decimal

from mail.models.mail import Mail, MailPlayer
from ast import literal_eval
from mail.enums.mail import AnnexType


def search_client(**params):
    """
    客户端查询邮件列表
    :param params:
    :return:
    """
    result = MailPlayer.search_client(**params)
    result['ls'] = [{
        'id': d['id'],
        'tag': d['mail__tag'],
        'title': d['mail__title'],
        'create_at': d['create_at'].strftime("%Y/%m/%d %H:%M:%S"),
        'exist_annex': d['mail__exist_annex'],
        'is_read': d['is_read'],
        'is_receive': d['is_receive']
    } for d in result['ls']]
    return result


def search_content(mp_id, player_id):
    """
    查看邮件内容
    :param mp_id: 邮件玩家链表ID
    :param player_id: 玩家ID
    :return:
    """
    mp = MailPlayer.search_mail_content(mp_id, player_id)
    print(mp)
    if mp is None:
        return None
    annex_ls = [] if mp.mail.annex == '' or mp.mail.annex is None else literal_eval(mp.mail.annex)
    annex = {
        'type': annex_ls[0]['annex_type'],
        'value': annex_ls[0]['annex_value']
    } if len(annex_ls) > 0 else {}
    return {
        "id": mp.id,
        "content_type": mp.mail.content_type,
        "content": mp.mail.content,
        "annex": annex,
        "is_receive": mp.is_receive,
        "exist_annex": mp.mail.exist_annex
    }


def delete_mail(mp_id, player_id):
    """
    删除关联关系
    :param mp_id: 邮件玩家链表ID
    :param player_id: 玩家ID
    :return:
    """
    MailPlayer.delete_mail(mp_id, player_id)


def get_annex_gold(mp_id, player_id):
    """
    获取附件金币
    :param mp_id:
    :param player_id:
    :return:
    """
    annex = MailPlayer.get_annex(mp_id, player_id)
    if annex is None:
        return None
    array_annex = [] if annex == '' or annex is None else literal_eval(annex)
    x = Decimal(0)
    for a in array_annex:
        if a['annex_type'] == AnnexType.GOLD.value:
            x += Decimal(a['annex_value'])
    return x


def set_is_receive(mp_id):
    """
    设置为已接受
    :param mp_id:
    :return:
    """
    MailPlayer.set_is_receive(mp_id)
