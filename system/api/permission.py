from three_server.base.controller import BaseController, HttpStatus
from django.contrib.auth.models import Permission
from three_server.base.result import ResultCode, ResultMsg


class PermissionController(BaseController):

    def get_permissions(self):
        perms = Permission.objects.filter(content_type_id=15).values("id", "codename", "name")
        a = [{
                'label': str(p['name']).split('/')[len(str(p['name']).split('/')) - 1],
                'type': 'first' if len(str(p['name']).split('/')) == 1 else 'children',
                'array': str(p['name']).split('/'),
                'value': p['id'],
                'children': []
            }for p in perms]
        for av in a[::-1]:
            if av['type'] == 'children':
                continue
            for av2 in a[::-1]:
                if av2['type'] == 'children' and av['array'][0] == av2['array'][0]:
                    del av2['array']
                    del av2['children']
                    av['children'].append(av2)
                    a.remove(av2)
        return self.json(code=ResultCode.CODE_20000.value, message=ResultMsg.MSG_20000.value, data=a)



