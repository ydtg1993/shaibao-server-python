from finance.models.bank_account import BankAccount


def search(**params):
    result = BankAccount.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'create_at': d['create_at'],
        'bank_name': d['bank_name'],
        'number': d['number'],
        'user_name': d['user_name'],
        'amount_range': '%d-%d' % (d['amount_min'], d['amount_max']),
        'active': d['active']
    } for d in result['ls']]
    return result


def add(**params):
    BankAccount.add(**params)


def remove(ba_id):
    BankAccount.remove(ba_id)


def switch(ba_id):
    BankAccount.switch(ba_id)
