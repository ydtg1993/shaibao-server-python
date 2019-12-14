import time
from three_server.utils.encrypt import md5
from player.models.player import Player


def login(phone, password):
    """
    登陆验证
    :param phone: 手机号
    :param password: 密码
    :return: 是否成功， 玩家对象
    """
    ok, obj = Player.authenticate(phone, md5(password))
    return ok, response_obj(obj)


def registered(phone, password, code):
    """
    注册
    :param phone: 手机号
    :param password: 密码
    :param code: 邀请注册码
    :return: 是否成功， 玩家对象
    """
    serial = str(int(time.time()))
    ok, obj = Player.create(serial, md5(password), phone, code)
    return ok, response_obj(obj)


def reset_password(phone, new_password):
    """
    重置密码
    :param phone: 手机号
    :param new_password: 新密码
    :return:
    """
    ok, obj = Player.reset_password(phone, md5(new_password))
    return ok, response_obj(obj)


def get_player_gold(player_id):
    pass


def auth_token(token):
    """
    验证Token
    :param token:
    :return: 成功 Boolean
    """
    return Player.check_token(token)


def reset_token(token):
    """
    重置Token
    :param token: token
    :return: 成功 Boolean
    """
    return Player.reset_token(token)


def response_obj(obj):
    return None if obj is None else {
        'name': obj.name,
        'avatar': obj.avatar,
        'serial': obj.serial,
        'gold': obj.gold,
        'token': obj.token,
        'phone': obj.phone
    }


def find_by_token(token):
    """
    根据token获取用户
    :param token:
    :return:
    """
    return Player.find_by_token(token)
