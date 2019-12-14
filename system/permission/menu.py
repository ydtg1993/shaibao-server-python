from django.contrib.auth.models import User
import copy


settingMenu = [
    {'path': 'permission', 'component': 'permission', 'name': 'permission', 'meta': {'title': '权限管理', 'icon': 'permission2'}},
    {'path': 'group', 'component': 'group', 'name': 'group', 'meta': {'title': '角色管理', 'icon': 'group'}},
    {'path': 'users', 'component': 'user', 'name': 'users', 'meta': {'title': '用户管理', 'icon': 'user'}}
]

gameSetMenu = [
    {'path': 'sign-reward', 'component': 'sign-reward', 'name': 'sign-reward', 'meta': {'title': '签到奖励', 'icon': 'group'}},
    {'path': 'recharge-set', 'component': 'recharge-set', 'name': 'recharge-set', 'meta': {'title': '充值设置', 'icon': 'group'}}
]

hallMenu = [
    {'path': 'hall', 'component': 'hall', 'name': 'hall', 'meta': {'title': '大厅配置', 'icon': 'hall'}},
]

resultMenu = [
    {'path': 'result', 'component': 'result', 'name': 'result', 'meta': {'title': '开奖记录', 'icon': 'result'}},
]

playerMenu = [
    {'path': 'player', 'component': 'player', 'name': 'player', 'meta': {'title': '玩家列表', 'icon': 'group'}},

]

mailMenu = [
    {'path': 'mail', 'component': 'mail', 'name': 'mail', 'meta': {'title': '邮件列表', 'icon': 'group'}},
]

announcementMenu = [
    {'path': 'drive', 'component': 'drive', 'name': 'drive', 'meta': {'title': '活动公告', 'icon': 'group'}},
    {'path': 'notice', 'component': 'notice', 'name': 'notice', 'meta': {'title': '全服通知', 'icon': 'group'}}
]

financeMenu = [
    {'path': 'bank', 'component': 'bank', 'name': 'bank', 'meta': {'title': '银行选项', 'icon': 'group'}},
    {'path': 'bank-account', 'component': 'bank-account', 'name': 'bank-account', 'meta': {'title': '银行账户', 'icon': 'group'}},
    {'path': 'fast', 'component': 'fast', 'name': 'fast', 'meta': {'title': '快捷账户', 'icon': 'group'}},
    {'path': 'recharge', 'component': 'recharge', 'name': 'recharge', 'meta': {'title': '充值记录', 'icon': 'group'}},
    {'path': 'withdraw', 'component': 'withdraw', 'name': 'withdraw', 'meta': {'title': '提现列表', 'icon': 'group'}},
]

menu_config = [
    {
        'path': '/system',
        'component': 'Layout',
        'meta': {'title': '系统设置', 'icon': 'system'},
        'children': settingMenu
    },
    {
        'path': '/game-setting',
        'component': 'Layout',
        'meta': {'title': '游戏配置', 'icon': 'group'},
        'children': gameSetMenu
    },
    {

        'path': '/hall',
        'component': 'Layout',
        'meta': {'title': '大厅设置', 'icon': 'hall'},
        'children': hallMenu
    },
    {
        'path': '/result',
        'component': 'Layout',
        'meta': {'title': '开奖记录', 'icon': 'result'},
        'children': resultMenu
    },
    {
        'path': '/player',
        'component': 'Layout',
        'meta': {'title': '玩家管理', 'icon': 'group'},
        'children': playerMenu
    },
    {
        'path': '/mail',
        'component': 'Layout',
        'meta': {'title': '邮件管理', 'icon': 'group'},
        'children': mailMenu
    },
    {
        'path': '/announcement',
        'component': 'Layout',
        'meta': {'title': '公告管理', 'icon': 'group'},
        'children': announcementMenu
    },
    {
        'path': '/finance',
        'component': 'Layout',
        'meta': {'title': '财务管理', 'icon': 'group'},
        'children': financeMenu
    }
]


def get_admin_menu():
    return menu_config


def get_user_menus(user: User):
    if user.is_superuser:
        return menu_config
    perms = user.get_all_permissions()
    copy_menu = copy.deepcopy(menu_config)
    new_menus = has_perm(copy_menu, perms)
    return new_menus


def get_admin_menus(user: User):
    if user.is_superuser:
        return menu_config
    perms = user.get_all_permissions()
    copy_menu = copy.deepcopy(menu_config)
    new_menus = has_perm(copy_menu, perms)
    return new_menus


def has_perm(nodes, perms):
    new_menus = []
    for n in nodes:
        for p in perms:
            if p.split('.')[1].startswith(n['path']):
                if 'children' in n.keys():
                    n['children'] = has_perm(n['children'], perms)
                new_menus.append(n)
                break
    return new_menus
