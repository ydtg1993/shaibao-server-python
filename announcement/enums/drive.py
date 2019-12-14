from enum import Enum


class DriveType(Enum):
    NEW = 'NEW'         # 新人活动
    NORMAL = 'NORMAL'   # 标准活动
    RETURN = 'RETURN'   # 回归活动


class DriveTypeMsg(Enum):
    NEW = '新人活动'     # 新人活动
    NORMAL = '标准活动'  # 标准活动
    RETURN = '回归活动'  # 回归活动


class DriveContentType(Enum):
    TEXT = 'TEXT'    # 文字
    IMAGE = 'IMAGE'  # 图片


class DriveContentTypeMsg(Enum):
    TEXT = '文字'    # 文字
    IMAGE = '图片'   # 图片
