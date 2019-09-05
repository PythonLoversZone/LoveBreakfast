# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

from flask import request
import json
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS
from SharpGoods.common.import_status import import_status
from SharpGoods.service.SLocations import SLocations
from SharpGoods.common.get_model_return_list import get_model_return_list, get_model_return_dict
from SharpGoods.common.get_str import get_str

class CLocations():
    def __init__(self):
        self.slocation = SLocations()
        self.params_list = ["LOno", "LOname", "LOtelphone", "LOdetail", "LOprovince", "LOcity", "LOarea", "LOid"]
        self.params_list2 = ["LOno", "LOname", "LOtelphone", "LOdetail", "LOprovince", "LOcity", "LOarea"]
        self.title = '============{0}============'

    def get_all_location(self):
        args = request.args.to_dict()
        print(self.title.format("args dict"))
        print(args)
        print(self.title.format("args dict"))
        if "token" not in args or not args.get("token"):
            return PARAMS_MISS
        data = import_status("SUCCESS_MESSAGE_GET_LOCATIONS", "OK")
        print(self.title.format("Location list"))
        print(get_model_return_list(self.slocation.get_all(args.get("token"))))
        data["data"] = get_model_return_list(self.slocation.get_all(args.get("token")))
        print(self.title.format("Location list"))
        return data

    def new_location(self):
        args = request.args.to_dict()
        print(self.title.format("args dict"))
        print(args)
        print(self.title.format("args dict"))
        print(self.title.format("data dict"))
        data = request.data
        data = json.loads(data)
        print(data)
        print(self.title.format("data dict"))
        if "token" not in args:
            return PARAMS_MISS

        location = {}
        for key in self.params_list2:
            if key not in data:
                return PARAMS_MISS
            location[key] = get_str(data, key)

        try:
            location["LOisedit"] = 301
            import uuid
            location["LOid"] = str(uuid.uuid4())
            location["USid"] = get_str(args, "token")
            result = self.slocation.add_model("Locations", **location)
            print(self.title.format("result boolean"))
            print(result)
            print(self.title.format("result boolean"))
            if result:
                return import_status("SUCCESS_MESSAGE_ADD_LOCATION", "OK")
            return SYSTEM_ERROR
        except Exception as e:
            print(self.title.format("add location error"))
            print(e.message)
            print(self.title.format("add location error"))
            return SYSTEM_ERROR

    def update_location(self):
        args = request.args.to_dict()
        print(self.title.format("args dict"))
        print(args)
        print(self.title.format("args dict"))
        print(self.title.format("data dict"))
        data = request.data
        data = json.loads(data)
        print(data)
        print(self.title.format("data dict"))

        if "token" not in args or "LOid" not in data:
            return PARAMS_MISS

        if not set(self.params_list).issuperset(data.keys()):
            print("the params is contains key out of {0}".format(self.params_list))
            return import_status("ERROR_MESSAGE_UPDATE_LOCATION_URL", "SHARPGOODS_ERROR", "ERROR_PARAMS")

        try:
            location = get_model_return_dict(self.slocation.get_location_by_loid(get_str(data, "LOid")))
            if location.get("LOisedit") != 301:
                return import_status("ERROR_MESSAGE_NO_ROLE_UPDATE_LOCATION", "SHARPGOODS_ERROR", "ERROR_ROLE")

            for key in data:
                location[key] = get_str(data, key)

            self.slocation.update_locations_by_loid(get_str(data, "LOid"), location)
            return import_status("SUCCESS_MESSAGE_UPDSTE_LOCATION", "OK")
        except Exception as e:
            print(self.title.format("update location error"))
            print(e.message)
            print(self.title.format("update location error"))
            return SYSTEM_ERROR

    def del_location(self):
        args = request.args.to_dict()
        print(self.title.format("args dict"))
        print(args)
        print(self.title.format("args dict"))

        if "token" not in args or "LOid" not in args:
            return PARAMS_MISS
        try:
            location = get_model_return_dict(self.slocation.get_location_by_loid(get_str(args, "LOid")))
            if location.get("LOisedit") != "301":
                return import_status("ERROR_MESSAGE_NO_ROLE_UPDATE_LOCATION", "SHARPGOODS_ERROR", "ERROR_ROLE")
            self.slocation.update_locations_by_loid(args.get("LOid"), {"LOisedit": 303})
            return import_status("SUCCESS_MESSAGE_DELETE_LOCATION", "OK")
        except Exception as e:
            print(self.title.format("del location error"))
            print(e.message)
            print(self.title.format("del location error"))
            return SYSTEM_ERROR
