# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from SharpGoods.config.response import APIS_WRONG
from SharpGoods.control.CReview import CReview

class SGReviews(Resource):
    def __init__(self):
        self.control_review = CReview()

    def post(self, review):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(review))
        print("=======================api===================")

        apis = {
            "create_review": "self.control_review.create_review()"
        }

        if review not in apis:
            return APIS_WRONG
        return eval(apis[review])

    def get(self, review):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(review))
        print("=======================api===================")
        apis = {
            "get_review": "self.control_review.get_review()"
        }
        if review not in apis:
            return APIS_WRONG
        return eval(apis[review])