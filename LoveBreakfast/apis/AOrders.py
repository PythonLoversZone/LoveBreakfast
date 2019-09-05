# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.config.response import APIS_WRONG

sys.path.append(os.path.dirname(os.getcwd()))


class LBOrders(Resource):
    def __init__(self):
        pass

    @staticmethod
    def get(orders):
        print(PRINT_API_NAME.format(orders))

        apis = {
            "get_order_list": "control_order.get_order_list()",
            "get_order_abo": "control_order.get_order_abo()",
            "get_order_user": "control_order.get_order_user()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])

    @staticmethod
    def post(orders):
        print(PRINT_API_NAME.format(orders))

        apis = {
            "make_main_order": "control_order.make_main_order()",
            "add_order_items": "control_order.add_order_items()",
            "update_order_info": 'control_order.update_order_info()',
            "update_order_status": "control_order.update_order_status()",
            "order_price": "control_order.get_order_price()"
        }

        if orders not in apis:
            return APIS_WRONG

        return eval(apis[orders])
