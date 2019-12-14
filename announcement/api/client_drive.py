from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from announcement.biz.client_drive import search_client


class ClientDriverController(BaseController):

    def search(self):
        """
        @api {post} /three/announcement/drive/search 查询活动公告列表
        @apiVersion 1.0.0
        @apiName search
        @apiGroup Announcement
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                    "1": {
                        "title": "文字活动",
                        "content_type": "TEXT",
                        "content": "内容内容内容内容内容内容",
                    },
                    "2": {
                        "title": "图片活动",
                        "content_type": "IMAGE",
                        "content": "http:x/0.jpg",
                    }
            }
        }
        """
        data = search_client()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
