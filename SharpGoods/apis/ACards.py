# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from SharpGoods.control.CCards import CCards


class SGCards(Resource):
    def __init__(self):
        self.ccards = CCards()

    def post(self, card):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(card))
        print("=======================api===================")
        apis = {
            "add_card": "self.ccards.add_card()",
            "update_card": "self.ccards.update_card()"
        }

        if card not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[card])

    def get(self, card):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(card))
        print("=======================api===================")
        apis = {
            "get_all": "self.ccards.get_mycard()",
            "get_openid": "self.ccards.get_openid()"
        }

        if card not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[card])