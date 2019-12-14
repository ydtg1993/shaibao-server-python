import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, FileResponse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q, QuerySet
from django.db.models import Model


class HttpStatus:
    """
        状态码约定：
        200~299：请求成功的状态
        400~499：为客户端提交的引起的错误
        500~599: 为服务端处理异常
        自定义业务的状态码：请冲210开始自定义
        http 默认的予以保留：如404，200 等等
        http status 参考表： http://tool.oschina.net/commons?type=5
    """
    # 以重复
    HTTP_300 = 300
    #
    HTTP_301 = 301
    # 成功
    HTTP_200 = 200
    # 登良错误, token 失效
    HTTP_400 = 400
    # 没有权限
    HTTP_401 = 401
    # 提交的数据不符合要求，拒绝访问
    HTTP_403 = 403
    # 资源不存在
    HTTP_404 = 404
    # 服务器错误
    HTTP_500 = 500


class BaseController(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.http_method_names = ['get', 'post', 'put', 'delete']
        self.render = render
        self.queryset = None
        self.model_form = None
        self.init()

    def init(self):
        """
        Hook: 初始化 queryset, model_form
        :return:
        """
        pass

    def get_token(self):
        try:
            header = self.request.META.get('HTTP-AUTHORIZATION')
        except:
            try:
                header = self.request.META.get('AUTHORIZATION')
            except:
                return None
        arr = header.split(' ')
        if len(arr) == 2:
            return arr[1]
        else:
            raise Exception("无效authorization信息")

    def body_data(self):
        if '{' not in str(self.request.body):
            return {}
        if self.request.body == b'':
            return {}
        return json.loads(self.request.body.decode())

    def get_argument(self, key):
        return self.request.GET.get(key)

    def get_arguments(self):
        return {key: self.request.GET.get(key) for key in dict(self.request.GET)}

    def dispatch(self, request, *args, **kwargs):
        try:
            action = kwargs["action"]
        except:
            action = None
        if action is None:
            method = request.method.lower()
            if method not in self.http_method_names:
                raise Exception("不支持的请求方式")
            handler = getattr(self, method)
        else:
            try:
                handler = getattr(self, action)
            except NotImplemented:
                return Http404("没有实现")
        return handler()

    def json(self, code=HttpStatus.HTTP_200, data=None, message=''):
        """
        :param code: HttpStatus 状态码
        :param data: 数据，支持子类型，字典类型，QuerySet(values), Model.
        :param message: 返回的信息
        :return: 返回applicaiton/json
        """
        # charset = 'GBK' if 'Safari' in self.request.META.get('HTTP_USER_AGENT') else 'UTF-8'
        return JsonResponse(
            {
                "code": code,
                "data": data,
                "message": message
            },
            encoder=CustomJSONEncoder,
            json_dumps_params={'ensure_ascii': False},
            content_type='application/json;charset=UTF-8',
            # charset=charset
        )

    def download(self, file):
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="models.txt"'
        return response

    def get(self):
        if self.queryset is None:
            raise Exception("没有指定model")
        pk = self.kwargs["id"]
        if pk is None:
            data = self.get_list()
        else:
            data = self.get_one(pk)
        return self.json(200, data)

    def get_list(self):
        """
        hook: 子类可以覆盖该方法，获取返回列表
        :return:
        """
        query_params = Q()
        for k, v in self.request.GET.items():
            if v is None or len(v) == 0:
                continue
            q = {}
            q[k] = v
            query_params.add(Q(**q), Q.AND)
        data = self.queryset.filter(query_params).values()
        return data

    def get_one(self, pk):
        """
        hook: 子类可以覆盖 该方法获取一个某一个具体实例
        :param pk: 主键
        :return:
        """
        model = self.queryset.get(id=pk)
        return pk

    def post(self):
        json_data = json.loads(self.request.body)
        form = self.model_form(json_data)
        if form.is_valid():
            instance = form.save(commit=False)
            if self.kwargs["id"] is not None:
                instance.id = self.kwargs["id"]
            instance.save()
            return self.json(200, message='success')
        else:
            return self.json(401, message=form.errors.as_json())

    def delete(self):
        pk = self.kwargs['id']
        self.queryset.get(id=pk).delete()
        return self.json(200, message='success')


class CustomJSONEncoder(DjangoJSONEncoder):
    """
    自定义序列化类
    """

    def default(self, o):
        result = None
        if isinstance(o, Model):
            result = o.to_dict()
        elif isinstance(o, QuerySet):
            try:
                result = [item.to_dict() for item in o]
            except:
                try:
                    return list(o)
                except:
                    raise Exception("{0} 无法序列化".format(type(o)))
        else:
            result = super().default(o)
        return result