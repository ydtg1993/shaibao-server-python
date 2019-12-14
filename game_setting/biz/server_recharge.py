import json
from game_setting.enums.recharge import RechargeMethod, RechargeMethodMsg
from game_setting.enums.recharge import RechargeType, RechargeTypeMsg
from system.models.keyValue import KeyValue
from system.enums.keyValue import Keys, Types
from django_celery_beat.models import ClockedSchedule, PeriodicTask


def methods():
    return [{
        'label': RechargeMethodMsg[d.value].value,
        'value': d.value,
    } for d in RechargeMethod]


def types():
    return [{
        'label': RechargeTypeMsg[d.value].value,
        'value': d.value,
    } for d in RechargeType]


def switch():
    activate = KeyValue.get_value(Keys.RECHARGE_TACTICS_ACTIVATE.value)
    activate = False if activate == str(True) else True
    KeyValue.set_value(
        key=Keys.RECHARGE_TACTICS_ACTIVATE.value,
        type=Types.RECHARGE.value,
        value=activate,
    )


def info():
    obj_info = KeyValue.get_value(Keys.RECHARGE_TACTICS_INFO.value)
    obj_activate = KeyValue.get_value(Keys.RECHARGE_TACTICS_ACTIVATE.value)
    return {
        "activate": obj_activate == str(True),
        "info": {} if obj_info is None else json.loads(obj_info)
    }


def create(value):
    KeyValue.set_value(
        key=Keys.RECHARGE_TACTICS_INFO.value,
        type=Types.RECHARGE.value,
        value=value
    )


def test():
    clocked = ClockedSchedule.objects.get_or_create(
        clocked_time='',
        enabled=True
    )
    PeriodicTask.objects.create(
        name='open_',
        task='proj.tasks.add',
        args=json.dumps([]),
        kwargs=json.dumps({}),
        headers=json.dumps({}),
        one_off=True,
        enabled=True,
        clocked=clocked
    )
