from django.db import models
from three_server.base.model import BaseModel
from announcement.enums.drive import DriveContentType, DriveType


class Drive(BaseModel):
    title = models.CharField(default='', max_length=6, verbose_name='标题')
    icon = models.CharField(default='', max_length=6, verbose_name='图标')
    content_type = models.CharField(default=DriveContentType.TEXT.value, max_length=12, verbose_name='内容类型')
    content = models.TextField(default='', verbose_name='内容')
    drive_type = models.CharField(default=DriveType.NORMAL.value, max_length=12, verbose_name='活动类型')

    @classmethod
    def create_drive(cls, **params):
        cls.objects.create(
            title=params['title'],
            content_type=params['content_type'],
            content=params['content'],
            drive_type=params['drive_type']
        )

    @classmethod
    def delete_drive(cls, d_id):
        try:
            cls.objects.get(id=d_id).delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().values(
            'id',
            'create_at',
            'title',
            'content_type',
            'content',
            'drive_type'
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
            'title',
            'content_type',
            'content'
        ).order_by('-id')
        return ls
