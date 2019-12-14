from django.utils.deprecation import MiddlewareMixin
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from three_server.utils import token
from system.models.keyValue import KeyValue
from player.models.player import Player
from three_server.base.result import ResultCode, ResultMsg


class AuthTokenMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        if '/api' in request.path:
            # 客户端校验
            if request.META.get('HTTP_AUTHORIZATION', '').startswith('Token'):
                if not hasattr(request, 'user') or request.user.is_anonymous():
                    try:
                        key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                        payload = token.decode(key)
                        if payload is None:
                            return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                        db_token = KeyValue.get_token(payload['user']['id'])
                        if db_token is None:
                            return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                        if key != db_token.value:
                            return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                        pk = payload['user']['id']
                        user = User.objects.get(id=pk)
                        KeyValue.get_token(user.id)
                        request.user = request._cached_user = user
                    except User.DoesNotExist:
                        return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                    except IndexError:
                        return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
            else:
                return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
        elif '/three' in request.path:
            # 客户端校验
            if request.META.get('HTTP_AUTHORIZATION', '').startswith('Token'):
                if not hasattr(request, 'user') or request.user.is_anonymous():
                    try:
                        key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                        pass
                        ok, player = Player.find_by_token(key)
                        if not ok:
                            return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                        request.player = player
                    except Player.DoesNotExist:
                        return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
                    except IndexError:
                        return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})
            else:
                return JsonResponse({'code': ResultCode.CODE_40001.value, 'message': ResultMsg.MSG_40001.value})


