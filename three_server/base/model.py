import datetime

from django.contrib.auth.models import User
from django.db import models


class DictMixin:
    """queryset转字典"""
    def to_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), DictMixin):
                d[attr] = getattr(self, attr).to_dict()
            elif isinstance(getattr(self, attr), User):
                d[attr] = getattr(self, attr).username
            else:
                d[attr] = getattr(self, attr)
        return d


class BaseModel(models.Model, DictMixin):
    """model 基类"""
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        default_permissions = ()
