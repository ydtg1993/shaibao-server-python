from django.db import models
from three_server.base.model import BaseModel


class Notice(BaseModel):
    content = models.TextField(default='', verbose_name='内容')

    @classmethod
    def create(cls, content):
        cls.objects.create(
            content=content
        )

    @classmethod
    def delete_notice(cls, n_id):
        try:
            cls.objects.get(id=n_id).delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().values(
            'id',
            'create_at',
            'content',
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
         ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}

    @classmethod
    def search_client(cls):
        ls = cls.objects.filter().values(
            'id',
            'content'
        ).order_by('-id')
        return ls
