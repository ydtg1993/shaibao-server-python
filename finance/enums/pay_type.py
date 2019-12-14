from enum import Enum


class PayType(Enum):
    fast = 'fast'      # 快捷支付
    bank = 'bank'      # 银行支付


class PayTypeMsg(Enum):
    fast = '快捷支付'      # 快捷支付
    bank = '银行支付'      # 银行支付


class PayStatusCode(Enum):
    failed = -1     # 支付失败
    default = 0      # 申请中
    success = 1      # 支付成功


class PayStatus(Enum):
    PayStatusMsg = {-1: '失败', 0: '申请中', 1: '成功'}
