from finance.models.bank_option import BankOption


def search():
    return {d['id']: d['name'] for d in BankOption.search_client()}
