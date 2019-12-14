from django.core.cache import cache


prefix = 'player_'


def set_player_hall(key, value):
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        cache.delete(u_key)
    cache.set(u_key, value)


def get_player_hall(key):
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        return cache.get(u_key)
    return None
