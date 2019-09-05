# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from SharpGoods.config.response import APIS_WRONG
from SharpGoods.control.CCoupons import CCoupons


class SGCoupons(Resource):
    def __init__(self):
        self.ccoupons = CCoupons()

    def post(self, card):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(card))
        print("=======================api===================")

        apis = {
            "update_coupons": "self.ccoupons.add_cardpackage()",
        }

        if card not in apis:
            return APIS_WRONG
        return eval(apis[card])

    def get(self, card):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(card))
        print("=======================api===================")

        apis = {
            "get_cardpkg": "self.ccoupons.get_cart_pkg()"
        }

        if card not in apis:
            return APIS_WRONG
        return eval(apis[card])