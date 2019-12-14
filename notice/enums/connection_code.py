from enum import Enum


# 必须是1000或从[3000,4999]开始
class ConnectionCode(Enum):
    VerificationFailed = 4003  # 验证不通过


class ConnectionMsg(Enum):
    VerificationFailed = 'VerificationFailed'      # 验证不通过
