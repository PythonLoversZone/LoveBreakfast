# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.config.response import APIS_WRONG

sys.path.append(os.path.dirname(os.getcwd()))


class LBUsers(Resource):
    def __init__(self):
        pass

    @staticmethod
    def post(users):
        print(PRINT_API_NAME.format(users))

        apis = {
            "register": "control_user.register()",
            "login": "control_user.login()",
            "update_info": "control_user.update_info()",
            "update_pwd": "control_user.update_pwd()",
            "get_inforcode": "control_user.get_inforcode()",
            "forget_pwd": "control_user.forget_pwd()"
        }

        if users in apis:
            return eval(apis[users])

        return APIS_WRONG

    @staticmethod
    def get(users):
        print(PRINT_API_NAME.format(users))

        apis = {
            "all_info": "control_user.all_info()"
        }

        if users in apis:
            return eval(apis[users])

        return APIS_WRONG
