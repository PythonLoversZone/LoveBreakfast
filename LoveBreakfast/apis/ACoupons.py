# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.config.response import APIS_WRONG

sys.path.append(os.path.dirname(os.getcwd()))


class LBCoupons(Resource):

    def __init__(self):
        pass

    @staticmethod
    def post(card):
        print(PRINT_API_NAME.format(card))

        apis = {
            "update_coupons": "control_coupon.add_cardpackage()",
        }

        if card in apis:
            return eval(apis[card])

        return APIS_WRONG

    @staticmethod
    def get(card):
        print(PRINT_API_NAME.format(card))

        apis = {
            "get_cardpkg": "control_coupon.get_cart_pkg()"

        }

        if card in apis:
            return eval(apis[card])

        return APIS_WRONG
