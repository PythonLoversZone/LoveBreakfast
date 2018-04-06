# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from config.status import response_ok

class COrders():

    def __int__(self):
        from config.status import response_error
        from config.status_code import error_param_miss
        from config.messages import error_messages_param_miss
        self.param_miss = {}
        self.param_miss["status"] = response_error
        self.param_miss["status_code"] = error_param_miss
        self.param_miss["messages"] = error_messages_param_miss

        from config.status import response_system_error
        from config.messages import error_system_error
        self.system_error = {}
        self.system_error["status"] = response_system_error
        self.system_error["messages"] = error_system_error

        from services.SOrders import SOrders
        self.sorders = SOrders()

        from services.SProduct import SProduct
        self.sproduct = SProduct()

    def get_order_list(self):
        pass

    def get_order_abo(self):
        pass

    def make_main_order(self):
        args = request.args.to_dict()
        data = request.data

        if "token" not in args:
            return self.param_miss

        if "Otime" not in data or "Otruetimemin" not in data or "Otruetimemax" not in data:
            return self.param_miss

        if "order_items" not in data:
            return self.system_error
        Uid = args["token"]
        Otime = data["Otime"]
        Otruetimemin = data["Otruetimemin"]
        Otruetimemax = data["Otruetimemax"]
        Ostatus = 5

        if "Lname" not in data or "Lno" not in data or "Lboxno" not in data:
            from config.status import response_error
            from config.status_code import error_no_location
            from config.messages import messages_no_location
            no_location = {}
            no_location["status"] = response_error
            no_location["status_code"] = error_no_location
            no_location["messages"] = messages_no_location
            return no_location

        Lname = data["Lname"]
        Lno = data["Lno"]
        Lboxno = data["Lboxno"]

        Lid = self.sorders.get_lid_by_lname_lno_lboxno(Lname, Lno, Lboxno)
        if not Lid:
            return self.system_error
        Oabo = None
        if "Oabo" in data:
            Oabo = data["Labo"]

        add_main_order = self.sorders.add_main_order(Otime, Otruetimemin, Otruetimemax, Ostatus, None, Uid, Lid, Oabo)
        if not add_main_order:
            return self.system_error

        order_item = data["order_items"]
        add_order_items_by_uid = self.add_order_items(order_item, add_main_order)

        from config.messages import messages_add_main_order_success
        response_make_main_order = {}
        response_make_main_order["status"] = response_ok
        response_make_main_order["messages"] = messages_add_main_order_success
        return response_make_main_order

    def add_order_items(self, order_item_list, oid):

        order_item_list = json.loads(order_item_list)
        order_price = 0
        for row in order_item_list:
            Pid = row["Pid"]
            Pnum = row["Pnum"]
            add_order_item = self.sorders.add_order_item(oid, Pid, Pnum)
            if not add_order_item:
                return self.system_error
            order_item_price = self.sproduct.get_pprice_by_pid(Pid)
            if not order_item_price:
                return self.system_error
            order_price = order_price + order_item_price

        update_main_order = {}
        update_main_order["Oprice"] = order_price
        response_update_main_order = self.sorders.update_price_by_oid(oid, update_main_order)

        if not response_update_main_order:
            return self.system_error

        return True

    def update_order_info(self):
        pass

    def update_order_status(self):
        args = request.args.to_dict()
        data = request.data

        if "token" not in args:
            return self.param_miss
        if "Ostatus" not in data or "Oid" not in data:
            return self.param_miss

        # 处理token过程，这里未设计

        Ostatus = data["Ostatus"]

        Ostatus_list = [5, 10, 15, 20, -1]
        if Ostatus not in Ostatus_list:
            from config.status import response_error
            from config.status_code import error_wrong_status_code
            from config.messages import messages_error_wrong_status_code
            wrong_status_code = {}
            wrong_status_code["status"] = response_error
            wrong_status_code["status_code"] = error_wrong_status_code
            wrong_status_code["messages"] = messages_error_wrong_status_code
            return wrong_status_code
        Oid = data["Oid"]

        update_ostatus = {}
        update_ostatus["Ostatus"] = Ostatus

        response_update_order_status = self.sorders.update_status_by_oid(Oid, update_ostatus)

        if not response_update_order_status:
            return self.system_error

        from config.messages import messages_update_order_status_ok
        update_order_status_ok = {}
        update_order_status_ok["status"] = response_ok
        update_order_status_ok["messages"] = messages_update_order_status_ok

        return update_order_status_ok