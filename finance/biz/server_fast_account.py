from finance.models.fast_account import FastAccount


def search(**params):
    result = FastAccount.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'account_name': d['account_name'],
        'account_number': d['account_number'],
        'qr_code': d['qr_code'],
        'active': d['active']
    } for d in result['ls']]
    return result


def add(**params):
    FastAccount.add(**params)


def remove(ba_id):
    FastAccount.remove(ba_id)


def switch(ba_id):
    FastAccount.switch(ba_id)


def activation(ba_id):
    FastAccount.activation(ba_id)
