define({ "api": [
  {
    "type": "post",
    "url": "/three/announcement/pig/info",
    "title": "金猪活动详情",
    "version": "1.0.0",
    "name": "pigInfo",
    "group": "Announcement",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"player_integral\": 9000,\n        \"total\": 999999,\n        \"record\": [\n            {\"name\": \"亚托克斯\", \"gold\": 500},\n            {\"name\": \"维鲁斯\", \"gold\": 500},\n            {\"name\": \"拉亚斯特\", \"gold\": 500}\n        ]\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./announcement/api/client_pig.py",
    "groupTitle": "Announcement"
  },
  {
    "type": "post",
    "url": "/three/announcement/pig/open",
    "title": "砸金猪接口",
    "version": "1.0.0",
    "name": "pigOpen",
    "group": "Announcement",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"gold\": 50\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./announcement/api/client_pig.py",
    "groupTitle": "Announcement"
  },
  {
    "type": "post",
    "url": "/three/announcement/drive/search",
    "title": "查询活动公告列表",
    "version": "1.0.0",
    "name": "search",
    "group": "Announcement",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n            \"1\": {\n                \"title\": \"文字活动\",\n                \"content_type\": \"TEXT\",\n                \"content\": \"内容内容内容内容内容内容\",\n            },\n            \"2\": {\n                \"title\": \"图片活动\",\n                \"content_type\": \"IMAGE\",\n                \"content\": \"http:x/0.jpg\",\n            }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./announcement/api/client_drive.py",
    "groupTitle": "Announcement"
  },
  {
    "type": "post",
    "url": "/three/announcement/notice/search",
    "title": "查询全服公告",
    "version": "1.0.0",
    "name": "search2",
    "group": "Announcement",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": [\n        \"我是一条通知。。。。。\",\n        \"我也是哦。。。。。\",\n        \"我也是耶✌。。。。。\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./announcement/api/client_notice.py",
    "groupTitle": "Announcement"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./apidoc/main.js",
    "group": "D__WorkSpase_Python_three_server_apidoc_main_js",
    "groupTitle": "D__WorkSpase_Python_three_server_apidoc_main_js",
    "name": ""
  },
  {
    "type": "post",
    "url": "/three/finance/bank/search",
    "title": "查询银行卡选项",
    "version": "1.0.0",
    "name": "bank_search",
    "group": "Finance",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"1\": \"中国银行\",\n        \"2\": \"平安银行\",\n        \"3\": \"邮政银行\",\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_bank_option.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/finance/pay/pay_method",
    "title": "查询支付方式",
    "version": "1.0.0",
    "name": "pay_method",
    "group": "Finance",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"fast\": {\n            \"0\": {\n                \"id\": \"1\",\n                \"name\": \"奥利瑞安·索尔\",\n                \"number\": \"123456789\",\n                \"qr_code\": \"base64****\",\n            }\n        },\n        \"banks\": {\n            \"0\": {\n                \"id\": \"1\",\n                \"bank_name\": \"中国邮政银行\",\n                \"interval\": \"5000-100000\",\n                \"name\": \"123456789\",\n                \"number\": \"123456789\",\n            },\n            \"1\": {\n                \"id\": \"2\",\n                \"bank_name\": \"中国建设银行\",\n                \"interval\": \"5000-8000\",\n                \"name\": \"123456789\",\n                \"number\": \"123456789\",\n            },\n        },\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_pay.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/finance/pay/record",
    "title": "支付记录",
    "version": "1.0.0",
    "name": "pay_record",
    "group": "Finance",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "current_page",
            "description": "<p>当前页</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "page_size",
            "description": "<p>页行数</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"id\": 1,\n                \"type\": \"快捷支付\",\n                \"pay_money\": \"987.00\",\n                \"create_at\": \"2019.09.20\",\n                \"status\": 1,\n            },\n            {\n                \"id\": 2,\n                \"type\": \"银行支付\",\n                \"pay_money\": \"987.00\",\n                \"create_at\": \"2019.09.20\",\n                \"status\": 0,\n            },\n        ],\n        \"total\": 20\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_pay.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/finance/pay/to_pay",
    "title": "支付",
    "version": "1.0.0",
    "name": "to_pay",
    "group": "Finance",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "pay_type",
            "description": "<p>支付类型</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "account_id",
            "description": "<p>方式ID</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "player_name",
            "description": "<p>玩家名称</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "pay_money",
            "description": "<p>支付金额</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_pay.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/finance/withdraw/add",
    "title": "提现申请",
    "version": "1.0.0",
    "name": "withdraw_add",
    "group": "Finance",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "value",
            "description": "<p>兑换金额</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_withdraw.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/finance/withdraw/search",
    "title": "查询提现记录",
    "version": "1.0.0",
    "name": "withdraw_search",
    "group": "Finance",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "current_page",
            "description": "<p>当前页</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "page_size",
            "description": "<p>页行数</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"sequence\": 1,\n                \"create_at\": 2019-09-30,\n                \"amount\": 56,\n                \"status\": 0\n            },\n            {\n                \"sequence\": 1,\n                \"create_at\": 2019-09-30,\n                \"amount\": 56,\n                \"status\": -1\n            },\n            {\n                \"sequence\": 2,\n                \"create_at\": 2019-09-29,\n                \"amount\": 193.9,\n                \"status\": 1\n            },\n        ],\n        \"total\": 20\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./finance/api/client_withdraw.py",
    "groupTitle": "Finance"
  },
  {
    "type": "post",
    "url": "/three/hall/client/enter_hall",
    "title": "进入大厅",
    "version": "1.0.0",
    "name": "enter_hall",
    "group": "Hall",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "hall_tag",
            "description": "<p>大厅标识</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"id\": 1,\n        \"name\": \"极速快三\",\n        \"lottery_type\": \"Self\",\n        \"lottery_time\": 1212121212,\n        \"game_date\": \"极速快三\",\n        \"stage\": \"BetStage\",\n        \"total\": \"100\",\n        \"sequence\": 1909050001,\n        \"previous_result\": [],\n        \"bet_option\": {\n            \"1\": {\n                \"dice_type\": \"BIG\",\n                \"odds\": 1\n            },\n            \"2\": {\n                \"dice_type\": \"SMALL\",\n                \"odds\": 1\n            },\n            ...\n        },\n        \"chip_option\": {\n            \"1\": {\n                \"label\": \"100\",\n                \"value\": 100,\n            },\n            \"2\": {\n                \"label\": \"1千\",\n                \"value\": 1000,\n            },\n            \"3\": {\n                \"label\": \"1万\",\n                \"value\": 10000,\n            },\n            ...\n        },\n        \"player\": {\n            \"gold\": 99\n        }\n    }",
          "type": "json"
        }
      ]
    },
    "filename": "./hall/api/client_hall.py",
    "groupTitle": "Hall"
  },
  {
    "type": "post",
    "url": "/three/hall/result/lottery_record",
    "title": "开奖记录",
    "version": "1.0.0",
    "name": "lottery_record",
    "group": "Hall",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "hall_tag",
            "description": "<p>大厅标识</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"id\": 1,\n                \"sequence\": 0001,\n                \"result\": [1,2,3],\n                \"big\": False,\n                \"even\": True,\n                \"sum\": 6\n            },\n            ...\n        ]\n    }",
          "type": "json"
        }
      ]
    },
    "filename": "./hall/api/client_result.py",
    "groupTitle": "Hall"
  },
  {
    "type": "post",
    "url": "/three/mail/mail/delete_mail",
    "title": "删除邮件",
    "version": "1.0.0",
    "name": "delete",
    "group": "Mail",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "obj_id",
            "description": "<p>编号</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./mail/api/client_mail.py",
    "groupTitle": "Mail"
  },
  {
    "type": "post",
    "url": "/three/mail/mail/info",
    "title": "邮件详情",
    "version": "1.0.0",
    "name": "info",
    "group": "Mail",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "obj_id",
            "description": "<p>编号</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"id\": 1,\n        \"content_type\": \"TEXT\",\n        \"content\": \"内容内容内容内容内容\",\n        \"annex\": {\n            \"type\": \"GOLD\",\n            \"value\": 50\n        },\n        \"is_receive\": True,\n        \"exist_annex\": True,\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./mail/api/client_mail.py",
    "groupTitle": "Mail"
  },
  {
    "type": "post",
    "url": "/three/mail/mail/list",
    "title": "邮件列表",
    "version": "1.0.0",
    "name": "leader_board",
    "group": "Mail",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "current_page",
            "description": "<p>当前页</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "page_size",
            "description": "<p>页行数</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"id\": 1,\n                \"tag\": \"系统消息\",\n                \"title\": \"vip充值回馈\",\n                \"create_at\": \"2019/08/10 12:00:00\",\n                \"exist_annex\": True,\n                \"is_read\": False,\n                \"is_receive\": False\n            },\n            {\n                \"id\": 2,\n                \"tag\": \"独家消息\",\n                \"title\": \"vip充值回馈\",\n                \"create_at\": \"2019/08/10 12:00:00\",\n                \"exist_annex\": False,\n                \"is_read\": False,\n                \"is_receive\": False\n            }\n        ],\n        \"total\": 20\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./mail/api/client_mail.py",
    "groupTitle": "Mail"
  },
  {
    "type": "post",
    "url": "/three/mail/mail/receive",
    "title": "领取附件",
    "version": "1.0.0",
    "name": "receive",
    "group": "Mail",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "obj_id",
            "description": "<p>编号</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {}",
          "type": "json"
        }
      ]
    },
    "filename": "./mail/api/client_mail.py",
    "groupTitle": "Mail"
  },
  {
    "type": "post",
    "url": "/three/player/bet/bet_record",
    "title": "下注记录",
    "version": "1.0.0",
    "name": "bet_record",
    "group": "Player",
    "description": "<p>ranking:-1 则是未上榜</p>",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "current_page",
            "description": "<p>当前页</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "page_size",
            "description": "<p>页行数</p>"
          },
          {
            "group": "参数",
            "type": "Array",
            "optional": false,
            "field": "types",
            "description": "<p>类型 未开奖：0 赢：1 输：-1</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"hall_tag\": \"Fast\",\n                \"sequence\": \"201908151281\",\n                \"create_at\": \"21:01:00\",\n                \"result\": [1,2,4],\n                \"state\": 1,\n                \"bonus\": 200,\n                \"bet_type\": \"BIG\",\n                \"bet_amount\": 200,\n            },\n            {\n                \"hall_tag\": \"Fast\",\n                \"sequence\": \"201908151281\",\n                \"create_at\": \"21:01:00\",\n                \"result\": [1,2,4],\n                \"state\": 1,\n                \"bonus\": 200,\n                \"bet_type\": \"BIG\",\n                \"bet_amount\": 200,\n            }\n        ],\n        \"total\": 20\n    }\n}",
          "type": "json"
        }
      ],
      "fields": {
        "响应备注": [
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "hall_tag",
            "description": "<p>大厅标签</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "sequence",
            "description": "<p>期号</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "create_at",
            "description": "<p>时间</p>"
          },
          {
            "group": "响应备注",
            "type": "Array",
            "optional": false,
            "field": "result",
            "description": "<p>开奖结果</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "state",
            "description": "<p>状态 0:未开奖 1:赢 -1:输</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "bonus",
            "description": "<p>奖金</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "bet_type",
            "description": "<p>下注类型</p>"
          },
          {
            "group": "响应备注",
            "type": "String",
            "optional": false,
            "field": "bet_amount",
            "description": "<p>下注金额</p>"
          }
        ]
      }
    },
    "filename": "./player/api/client_bet.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/three/player/card/add",
    "title": "添加银行卡",
    "version": "1.0.0",
    "name": "card_add",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>名称</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "number",
            "description": "<p>银行卡号</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "bank_id",
            "description": "<p>开户行</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "bank_branch",
            "description": "<p>支行</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./player/api/client_card.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/three/player/player/leader_board",
    "title": "排行榜",
    "version": "1.0.0",
    "name": "leader_board",
    "group": "Player",
    "description": "<p>ranking:-1 则是未上榜</p>",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "current_page",
            "description": "<p>当前页</p>"
          },
          {
            "group": "参数",
            "type": "Number",
            "optional": false,
            "field": "page_size",
            "description": "<p>页行数</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"ls\": [\n            {\n                \"id\": 1,\n                \"ranking\": 1,\n                \"name\": \"孙坚\",\n                \"profit\": 12345\n            },\n            {\n                \"id\": 2,\n                \"ranking\": 2,\n                \"name\": \"孙策\",\n                \"profit\": 12345.88\n            },\n            {\n                \"id\": 3,\n                \"ranking\": 3,\n                \"name\": \"孙权\",\n                \"profit\": 1245.88\n            }\n        ],\n        \"own\": {\n            \"ranking\": 3,\n            \"name\": \"孙权\",\n            \"profit\": 1245.88\n        }\n        \"total\": 20\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./player/api/client_player.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/auth/client/login",
    "title": "登录",
    "version": "1.0.0",
    "name": "login",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"serial\": \"1566365805\",\n        \"avatar\": \"\",\n        \"name\": \"1566365805\",\n        \"phone\": \"1566365805\",\n        \"gold\": \"0.00\",\n        \"token\": \"43ab1e62-c3e8-11e9-9331-4cedfbc56de4\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./three_server/api/client_auth.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/three/player/card/info",
    "title": "获取玩家银行卡",
    "version": "1.0.0",
    "name": "player_card",
    "group": "Player",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"name\": \"藤田\",\n        \"number\": \"23123123123\",\n        \"bank_name\": \"交通银行\",\n        \"bank_branch\": \"支行\",\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./player/api/client_card.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/three/player/player/player_info",
    "title": "获取玩家信息",
    "version": "1.0.0",
    "name": "player_info",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>玩家Token</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"name\": \"苹果\",\n        \"phone\": \"18009230222\",\n        \"gold\": 1023\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./player/api/client_player.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/auth/client/registered",
    "title": "注册",
    "version": "1.0.0",
    "name": "registered",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>短信验证码</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "invite_code",
            "description": "<p>邀请码</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"serial\": \"1566365805\",\n        \"avatar\": \"\",\n        \"name\": \"1566365805\",\n        \"phone\": \"1566365805\",\n        \"gold\": \"0.00\",\n        \"token\": \"43ab1e62-c3e8-11e9-9331-4cedfbc56de4\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./three_server/api/client_auth.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/auth/client/reset_password",
    "title": "重置密码",
    "version": "1.0.0",
    "name": "reset_password",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>短信验证码</p>"
          },
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"serial\": \"1566365805\",\n        \"avatar\": \"\",\n        \"name\": \"1566365805\",\n        \"phone\": \"1566365805\",\n        \"gold\": \"0.00\",\n        \"token\": \"43ab1e62-c3e8-11e9-9331-4cedfbc56de4\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./three_server/api/client_auth.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/auth/client/send_code",
    "title": "发送验证码",
    "version": "1.0.0",
    "name": "send_code",
    "group": "Player",
    "parameter": {
      "fields": {
        "参数": [
          {
            "group": "参数",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": \"3993\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./three_server/api/client_auth.py",
    "groupTitle": "Player"
  },
  {
    "type": "post",
    "url": "/three/sign/reward/search",
    "title": "签到奖励列表",
    "version": "1.0.0",
    "name": "search",
    "group": "Sign",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": [\n        \"1\": {\n            \"day\":\"1\",\n            \"is_sign\": False,\n            \"allow\": True,\n        },\n        \"2\": {\n            \"day\":\"2\",\n            \"is_sign\": False,\n            \"allow\": False,\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./sign/api/client_sign_reward.py",
    "groupTitle": "Sign"
  },
  {
    "type": "post",
    "url": "/three/sign/sign/sign",
    "title": "玩家签到",
    "version": "1.0.0",
    "name": "sign",
    "group": "Sign",
    "success": {
      "examples": [
        {
          "title": "返回样例:",
          "content": "{\n    \"code\": 20000,\n    \"message\": \"Succeed\",\n    \"data\": {\n        \"type\": \"GOLD\",\n        \"value\": \"19.88\",\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./sign/api/client_sign.py",
    "groupTitle": "Sign"
  },
  {
    "type": "get",
    "url": "ws://10.10.13.153:8000/ws/three/<player_token>",
    "title": "WebSocket 连接",
    "version": "1.0.0",
    "name": "WebSocket___",
    "group": "WebSocket_Connection",
    "filename": "./notice/consumers.py",
    "groupTitle": "WebSocket_Connection"
  },
  {
    "type": "post",
    "url": "/EnterNotice",
    "title": "进入房间通知",
    "version": "1.0.0",
    "name": "EnterNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"EnterNotice\",\n    \"data\": {\n        \"player\":{\n            \"gold\": 1023,\n            \"bet_ls\": []\n        },\n        \"hall\":{\n            \"stage\": \"BetStage\",\n            \"past_result\": [1, 2, 3],\n            \"bet_end_time\": Date\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameBetErrorNotice",
    "title": "下注异常通知",
    "version": "1.0.0",
    "name": "GameBetErrorNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameBetErrorNotice\",\n    \"data\": {\n        \"code\": 41002,\n        \"msg\": \"当阶段不允许\",\n        \"gold\": 10\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameBetSuccessNotice",
    "title": "下注成功通知",
    "version": "1.0.0",
    "name": "GameBetSuccessNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameBetSuccessNotice\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameLotteryNotice",
    "title": "游戏开奖通知",
    "version": "1.0.0",
    "name": "GameLotteryNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameLotteryNotice\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameLotteryResultNotice",
    "title": "游戏结果通知",
    "version": "1.0.0",
    "name": "GameLotteryResultNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameLotteryResultNotice\",\n    \"data\": {\n        \"result\": [1,2,3],\n        \"wins\": [\"BIG\", \"EVEN\", \"SUM_SIXTEEN\"],\n        \"positions\": [1,2,3]\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameOverNotice",
    "title": "游戏结束通知",
    "version": "1.0.0",
    "name": "GameOverNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameOverNotice\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameSettleNotice",
    "title": "游戏结算通知",
    "version": "1.0.0",
    "name": "GameSettleNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameSettleNotice\",\n    \"data\": {}\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/GameStartNotice",
    "title": "游戏开始通知",
    "version": "1.0.0",
    "name": "GameStartNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"GameStartNotice\",\n    \"data\": {\n        \"sequence\": 1909060001,\n        \"previous_result\": [1,2,3],\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/StartBetNotice",
    "title": "游戏下注通知",
    "version": "1.0.0",
    "name": "StartBetNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"StartBetNotice\",\n    \"data\": {\n        \"hall\": {\n            \"lottery_time\": Date\n            \"countdown\": 5\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/UpdatePlayerInfoNotice",
    "title": "更新用户信息通知",
    "version": "1.0.0",
    "name": "UpdatePlayerInfoNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Hall\",\n    \"event\": \"UpdatePlayerInfoNotice\",\n    \"data\": {\n        \"name\": \"苹果\",\n        \"phone\": \"18009230222\",\n        \"gold\": 1023,\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./player/notice/player_notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/WinningNotice",
    "title": "玩家中奖通知",
    "version": "1.0.0",
    "name": "WinningNotice",
    "group": "WebSocket_Notice",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"hall_tag\": \"Fast\",\n    \"event\": \"WinningNotice\",\n    \"data\": {\n        \"win_gold\": 20,\n        \"positions\": [1,2,3]\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/notice/notice.py",
    "groupTitle": "WebSocket_Notice"
  },
  {
    "type": "post",
    "url": "/ReqBet",
    "title": "游戏下注接口",
    "version": "1.0.0",
    "name": "ReqBet",
    "group": "WebSocket_Receive",
    "success": {
      "examples": [
        {
          "title": "通知样例:",
          "content": "{\n    \"event\": \"ReqBet\",\n    \"data\": {\n        \"bet_amount\": 200,\n        \"dice_type\": \"SUM_THREE\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./game/api/api.py",
    "groupTitle": "WebSocket_Receive"
  }
] });
