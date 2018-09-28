# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.control.CShop import CShop

sys.path.append(os.path.dirname(os.getcwd()))


class LBShop(Resource):
    def __init__(self):
        self.control_shop = CShop()

    @staticmethod
    def post(shop):
        print(PRINT_API_NAME.format(shop))

        apis = {

        }

        if shop in apis:
            return eval(apis[shop])

        return

    @staticmethod
    def get(shop):
        print(PRINT_API_NAME.format(shop))

        apis = {
            "get_all_shops": "self.control_shop.get_all_shops()",
            "get_shop_detail": "self.control_shop.get_shop_detail()",
            "get_category_and_product": "self.control_shop.get_category_and_product()"
        }
        return eval(apis[shop])
