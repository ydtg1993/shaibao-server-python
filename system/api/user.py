from three_server.base.controller import BaseController
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from system.forms.user import UserForm, UpdateUserPasswordForm, ShowUserForm
from django.contrib.auth import authenticate
from django.db.models import Q
from system.permission.menu import get_user_menus
from django.db.utils import IntegrityError
from three_server.base.result import ResultCode, ResultMsg


class UserController(BaseController):

    def get_user_info(self):
        user = self.request.user
        data = {
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            # 'is_super': user.is_superuser,
            'user_id': user.id,
            'name': user.username,
            'menus': get_user_menus(user),
            # 'menus': get_admin_menu(),
            'roles': ['admin']
        }
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def submit_user(self):
        r_user_id = self.request.user.id
        if r_user_id is None:
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        try:
            user = User.objects.get(id=r_user_id)
            if not user.is_superuser:
                return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
            form = UserForm(self.body_data())
            if not form.is_valid():
                return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
            password = make_password(form.data['password'])
            try:
                submit_user = User.objects.get(id=form.data['user_id'])
                submit_user.username = form.data['user_name']
                submit_user.password = password
                submit_user.save()
                message = '修改成功'
            except IntegrityError:
                return self.json(ResultCode.CODE_60001.value, None, ResultMsg.MSG_60001.value)
            except User.DoesNotExist:
                try:
                    User.objects.get(username=form.data['user_name'])
                    return self.json(ResultCode.CODE_60001.value, None, ResultMsg.MSG_60001.value)
                except User.DoesNotExist:
                    email = '%s@qq.com' % form.data['user_name']
                    submit_user = User.objects.create(
                        username=form.data['user_name'],
                        password=password,
                        email=email,
                        is_active=True
                    )
                    message = '创建成功'
            submit_user.groups.clear()
            submit_user.groups.add(form.data["role"])
            return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
        except User.DoesNotExist:
            return self.json(ResultCode.CODE_53001.value, None, ResultMsg.MSG_53001.value)

    def delete_user(self):
        r_user_id = self.request.user.id
        if r_user_id is None:
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        try:
            user = User.objects.get(id=r_user_id)
            if not user.is_superuser:
                return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
            user_id = self.get_argument('user_id')
            if user_id is None:
                return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
            user = User.objects.get(id=user_id)
            user.is_active = False
            user.save()
            return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
        except User.DoesNotExist:
            return self.json(ResultCode.CODE_53001.value, None, ResultMsg.MSG_53001.value)

    def show_user(self):
        form = ShowUserForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
        q_roles = Q()
        q_roles.connector = "OR"
        q_name = Q()
        q_name.connector = "AND"
        base = Q(is_active=True, is_superuser=False)
        for role in self.body_data()['roles']:
            q_roles.children.append(('groups__id', role))
        if self.body_data()['username'] is not None and self.body_data()['username'] is not '':
            q_name.children.append(('username', self.body_data()['username']))

        con = Q()
        con.add(q_roles, 'AND')
        con.add(base, 'AND')
        con.add(q_name, 'AND')

        users = User.objects.filter(
            con
        ).order_by('id').values(
            'id',
            'username',
            'groups__name',
            'groups__id',
        )[
            (int(self.body_data()['current_page']) - 1) *
            int(self.body_data()['page_size']):
            (int(self.body_data()['current_page']) - 1) *
            int(self.body_data()['page_size']) + int(self.body_data()['page_size'])
        ]
        data = {'total': User.objects.filter(con).count(), 'listData': users}
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def update_password(self):
        form = UpdateUserPasswordForm(self.body_data())
        if form.is_valid():
            username = self.request.user.username
            user = authenticate(username=username, password=form.data['password'])
            if user is not None:
                user.password = make_password(form.data['new_password'])
                user.save()
                return self.json(200, message="修改成功，本次退出后生效")
            else:
                return self.json(401, message='旧密码输入错误')

