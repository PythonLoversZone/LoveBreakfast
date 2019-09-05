# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from SharpGoods.config.response import APIS_WRONG
from SharpGoods.control.CUsers import CUsers

class SGUsers(Resource):
    def __init__(self):
        self.control_user = CUsers()

    def post(self, users):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(users))
        print("=======================api===================")

        apis = {
            "register":"self.control_user.register()",
            "login":"self.control_user.login()",
            "update_info":"self.control_user.update_info()",
            "update_pwd":"self.control_user.update_pwd()",
            "get_inforcode":"self.control_user.get_inforcode()",
            "forget_pwd":"self.control_user.forget_pwd()"
        }

        if users not in apis:
            return APIS_WRONG
        return eval(apis[users])

    def get(self, users):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(users))
        print("=======================api===================")

        apis = {
            "all_info":"self.control_user.all_info()"
        }

        if users not in apis:
            return APIS_WRONG
        return eval(apis[users])