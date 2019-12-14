from django.core.cache import cache


#  缓存手机验证码
def set_code(key, value):
    if cache.has_key(key):
        return False
    cache.set(key, value, 60)
    return True


#  缓存中取手机验证码
def get_code(key):
    if cache.has_key(key):
        phone_key = cache.get(key)
        cache.delete(key)
        return phone_key
    return None
