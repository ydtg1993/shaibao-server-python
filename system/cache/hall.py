from django.core.cache import cache


prefix = 'hall_'
out_time = 60 * 6


def set_hall_tag(key, value):
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        cache.delete(u_key)
    cache.set(u_key, value, out_time)


def get_hall_tag(key):
    u_key = '%s%s' % (prefix, key)
    if cache.has_key(u_key):
        return cache.get(u_key)
    return None