# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS
from SharpGoods.common.import_status import import_status

class CUsers():
    def __init__(self):
        from SharpGoods.service.SUsers import SUsers
        self.susers = SUsers()

    def register(self):
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "UStelphone" not in data or "USpassword" not in data or "UScode" not in data:
            return PARAMS_MISS

        list_utel = self.susers.get_all_user_tel()
        print "=================list_utel================="
        print list_utel
        print "=================list_utel================="
        if list_utel == False:
            return SYSTEM_ERROR
        if data["UStelphone"] in list_utel:
            return import_status("ERROR_MESSAGE_REPEAT_TELPHONE", "SHARPGOODS_ERROR", "ERROR_REPEAT_TELPHONE")

        code_in_db = self.susers.get_code_by_utel(data["UStelphone"])
        print "=================code_in_db================="
        print code_in_db
        print "=================code_in_db================="
        if not code_in_db:
            return import_status("ERROR_MESSAGE_WRONG_TELCODE", "SHARPGOODS_ERROR", "ERROR_WRONG_TELCODE")
        if code_in_db.ICcode != data["UScode"]:
            return import_status("ERROR_MESSAGE_WRONG_TELCODE", "SHARPGOODS_ERROR", "ERROR_WRONG_TELCODE")

        if "USinvate" in data:
            USinvate = data["USinvate"]
            #TODO 优惠券发放

        USinvatecode = self.make_invate_code()
        is_register = self.susers.login_users(data["UStelphone"], data["USpassword"], USinvatecode)
        print "=================is_register================="
        print is_register
        print "=================is_register================="
        if is_register:
            return import_status("SUCCESS_MESSAGE_REGISTER", "OK")
        else:
            return SYSTEM_ERROR

    def login(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "UStelphone" not in data or "USpassword" not in data:
            return PARAMS_MISS
        Utel = data["UStelphone"]
        list_utel = self.susers.get_all_user_tel()
        print "=================list_utel================="
        print list_utel
        print "=================list_utel================="
        if list_utel == False:
            return SYSTEM_ERROR

        if Utel not in list_utel:
            return import_status("ERROR_MESSAGE_NONE_TELPHONE", "SHARPGOODS_ERROR", "ERROR_NONE_TELPHONE")

        upwd = self.susers.get_upwd_by_utel(Utel)
        print "=================USpassword================="
        print upwd
        print "=================USpassword================="
        if upwd != data["USpassword"]:
            return import_status("ERROR_MESSAGE_WRONG_PASSWORD", "SHARPGOODS_ERROR", "ERROR_WRONG_PASSWORD")

        Uid = self.susers.get_uid_by_utel(Utel)
        print "=================USid================="
        print Uid
        print "=================USid================="
        login_success = import_status("SUCCESS_MESSAGE_LOGIN", "OK")
        login_success["data"] = {}
        login_success["data"]["token"] = Uid

        return login_success


    def update_info(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "token" not in args or data in ["", "{}"]:
            return PARAMS_MISS

        users = {}
        if "USname" in data:
            Uname = data["USname"]
            users["USname"] = Uname
        if "USsex" in data:
            Usex = data["USsex"]
            if Usex == "男".decode("UTF-8"):
                Usex = 101
            elif Usex == "女".decode("UTF-8"):
                Usex = 102
            users["USsex"] = Usex
        if users == {}:
            return PARAMS_MISS

        Uid = args["token"]
        update_info = self.susers.update_users_by_uid(Uid, users)
        print "=================update_info================="
        print update_info
        print "=================update_info================="
        if not update_info:
            return SYSTEM_ERROR

        response_of_update_users = import_status("SUCCESS_MESSAGE_UPDATE_PERSONAL", "OK")
        return response_of_update_users


    def update_pwd(self):
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "USpasswordold" not in data or "USpasswordnew" not in data or "UStelphone" not in data:
            return SYSTEM_ERROR

        Utel = data["UStelphone"]
        list_utel = self.susers.get_all_user_tel()
        print "=================list_utel================="
        print list_utel
        print "=================list_utel================="
        if list_utel == False:
            return SYSTEM_ERROR

        if Utel not in list_utel:
            return import_status("ERROR_MESSAGE_NONE_TELPHONE", "SHARPGOODS_ERROR", "ERROR_NONE_TELPHONE")

        upwd = self.susers.get_upwd_by_utel(Utel)
        print "=================USpassword================="
        print upwd
        print "=================USpassword================="
        if upwd != data["USpasswordold"]:
            return import_status("ERROR_MESSAGE_WRONG_PASSWORD", "SHARPGOODS_ERROR", "ERROR_WRONG_PASSWORD")
        users = {}
        Upwd = data["USpasswordnew"]
        users["USpassword"] = Upwd
        Uid = self.susers.get_uid_by_utel(Utel)
        update_info = self.susers.update_users_by_uid(Uid, users)
        print "=================update_info================="
        print update_info
        print "=================update_info================="
        if not update_info:
            return SYSTEM_ERROR

        response_of_update_users = import_status("SUCCESS_MESSAGE_UPDATE_PASSWORD", "OK")
        return response_of_update_users

    def forget_pwd(self):
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "USpasswordnew" not in data or "USpasswordnewrepeat" not in data or "UStelphone" not in data or "UScode" not in data:
            return SYSTEM_ERROR

        Utel = data["UStelphone"]
        list_utel = self.susers.get_all_user_tel()
        print "=================list_utel================="
        print list_utel
        print "=================list_utel================="
        if list_utel == False:
            return SYSTEM_ERROR

        if Utel not in list_utel:
            return import_status("ERROR_MESSAGE_NONE_TELPHONE", "SHARPGOODS_ERROR", "ERROR_NONE_TELPHONE")

        code_in_db = self.susers.get_code_by_utel(data["UStelphone"])
        print "=================code_in_db================="
        print code_in_db
        print "=================code_in_db================="
        if not code_in_db:
            return import_status("ERROR_MESSAGE_WRONG_TELCODE", "SHARPGOODS_ERROR", "ERROR_WRONG_TELCODE")
        if code_in_db.ICcode != data["UScode"]:
            return import_status("ERROR_MESSAGE_WRONG_TELCODE", "SHARPGOODS_ERROR", "ERROR_WRONG_TELCODE")

        if data["USpasswordnew"] != data["USpasswordnewrepeat"]:
            return import_status("ERROR_MESSAGE_WRONG_REPEAT_PASSWORD", "SHARPGOODS_ERROR", "ERROR_CODE_WRONG_REPEAT_PASSWORD")

        users = {}
        Upwd = data["USpasswordnew"]
        users["USpassword"] = Upwd
        Uid = self.susers.get_uid_by_utel(Utel)
        update_info = self.susers.update_users_by_uid(Uid, users)
        print "=================update_info================="
        print update_info
        print "=================update_info================="
        if not update_info:
            return SYSTEM_ERROR

        response_of_update_users = import_status("SUCCESS_MESSAGE_UPDATE_PASSWORD", "OK")
        return response_of_update_users

    def get_inforcode(self):
        data = request.data
        data = json.loads(data)
        print("=====================data=================")
        print(data)
        print("=====================data=================")
        if "UStelphone" not in data:
            return SYSTEM_ERROR
        Utel = data["UStelphone"]
        # 拼接验证码字符串（6位）
        code = ""
        while len(code) < 6:
            import random
            item = random.randint(1, 9)
            code = code + str(item)

        print("=====================code=================")
        print code
        print("=====================code=================")
        # 获取当前时间，与上一次获取的时间进行比较，小于60秒的获取直接报错
        import datetime
        time_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(time_time, "%Y%m%d%H%M%S")
        # 根据电话号码获取时间
        # utel_list = self.susers.get_all_user_tel()
        # print("=====================utel_list=================")
        # print utel_list
        # print("=====================utel_list=================")
        # if Utel in utel_list:
        #     return import_status("ERROR_MESSAGE_REGISTED_TELPHONE", "SHARPGOODS_ERROR", "ERROR_REGISTED_TELPHONE")
        time_up = self.susers.get_uptime_by_utel(Utel)
        print("=====================time_up=================")
        print time_up
        print("=====================time_up=================")
        if time_up:
            time_up_time = datetime.datetime.strptime(time_up.ICtime, "%Y%m%d%H%M%S")
            delta = time_time - time_up_time
            if delta.seconds < 60:
                return import_status("ERROR_MESSAGE_FAST_GET", "SHARPGOODS_ERROR", "ERROR_FAST_GET")

        new_inforcode = self.susers.add_inforcode(Utel, code, time_str)
        print("=====================new_inforcode=================")
        print new_inforcode
        print("=====================new_inforcode=================")
        if not new_inforcode:
            return SYSTEM_ERROR
        from SharpGoods.config.Inforcode import SignName, TemplateCode
        from SharpGoods.common.Inforsend import send_sms
        params = '{\"code\":\"' + code + '\",\"product\":\"etech\"}'

        # params = u'{"name":"wqb","code":"12345678","address":"bz","phone":"13000000000"}'
        import uuid
        __business_id = uuid.uuid1()
        response_send_message = send_sms(__business_id, Utel, SignName, TemplateCode, params)
        print("=====================response_send_message=================")
        print response_send_message
        print("=====================response_send_message=================")
        response_send_message = json.loads(response_send_message)

        if response_send_message["Code"] == "OK":
            status = 200
            message = "获取成功"
        else:
            status = 405
            message = "获取验证码失败"
        response_ok = {}
        response_ok["status"] = status
        response_ok["message"] = message

        return response_ok

    def all_info(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "token" not in args:
            return PARAMS_MISS
        Uid = args["token"]
        users_info = self.susers.get_all_users_info(Uid)
        print "=================users_info================="
        print users_info
        print "=================users_info================="
        if not users_info:
            return SYSTEM_ERROR

        response_user_info = {}
        Utel = users_info.UStelphone
        response_user_info["UStelphone"] = Utel
        if users_info.USname not in ["", None]:
            Uname = users_info.USname
            response_user_info["USname"] = Uname
        else:
            response_user_info["USname"] = None
        if users_info.USsex not in ["", None]:
            Usex = users_info.USsex
            if Usex == 101:
                response_user_info["USsex"] = "男"
            elif Usex == 102:
                response_user_info["USsex"] = "女"
            else:
                response_user_info["USsex"] = "未知性别"
        else:
            response_user_info["USsex"] = None
        response_user_info["UScoin"] = users_info.UScoin
        response_user_info["USinvate"] = users_info.USinvate

        response_of_get_all = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response_of_get_all["data"] = response_user_info
        return response_of_get_all

    def make_invate_code(self):
        USinvate = self.susers.get_all_invate_code()
        while True:
            invate_code = self.make_random_code()
            if invate_code not in USinvate:
                break
        return invate_code

    def make_random_code(self):
        import random
        random_code = ""
        while len(random_code) < 2:
            a = random.randint(97, 122)
            a = chr(a)
            random_code = random_code + a
        while len(random_code) < 6:
            a = random.randint(0, 9)
            random_code = random_code + str(a)
        return random_code

if __name__ == '__main__':
    users = CUsers()
    print users.make_invate_code()