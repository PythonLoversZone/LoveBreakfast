# *- coding:utf8 *-
# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd())) # 增加系统路径
#引用python类
from flask import request
import json
#引用项目类

from SharpGoods.common.get_str import get_str
from SharpGoods.common.import_status import import_status
from SharpGoods.service.SReview import SReview
from SharpGoods.common.timeformate import get_web_time_str
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS

class CReview():
    def __init__(self):
        self.service_review = SReview()
        from SharpGoods.service.SOrders import SOrders
        self.sorder = SOrders()
        from SharpGoods.service.SProduct import SProduct
        self.sproduct = SProduct()
        from SharpGoods.service.SUsers import SUsers
        self.suser = SUsers()

    #  创建评论
    def create_review(self):
        args = request.args.to_dict()  # 捕获前端的URL参数，以字典形式呈现
        print "=================args================="
        print args
        print "=================args================="
        # 判断url参数是否异常
        if "token" not in args and "OMid" not in args:
            return PARAMS_MISS
        Uid = args["token"]
        OMid = args["OMid"]

        uid = self.sorder.get_uid_by_omid(OMid)
        print "=================uid================="
        print uid
        print "=================uid================="
        omstatus = self.sorder.get_omstatus_by_omid(OMid)
        print "=================omstatus================="
        print omstatus
        print "=================omstatus================="
        if uid != Uid:
            return import_status("ERROR_MESSAGE_NONE_PERMISSION", "SHARPGOODS_ERROR", "ERROR_NONE_PERMISSION")
        if omstatus != 42:
            return import_status("ERROR_MESSAGE_WRONG_STATUS", "SHARPGOODS_ERROR", "ERROR_WRONG_STATUS")

        data = json.loads(request.data)
        print "=================data================="
        print data
        print "=================data================="
        if data == []:
            return PARAMS_MISS
        for review in data:
            if "PBid" not in review or "REcontent" not in review or "REscore" not in review:
                return PARAMS_MISS
            PRid = self.sproduct.get_prid_by_pbid(review["PBid"])
            print "=================PRid================="
            print PRid
            print "=================PRid================="
            REcontent = review["REcontent"]
            add_review = self.service_review.new_review(PRid, uid, REcontent)
            if not add_review:
                return SYSTEM_ERROR
            product = self.sproduct.get_volue_score_by_pbid(review["PBid"])
            print "=================product================="
            print product
            print "=================product================="
            PBscore,PBvolue = product.PBscore, product.PBsalesvolume
            score = (review["REscore"] + PBscore * PBvolue)/PBvolue
            product_brand = {}
            product_brand["PBid"] = review["PBid"]
            product_brand["PBscore"] = score
            update_product = self.sproduct.update_score_by_pbid(review["PBid"], product_brand)
            if not update_product:
                return SYSTEM_ERROR
        order_main = {}
        order_main["OMstatus"] = 49
        update_order_status = self.sorder.update_omstatus_by_omid(OMid, order_main)
        if not update_order_status:
            return SYSTEM_ERROR
        return import_status("SUCCESS_MESSAGE_NEW_REVIEW", "OK")

    # 根据Oid获取商品评论
    def get_review(self):
        args = request.args.to_dict()  # 捕获前端的URL参数，以字典形式呈现
        print "=================args================="
        print args
        print "=================args================="
        # 判断url参数是否异常
        if "PRid" not in args:
            return PARAMS_MISS
        PRid = args["PRid"]
        PBid_list = self.sproduct.get_pbid_by_prid(PRid)
        review_list = []
        all_review = self.service_review.get_review_by_pbid(PRid)
        print "=================all_review================="
        print all_review
        print "=================all_review================="
        if all_review:
            for review in all_review:
                reviews = {}
                REid = review.REid
                REtime = review.REtime
                REtime = get_web_time_str(REtime)
                USid = review.USid
                REcontent = review.REcontent
                USname = self.suser.get_usname_by_usid(USid)
                print "=================USname================="
                print USname
                print "=================USname================="
                reviews["REid"] = REid
                reviews["REtime"] = REtime
                reviews["USname"] = USname
                reviews["REcontent"] = REcontent
                review_list.append(reviews)
        response = import_status("SUCCESS_MESSAGE_GET_REVIEW", "OK")
        response["data"] = review_list
        return response

    # def get_user_review(self):
    #     args = request.args.to_dict()  # 捕获前端的URL参数，以字典形式呈现
    #     # 判断url参数是否异常
    #     if len(args) != 1 or "Uid" not in args.keys():
    #         message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
    #         return {
    #             "message": message,
    #             "status": status,
    #             "statuscode": statuscode,
    #         }
    #     uid_to_str = get_str(args, "Uid")
    #     uid_list = []
    #     if uid_to_str not in uid_list:
    #         message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
    #         return {
    #             "message": message,
    #             "status": status,
    #             "statuscode": statuscode,
    #         }
    #     review_of_control = self.service_review.get_user_review(uid_to_str)
    #     review_list = []
    #     for i in range(len(review_of_control)):
    #         dict_of_review = {}
    #         dict_of_review["Rid"] = review_of_control[i].get("Rid")
    #         dict_of_review["Rpname"] = review_of_control[i].get("Rpname")
    #         dict_of_review["Rpimage"] = review_of_control[i].get("Rpimage")
    #         dict_of_review["Rscore"] = review_of_control[i].get("Rscore")
    #         dict_of_review["Rcontent"] = review_of_control[i].get("Rcontent")
    #         review_list.append(dict_of_review)
    #     return {
    #         "message": "get user revirew success !",
    #         "status": 200,
    #         "statuscode": review_list
    #     }

    def delete_user_review(self):
        args = request.args.to_dict()  # 捕获前端的URL参数，以字典形式呈现
        # 判断url参数是否异常
        if len(args) != 1 or "Uid" not in args.keys() or "Rid" not in args.keys():
            message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        uid_to_str = get_str(args, "Uid")
        uid_list = []
        if uid_to_str not in uid_list:
            message, status, statuscode = import_status("URL_PARAM_WRONG", "response_error", "URL_PARAM_WRONG")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        rid_to_str = get_str(args, "Rid")
        rid_list = self.service_review.get_rid_by_uid(uid_to_str)
        if rid_to_str not in rid_list:
            message, status, statuscode = import_status("NO_THIS_REVIEW", "response_error", "NO_THIS_REVIEW")
            return {
                "message": message,
                "status": status,
                "statuscode": statuscode,
            }
        result = self.service_review.delete_user_review(rid_to_str)
        print(request)
        return {
            "message": "delete review success !",
            "status": 200,
        }