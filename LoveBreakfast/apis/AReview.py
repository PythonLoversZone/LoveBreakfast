# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.config.response import APIS_WRONG
from LoveBreakfast.control.CReview import CReview

sys.path.append(os.path.dirname(os.getcwd()))


class LBReview(Resource):
    def __init__(self):
        self.control_review = CReview()

    @staticmethod
    def post(review):
        print(PRINT_API_NAME.format(review))

        apis = {
            "create_review": "self.control_review.create_review()",
            "delete_user_review": "self.control_review.delete_user_review()"
        }

        if review in apis:
            return eval(apis[review])

        return APIS_WRONG

    @staticmethod
    def get(review):
        print(PRINT_API_NAME.format(review))
        apis = {
            "get_review": "self.control_review.get_review()",
            "get_user_review": "self.control_review.get_user_review()",
            "get_product_review": "self.control_review.get_product_review()"
        }
        if review in apis:
            return eval(apis[review])

        return APIS_WRONG
