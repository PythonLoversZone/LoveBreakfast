# *- coding:utf8 *-
import os
import sys

from flask_restful import Resource

from LoveBreakfast.config.Logs import PRINT_API_NAME
from LoveBreakfast.config.response import APIS_WRONG

sys.path.append(os.path.dirname(os.getcwd()))


class LBLocations(Resource):
    def __int__(self):
        self.apis_wrong = []

    @staticmethod
    def get(locations):
        print(PRINT_API_NAME.format(locations))

        apis = {
            "get_city_location": "control_location.get_city_location()"
        }

        if locations in apis:
            return eval(apis[locations])

        return APIS_WRONG
