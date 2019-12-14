import random

from three_server.base.result import ResultCode, ResultMsg
from django.http.response import JsonResponse
from three_server.forms.client_auth import ClientLoginForm, ClientRegisteredForm, ClientResetPasswordForm, SendCodeForm
import json
import re
from player.biz.client_player import login, registered, reset_password
from system.cache.verification_code import set_code, get_code

import logging
log = logging.getLogger('game')


def client_login(request):
    """
    @api {post} /auth/client/login 登录
    @apiVersion 1.0.0
    @apiName login
    @apiGroup Player
    @apiParam (参数) {String} phone 手机号
    @apiParam (参数) {String} password 密码
    @apiSuccessExample {json} 返回样例:
    {
        "code": 20000,
        "message": "Succeed",
        "data": {
            "serial": "1566365805",
            "avatar": "",
            "name": "1566365805",
            "phone": "1566365805",
            "gold": "0.00",
            "token": "43ab1e62-c3e8-11e9-9331-4cedfbc56de4"
        }
    }
    """
    if request.body.decode() is None or request.body.decode() is '':
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    form = ClientLoginForm(json.loads(request.body.decode()))
    log.info(form.data)
    if not form.is_valid():
        log.info(form.errors)
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    ok = re.match(r"^1[35678]\d{9}$", form.data['phone'])
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_40007.value, 'message': ResultMsg.MSG_40007.value})
    ok, data = login(form.data['phone'], form.data['password'])
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_50000.value, 'message': ResultMsg.MSG_50000.value})
    if data is None:
        return JsonResponse({'code': ResultCode.CODE_60000.value, 'message': ResultMsg.MSG_60000.value})
    return JsonResponse({'code': ResultCode.CODE_20000.value, 'data': data, 'message': ResultMsg.MSG_20000.value})


def client_registered(request):
    """
    @api {post} /auth/client/registered 注册
    @apiVersion 1.0.0
    @apiName registered
    @apiGroup Player
    @apiParam (参数) {String} phone 手机号
    @apiParam (参数) {String} code 短信验证码
    @apiParam (参数) {String} password 密码
    @apiParam (参数) {String} invite_code 邀请码
    @apiSuccessExample {json} 返回样例:
    {
        "code": 20000,
        "message": "Succeed",
        "data": {
            "serial": "1566365805",
            "avatar": "",
            "name": "1566365805",
            "phone": "1566365805",
            "gold": "0.00",
            "token": "43ab1e62-c3e8-11e9-9331-4cedfbc56de4"
        }
    }
    """
    if request.body.decode() is None or request.body.decode() is '':
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    form = ClientRegisteredForm(json.loads(request.body.decode()))
    log.info(form.data)
    if not form.is_valid():
        log.info(form.errors)
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    #  验证短信验证码
    ok = re.match(r"^1[35678]\d{9}$", form.data['phone'])
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_40007.value, 'message': ResultMsg.MSG_40007.value})
    cache_code = get_code(form.data['phone'])
    if cache_code != form.data['code']:
        return JsonResponse({'code': ResultCode.CODE_40006.value, 'message': ResultMsg.MSG_40006.value})
    invite_code = form.data['invite_code'] if 'invite_code' in form.data else ''
    ok, result = registered(form.data['phone'], form.data['password'], invite_code)
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_50000.value, 'message': ResultMsg.MSG_50000.value})
    return JsonResponse({'code': ResultCode.CODE_20000.value, 'data': result, 'message': ResultMsg.MSG_20000.value})


def client_reset_password(request):
    """
    @api {post} /auth/client/reset_password 重置密码
    @apiVersion 1.0.0
    @apiName reset_password
    @apiGroup Player
    @apiParam (参数) {String} phone 手机号
    @apiParam (参数) {String} code 短信验证码
    @apiParam (参数) {String} password 密码
    @apiSuccessExample {json} 返回样例:
    {
        "code": 20000,
        "message": "Succeed",
        "data": {
            "serial": "1566365805",
            "avatar": "",
            "name": "1566365805",
            "phone": "1566365805",
            "gold": "0.00",
            "token": "43ab1e62-c3e8-11e9-9331-4cedfbc56de4"
        }
    }
    """
    if request.body.decode() is None or request.body.decode() is '':
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    form = ClientResetPasswordForm(json.loads(request.body.decode()))
    log.info(form.data)
    if not form.is_valid():
        log.info(form.errors)
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    #  验证短信验证码
    cache_code = get_code(form.data['phone'])
    if cache_code != form.data['code']:
        return JsonResponse({'code': ResultCode.CODE_40006.value, 'message': ResultMsg.MSG_40006.value})
    ok, result = reset_password(form.data['phone'], form.data['password'])
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_50000.value, 'message': ResultMsg.MSG_50000.value})
    if result is None:
        return JsonResponse({'code': ResultCode.CODE_40008.value, 'message': ResultMsg.MSG_40008.value})
    return JsonResponse({'code': ResultCode.CODE_20000.value, 'data': result, 'message': ResultMsg.MSG_20000.value})


def send_code(request):
    """
    @api {post} /auth/client/send_code 发送验证码
    @apiVersion 1.0.0
    @apiName send_code
    @apiGroup Player
    @apiParam (参数) {String} phone 手机号
    @apiSuccessExample {json} 返回样例:
    {
        "code": 20000,
        "message": "Succeed",
        "data": "3993"
    }
    """
    if request.body.decode() is None or request.body.decode() is '':
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    form = SendCodeForm(json.loads(request.body.decode()))
    log.info(form.data)
    if not form.is_valid():
        log.info(form.errors)
        return JsonResponse({'code': ResultCode.CODE_40003.value, 'message': ResultMsg.MSG_40003.value})
    ok = re.match(r"^1[35678]\d{9}$", form.data['phone'])
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_40007.value, 'message': ResultMsg.MSG_40007.value})
    code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    log.info('验证码：【%s】' % code)
    ok = set_code(form.data['phone'], code)
    if not ok:
        return JsonResponse({'code': ResultCode.CODE_40009.value, 'message': ResultMsg.MSG_40009.value})
    return JsonResponse({'code': ResultCode.CODE_20000.value, 'data': code, 'message': ResultMsg.MSG_20000.value})
