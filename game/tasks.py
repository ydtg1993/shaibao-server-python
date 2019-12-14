from __future__ import absolute_import,unicode_literals
from celery import shared_task

import logging
log = logging.getLogger('game')


@shared_task
def add(x, y):
    log.info('定时任务加法。。。')
    return x+y


@shared_task
def sub(x, y):
    log.info('定时任务减法。。。')
    return x-y
