from django.core.cache import cache

prefix = 'channel_'


#  缓存连接名
def set_channel_name(key, value):
    u_key = '%s%s' % (prefix, key)
    u_value = '%s%s' % (prefix, value)
    if cache.has_key(u_key):
        cache.delete(u_key)
    if cache.has_key(u_value):
        cache.delete(u_value)
    cache.set(u_key, value,)
    cache.set(u_value, key)
    return True


#  缓存连接名
def get_channel_name(key):
    """
    获取Player连接名
    :param key: Player Token
    :return: 连接名
    """
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        return cache.get(u_key)
    return None


def get_player_token(key):
    """
    获取Player Token
    :param key: Player 连接名
    :return: Player Token
    """
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        return cache.get(u_key)
    return None


#  删除缓存连接名
def del_channel_name(key, value):
    u_key = '%s%s' % (prefix, key)
    u_value = '%s%s' % (prefix, value)
    if cache.has_key(u_key):
        cache.delete(u_key)
    if cache.has_key(u_value):
        cache.delete(u_value)
    return True
