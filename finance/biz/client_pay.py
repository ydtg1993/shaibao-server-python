from finance.models.fast_account import FastAccount
from finance.models.bank_account import BankAccount
from finance.models.recharge_record import RechargeRecord
from finance.enums.pay_type import PayTypeMsg, PayType


def pay_method():
    result = {}
    fast_account = FastAccount.get_active_account()
    if fast_account is None:
        result['fast'] = {}
    else:
        result['fast'] = {
            'id': fast_account.id,
            'name': fast_account.account_name,
            'number': fast_account.account_number,
            'qr_code': fast_account.qr_code,
        }
    result['banks'] = {d['id']: {
        'id': d['id'],
        'bank_name': d['bank_name'],
        'interval': '%d-%d' % (d['amount_min'], d['amount_max']),
        'name': d['user_name'],
        'number': d['number'],
    } for d in BankAccount.search_client()}
    return result


def to_pay(**params):
    if params['pay_type'] == PayType.fast.value:
        fa = FastAccount.get_active_account()
        if fa is None:
            return False
        RechargeRecord.add(
            player_id=params['player_id'],
            depositor=params['player_name'],
            pay_money=params['pay_money'],
            type=PayType.fast.value,
            payee=fa.account_name,
            account_id=fa.id,
        )
        return True
    if params['pay_type'] == PayType.bank.value:
        ba = BankAccount.find_by_id(params['account_id'])
        if ba is None:
            return False
        RechargeRecord.add(
            player_id=params['player_id'],
            depositor=params['player_name'],
            pay_money=params['pay_money'],
            type=PayType.bank.value,
            payee=ba.user_name,
            account_id=ba.id,
        )
        return True


def record(**params):
    result = RechargeRecord.search_client(**params)
    result['ls'] = [{
        'id': d['id'],
        'type': PayTypeMsg[d['type']].value,
        'pay_money': d['pay_money'],
        'create_at': d['create_at'].strftime("%Y.%m.%d"),
        'status': d['status'],
    } for d in result['ls']]
    return result
