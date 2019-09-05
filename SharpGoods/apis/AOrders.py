# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from SharpGoods.control.COrders import COrders
from SharpGoods.config.response import APIS_WRONG

class SGOrders(Resource):
    def __init__(self):
        self.corders = COrders()

    def get(self, orders):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(orders))
        print("=======================api===================")

        apis = {
            "get_order_list":"self.corders.get_order_list()",
            "get_order_abo":"self.corders.get_order_abo()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])

    def post(self, orders):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(orders))
        print("=======================api===================")

        apis = {
            "make_main_order":"self.corders.make_order()",
            "update_order_status":"self.corders.update_order_status()",
            "order_price": "self.corders.get_order_price()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])