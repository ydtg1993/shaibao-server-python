from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from announcement.biz.client_notice import search_client


class ClientNoticeController(BaseController):

    def search(self):
        """
        @api {post} /three/announcement/notice/search 查询全服公告
        @apiVersion 1.0.0
        @apiName search2
        @apiGroup Announcement
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": [
                "我是一条通知。。。。。",
                "我也是哦。。。。。",
                "我也是耶✌。。。。。"
            ]
        }
        """
        data = search_client()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
