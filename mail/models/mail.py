from three_server.base.model import BaseModel
from django.db import models
from player.models.player import Player


class Mail(BaseModel):
    mail_type = models.CharField(max_length=24, verbose_name='邮件类型')
    tag = models.CharField(default='', max_length=12, verbose_name='标签')
    title = models.CharField(default='', max_length=24, verbose_name='标题')
    content_type = models.TextField(default='', verbose_name='内容类型')
    content = models.CharField(default='', max_length=124, verbose_name='内容')
    exist_annex = models.BooleanField(default=False, verbose_name='存在附件')
    annex = models.CharField(default='', max_length=1024, verbose_name='附件')

    @classmethod
    def create(cls, **params):
        try:
            obj = cls(
                mail_type=params['mail_type'],
                tag=params['tag'],
                title=params['title'],
                content_type=params['content_type'],
                content=params['content'],
                exist_annex=params['exist_annex'],
            )
            if params['exist_annex']:
                obj.annex = params['annex']
            obj.save()
            return True, obj
        except cls.DoesNotExist:
            return False, None

    @classmethod
    def delete_mail(cls, mail_id):
        try:
            mail = cls.objects.get(id=mail_id)
            mail.delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def search_server(cls, **params):
        ls = cls.objects.filter().values(
            'id',
            'mail_type',
            'tag',
            'title',
            'content_type',
            'content',
            'exist_annex',
            'annex'
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.filter().count()
        return {'total': total, 'ls': ls}


class MailPlayer(BaseModel):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='邮件')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='玩家')
    is_read = models.BooleanField(default=False, verbose_name='是否读取')
    is_receive = models.BooleanField(default=False, verbose_name='是否领取')

    @classmethod
    def create(cls, mail_id, players):
        queryset_list = []
        for player in players:
            queryset_list.append(cls(mail_id=mail_id, player_id=player['id']))
        cls.objects.bulk_create(queryset_list)

    @classmethod
    def search_mail_content(cls, mp_id, player_id):
        try:
            mp = cls.objects.get(id=mp_id, player_id=player_id)
            mp.is_read = True
            mp.save()
            return mp
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_mail(cls, mp_id, player_id):
        try:
            mp = cls.objects.get(id=mp_id, player_id=player_id)
            mp.delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def search_client(cls, **params):
        ls = cls.objects.filter(
            player_id=params['player_id']
        ).values(
            'id',
            'mail__tag',
            'mail__mail_type',
            'mail__title',
            'create_at',
            'mail__exist_annex',
            'is_read',
            'is_receive'
        ).order_by('-id')[
             (int(params['current_page']) - 1) * int(params['page_size']):
             (int(params['current_page']) - 1) * int(params['page_size']) + int(params['page_size'])
        ]
        total = cls.objects.filter(player_id=params['player_id']).count()
        return {'total': total, 'ls': ls}

    @classmethod
    def get_annex(cls, mp_id, player_id):
        try:
            mp = cls.objects.get(
                id=mp_id,
                player_id=player_id,
                is_receive=False
            )
            return mp.mail.annex
        except cls.DoesNotExist:
            return None

    @classmethod
    def set_is_receive(cls, mp_id):
        try:
            mp = cls.objects.get(id=mp_id)
            mp.is_receive = True
            mp.save()
            return True
        except cls.DoesNotExist:
            return False
