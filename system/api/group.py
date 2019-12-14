from three_server.base.controller import BaseController
from system.forms.groupform import GroupForm, FindGroupForm
from django.contrib.auth.models import Permission, Group
from three_server.base.result import ResultCode, ResultMsg
from django.db.utils import IntegrityError


class GroupController(BaseController):

    def create_group(self):
        form = GroupForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
        try:
            group = Group.objects.get(id=form.data['group_id'])
            group.name = form.data['group_name']
            group.permissions.clear()
            for perm_id in form.data['permissions']:
                perm = Permission.objects.get(id=perm_id)
                group.permissions.add(perm)
            group.save()
            return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
        except IntegrityError:
            return self.json(ResultCode.CODE_60001.value, None, ResultMsg.MSG_60001.value)
        except Group.DoesNotExist:
            try:
                Group.objects.get(name=form.data['group_name'])
                return self.json(ResultCode.CODE_60001.value, None, ResultMsg.MSG_60001.value)
            except Group.DoesNotExist:
                group = Group.objects.create(name=form.data['group_name'])
                group.permissions.clear()
                for perm_id in form.data['permissions']:
                    perm = Permission.objects.get(id=perm_id)
                    group.permissions.add(perm)
                return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def delete_group(self):
        group_id = self.get_argument('group_id')
        group = Group.objects.get(id=group_id)
        is_occupy = group.user_set.all()
        if is_occupy:
            return self.json(ResultCode.CODE_60002.value, None, ResultMsg.MSG_60002.value)
        else:
            group.delete()
            groups = Group.objects.all().values()
        return self.json(ResultCode.CODE_20000.value, groups, ResultMsg.MSG_20000.value)

    def update_group(self):
        form = GroupForm(self.body_data())
        if form.is_valid():
            group = Group.objects.get(id=form.data["id"])
            group.name = form.data["group_name"]
            group.permissions.clear()
            for perm_id in form.data['permissions']:
                perm = Permission.objects.get(id=perm_id)
                group.permissions.add(perm)
            group.save()
            groups = Group.objects.all().values()
            return self.json(ResultCode.CODE_20000.value, groups, ResultMsg.MSG_20000.value)
        else:
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)

    def get_groups(self):
        form = FindGroupForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
        groups = Group.objects.filter().order_by('-id').values()[
                 (int(form.data['current_page']) - 1) * int(form.data['page_size']):
                 (int(form.data['current_page']) - 1) * int(form.data['page_size']) + int(form.data['page_size'])]
        total = Group.objects.filter().count()
        return self.json(ResultCode.CODE_20000.value, {'ls': groups, 'total': total}, ResultMsg.MSG_20000.value)

    def get_groups_option(self):
        groups = Group.objects.filter().values('id', 'name')
        options = [{'label': v['name'], 'value': v['id']} for v in groups]
        return self.json(ResultCode.CODE_20000.value, options, ResultMsg.MSG_20000.value)

    def get_group_perms(self):
        group_id = self.get_argument("group_id")
        if group_id is None:
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
        data = {}
        perms = Permission.objects.filter(content_type_id__gte=7).values("id", "codename", "name")
        ret = [{"key": p['id'], "label": p['name']} for p in perms]
        data['all'] = ret

        group = Group.objects.get(id=group_id)
        had_perms = group.permissions.all().values("id")
        had = [p['id'] for p in had_perms]
        data['own'] = had
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def get_group_perms_id(self):
        group_id = self.get_argument("group_id")
        if group_id is None:
            return self.json(ResultCode.CODE_40000.value, None, ResultMsg.MSG_40000.value)
        data = {}
        try:
            group = Group.objects.get(id=group_id)
            had_perms = group.permissions.all().values("id")
            had = [p['id'] for p in had_perms]
            data['own'] = had
            return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
        except Group.DoesNotExist:
            return self.json(ResultCode.CODE_53001.value, None, ResultMsg.MSG_53001.value)
