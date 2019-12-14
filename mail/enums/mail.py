from enum import Enum


class MailType(Enum):
    SYSTEM_MAIL = 'SYSTEM_MAIL'  # 群发邮件
    PRIVATE_MAIL = 'PRIVATE_MAIL'  # 私人邮件


class MailTypeMsg(Enum):
    SYSTEM_MAIL = '系统邮件'  # 系统邮件
    PRIVATE_MAIL = '私人邮件'  # 私人邮件


class MailContentType(Enum):
    TEXT = 'TEXT'    # 文字
    IMAGE = 'IMAGE'  # 图片


class MailContentMsg(Enum):
    TEXT = '文字'    # 文字
    IMAGE = '图片'   # 图片


class AnnexType(Enum):
    GOLD = 'GOLD'  # 金币
    OBJECT = 'OBJECT'  # 金币


class AnnexTypeMsg(Enum):
    GOLD = '金币'  # 金币
    OBJECT = '实物'  # 金币
