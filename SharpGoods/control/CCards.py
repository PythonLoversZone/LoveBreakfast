# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from SharpGoods.common.TransformToList import add_model, update_model, get_all
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS


class CCards():
    def __init__(self):
        pass

    def add_card(self):
        args = request.args.to_dict()
        print args
        if "openid" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        print data
        if "Cname" not in data:
            return {
                "status":405,
                "status_code":405900,
                "message":"请填写姓名"
            }
        if "Ctelphone" not in data:
            return {
                "status":405,
                "status_code":405901,
                "message":"请填写联系方式"
            }
        if "Ccompany" not in data:
            return {
                "status":405,
                "status_code":405902,
                "message":"请填写公司名称"
            }
        if "Cposition" not in data:
            return {
                "status":405,
                "status_code":405903,
                "message":"请输入职位"
            }
        if "Clocation" not in data:
            return {
                "status":405,
                "status_code":405904,
                "message":"请选择公司地址"
            }
        Cid = str(uuid.uuid1())
        add_model("Cards",
                  **{
                      "Cid": Cid,
                      "Cname": data["Cname"],
                      "Ctelphone": data["Ctelphone"],
                      "Ccompany": data["Ccompany"],
                      "Cposition": data["Cposition"],
                      "Clocation": data["Clocation"],
                      "openid": args["openid"]
                  })
        return {
            "status": 200,
            "message": "OK",
            "data": {
                "Cid": Cid
            }
        }

    def update_card(self):
        args = request.args.to_dict()
        if "openid" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        if "Cname" not in data:
            return {
                "status": 405,
                "status_code": 405900,
                "message": "请填写姓名"
            }
        if "Ctelphone" not in data:
            return {
                "status": 405,
                "status_code": 405901,
                "message": "请填写联系方式"
            }
        if "Ccompany" not in data:
            return {
                "status": 405,
                "status_code": 405902,
                "message": "请填写公司名称"
            }
        if "Cposition" not in data:
            return {
                "status": 405,
                "status_code": 405903,
                "message": "请输入职位"
            }
        if "Clocation" not in data:
            return {
                "status": 405,
                "status_code": 405904,
                "message": "请选择公司地址"
            }
        Cid = str(uuid.uuid1())
        update_model("Cards",
                  **{
                      "Cid": Cid,
                      "Cname": data["Cname"],
                      "Ctelphone": data["Ctelphone"],
                      "Ccompany": data["Ccompany"],
                      "Cposition": data["Cposition"],
                      "Clocation": data["Clocation"],
                      "openid": args["openid"]
                  })
        return {
            "status": 200,
            "message": "OK",
            "data": {
                "Cid": Cid
            }
        }

    def get_mycard(self):
        args = request.args.to_dict()
        if "openid" not in args:
            return PARAMS_MISS
        all_card = get_all("Cards", args["openid"])
        my_cards = []
        for row in all_card:
            my_card = {}
            my_card["Cid"] = row.Cid
            my_card["Cname"] = row.Cname
            my_card["Ctelphone"] = row.Ctelphone
            my_card["Ccompany"] = row.Ccompany
            my_card["Cposition"] = row.Cposition
            my_card["Clocation"] = row.Clocation
            my_card["openid"] = row.openid
            my_cards.append(my_card)
        return {
            "status": 200,
            "message": "OK",
            "data": my_cards
        }

    def get_openid(self):
        args = request.args.to_dict()
        if "code" not in args:
            return PARAMS_MISS
        print("=======================args===================")
        print(args)
        print("=======================args===================")
        code = args["code"]
        APP_ID = "wx284751ea4c889568"
        APP_SECRET_KEY = "051c81977efa8175e43686565265bb4f"
        request_url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type={3}" \
            .format(APP_ID, APP_SECRET_KEY, code, "authorization_code")
        print("=======================request_url===================")
        print str(request_url)
        print("=======================request_url===================")
        strResult = None
        try:
            import urllib2
            req = urllib2.Request(request_url)
            response = urllib2.urlopen(req)
            strResult = response.read()
            response.close()
            print strResult
        except Exception as e:
            print e.message
        if "openid" not in strResult or "session_key" not in strResult:
            return SYSTEM_ERROR
        strResult = json.loads(strResult)
        print("=======================strResult===================")
        print(strResult)
        print("=======================strResult===================")
        openid = strResult["openid"]

        data = {
            "status": 200,
            "message": "OK"
        }
        data["data"] = {}
        data["data"]["openid"] = openid

        return data