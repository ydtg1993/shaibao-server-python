from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from mail.forms.client_mail import MailListForm, MailIDForm

from mail.biz.client_mail import search_client, search_content, delete_mail, get_annex_gold, set_is_receive
from player.biz.public_player import update_player_gold
from player.notice.player_notice import update_player_info


class ClientMailController(BaseController):

    def list(self):
        """
        @api {post} /three/mail/mail/list 邮件列表
        @apiVersion 1.0.0
        @apiName leader_board
        @apiGroup Mail
        @apiParam (参数) {Number} current_page 当前页
        @apiParam (参数) {Number} page_size 页行数
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "ls": [
                    {
                        "id": 1,
                        "tag": "系统消息",
                        "title": "vip充值回馈",
                        "create_at": "2019/08/10 12:00:00",
                        "exist_annex": True,
                        "is_read": False,
                        "is_receive": False
                    },
                    {
                        "id": 2,
                        "tag": "独家消息",
                        "title": "vip充值回馈",
                        "create_at": "2019/08/10 12:00:00",
                        "exist_annex": False,
                        "is_read": False,
                        "is_receive": False
                    }
                ],
                "total": 20
            }
        }
        """
        form = MailListForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['player_id'] = self.request.player.id
        data = search_client(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def info(self):
        """
        @api {post} /three/mail/mail/info 邮件详情
        @apiVersion 1.0.0
        @apiName info
        @apiGroup Mail
        @apiParam (参数) {String} obj_id 编号
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "id": 1,
                "content_type": "TEXT",
                "content": "内容内容内容内容内容",
                "annex": {
                    "type": "GOLD",
                    "value": 50
                },
                "is_receive": True,
                "exist_annex": True,
            }
        }
        """
        form = MailIDForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_content(form.data['obj_id'], self.request.player.id)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def delete_mail(self):
        """
        @api {post} /three/mail/mail/delete_mail 删除邮件
        @apiVersion 1.0.0
        @apiName delete
        @apiGroup Mail
        @apiParam (参数) {String} obj_id 编号
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {}
        }
        """
        form = MailIDForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = delete_mail(form.data['obj_id'], self.request.player.id)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def receive(self):
        """
        @api {post} /three/mail/mail/receive 领取附件
        @apiVersion 1.0.0
        @apiName receive
        @apiGroup Mail
        @apiParam (参数) {String} obj_id 编号
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {}
        """
        form = MailIDForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        # 获取附件金币
        sum_gold = get_annex_gold(form.data['obj_id'], self.request.player.id)
        if sum_gold is None:
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        # 更新玩家金币
        ok, player = update_player_gold(self.request.player.token, sum_gold)
        if not ok:
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        update_player_info(player)
        set_is_receive(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def test_send(self):
        update_player_info(self.request.player)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
