import datetime
import jwt

secret_key = 'secret@tg_tobot'


def encode(user):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
        'user': user
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token.decode('utf-8')


def decode(token):
    try:
        return jwt.decode(token, secret_key,  algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        print("token过期")
    except Exception:
        print("token 无效")

