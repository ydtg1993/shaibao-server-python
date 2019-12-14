from finance.models.bank_option import BankOption


def search(**params):
    return BankOption.search_server(**params)


def add(name):
    return BankOption.creat(name)


def remove(obj_id):
    return BankOption.remove(obj_id)


def find_by_name(name):
    return BankOption.find_by_name(name)


def init_option():
    BankOption.init_option()


def delete_all():
    BankOption.delete_all()


def switch(obj_id):
    BankOption.switch(obj_id)
