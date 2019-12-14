from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from system.models.keyValue import KeyValue
from three_server.forms.login import LoginForm
from three_server.utils import token
from three_server.base.result import ResultCode, ResultMsg
import json


def login(request):
    print(request.body)
    form = LoginForm(json.loads(request.body.decode()))
    if form.is_valid():
        user = authenticate(username=form.data["username"], password=form.data["password"])
        if user:
            user_info = {'id': user.id, 'username': user.username}
            key = token.encode(user_info)
            KeyValue.set_token({'key': user.id, 'value': key})
            result = {'token': key, 'user_info': {'id': user.id, 'username': user.username}}
            return JsonResponse({
                'code': ResultCode.CODE_20000.value, 'message': ResultMsg.MSG_20000.value,
                'data': result
            })
        else:
            return JsonResponse({'code': ResultCode.CODE_60000.value, 'message': ResultMsg.MSG_60000.value})
    else:
        return JsonResponse({'code': ResultCode.CODE_40000.value, 'message': ResultMsg.MSG_40000.value})


def logout(request):
    user_id = request.GET.get('user_id')
    if user_id is None:
        return JsonResponse({'code': ResultCode.CODE_40000.value, 'message': ResultMsg.MSG_40000.value})
    KeyValue.set_token({'key': user_id, 'value': ""})
    return JsonResponse({'code': ResultCode.CODE_20000.value, 'message': ResultMsg.MSG_20000.value})
