from __future__ import absolute_import, unicode_literals
from celery import Celery, platforms
import os

import logging

log = logging.getLogger('game')

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'three_server.settings')
platforms.C_FORCE_ROOT = True

# 创建应用
app = Celery('three_server')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))
