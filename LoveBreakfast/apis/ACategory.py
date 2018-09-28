# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.services.SCategory import SCategory

sys.path.append(os.path.dirname(os.getcwd()))


class LBCategory(Resource):
    def __init__(self):
        self.control_category = SCategory()

    @staticmethod
    def post(category):
        print(PRINT_API_NAME.format(category))

        apis = {

        }

        if category in apis:
            return eval(apis[category])

        return

    @staticmethod
    def get(category):
        print(PRINT_API_NAME.format(category))

        apis = {
            "get_all_category": "self.control_category.get_all_category()",
            "get_category_by_sid": "self.control_category.get_category_by_sid()",
        }
        return eval(apis[category])
