from django.db import models
from three_server.base.model import BaseModel
from system.enums.keyValue import Keys, DefaultValues, Types, ValueType


class KeyValue(BaseModel):
    key = models.CharField(max_length=64, unique=True, db_index=True, verbose_name='键')
    value = models.TextField(verbose_name='值')
    type = models.CharField(max_length=200, verbose_name='类型')

    @classmethod
    def set_token(cls, data):
        KeyValue.objects.update_or_create(key=data['key'], type=Types.LOGIN.value, defaults={'value': data['value']})

    @classmethod
    def get_token(cls, key):
        try:
            return KeyValue.objects.get(key=key, type=Types.LOGIN.value)
        except KeyValue.DoesNotExist:
            return None

    @classmethod
    def get_value(cls, key):
        try:
            data = cls.objects.get(key=Keys[key].value)
        except cls.DoesNotExist:
            try:
                s_key = Keys[key].value
                d_value = DefaultValues[s_key].value
                d_type = ValueType[s_key].value
                data = cls.objects.create(key=key, value=d_value, type=d_type)
            except KeyError:
                return None
        return data.value

    @classmethod
    def set_value(cls, **data):
        KeyValue.objects.update_or_create(key=data['key'], type=data['type'], defaults={'value': data['value']})

    @classmethod
    def update_value(cls, key, value):
        try:
            obj = cls.objects.get(key=key)
            obj.value = value
            obj.save()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def find_by_type(cls, type):
        ls = cls.objects.filter(type=type).values().order_by('-id')
        return ls
