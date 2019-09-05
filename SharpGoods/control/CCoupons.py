# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS
from SharpGoods.common.get_model_return_list import get_model_return_list
from SharpGoods.common.timeformate import get_web_time_str, format_forweb_no_HMS
from SharpGoods.common.import_status import import_status
import json


class CCoupons():
    def __init__(self):
        from SharpGoods.service.SCoupons import SCoupons
        self.scoupons = SCoupons()

    def get_cart_pkg(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "token" not in args:
            return PARAMS_MISS
        uid = args.get("token")

        try:
            cart_list = []
            cart_pkgs = self.scoupons.get_cardpackage_by_uid(uid)
            print "=================cart_pkgs================="
            print cart_pkgs
            print "=================cart_pkgs================="
            for cart_pkg in cart_pkgs:
                if cart_pkg.CAstatus == 2:
                    continue
                coupon = self.scoupons.get_coupons_by_couid(cart_pkg.COid)
                print "=================coupon================="
                print coupon
                print "=================coupon================="
                cart = {}
                COtype = coupon.COtype
                print "=================COtype================="
                print COtype
                print "=================COtype================="
                cart["CAid"] = cart_pkg.CAid
                if COtype == 801:
                    COfilter = coupon.COfilter
                    cart["COuse"] = "满{0}元可用".format(COfilter)
                    cart["COcut"] = coupon.COamount
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 802:
                    COfilter = coupon.COfilter
                    cart["COuse"] = "满{0}元可用".format(COfilter)
                    cart["COcut"] = str(coupon.COdiscount * 100) + "%"
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 803:
                    CObrand = coupon.CObrand.encode("utf8")
                    cart["COuse"] = "限{0}商品可用".format(str(CObrand))
                    cart["COcut"] = coupon.COamount
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 804:
                    cart["COuse"] = "无限制"
                    cart["COcut"] = coupon.COamount
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                else:
                    return
                cart_list.append(cart)
        except Exception as e:
            print("ERROR: " + e.message)
            return SYSTEM_ERROR
        response = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = cart_list
        return response

    def get_cart_pkg_by_pblst(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "token" not in args:
            return PARAMS_MISS
        uid = args["token"]
        data = json.loads(request.data)
        print "=================data================="
        print data
        print "=================data================="
        if "PBid" not in data and "OMprice" not in data:
            return PARAMS_MISS
        try:
            cart_list = []
            cart_pkgs = get_model_return_list(self.scoupons.get_cardpackage_by_uid(uid))
            print "=================cart_pkgs================="
            print cart_pkgs
            print "=================cart_pkgs================="
            for cart_pkg in cart_pkgs:
                if cart_pkg.get("CAstatus") == 2:
                    continue
                coupon = self.scoupons.get_coupons_by_couid(cart_pkg.get("COid"))
                print "=================coupon================="
                print coupon
                print "=================coupon================="
                cart = {}
                cart["CAid"] = cart_pkg.CAid
                COtype = coupon.COtype
                cart["COtype"] = COtype
                if COtype == 801:
                    cart["COuse"] = "满{0}元可用".format(coupon.COfilter)
                    cart["COcut"] = coupon.COamount
                    cart["COstart"] = get_web_time_str(coupon.COstart, format_forweb_no_HMS)
                    cart["COend"] = get_web_time_str(coupon.COend, format_forweb_no_HMS)
                elif COtype == 802:
                    cart["COuse"] = "满{0}元可用".format(coupon.COfilter)
                    cart["COcut"] = str(coupon.COdiscount * 100) + "%"
                    cart["COstart"] = get_web_time_str(coupon.COstart, format_forweb_no_HMS)
                    cart["COend"] = get_web_time_str(coupon.COend, format_forweb_no_HMS)
                elif COtype == 803:
                    cart["COuse"] = "限{0}商品可用".format(coupon.CObrand)
                    cart["COcut"] = coupon.COamount
                    cart["COstart"] = get_web_time_str(coupon.COstart, format_forweb_no_HMS)
                    cart["COend"] = get_web_time_str(coupon.COend, format_forweb_no_HMS)
                elif COtype == 804:
                    cart["COuse"] = "无限制"
                    cart["COcut"] = coupon.COamount
                    cart["COstart"] = get_web_time_str(coupon.COstart, format_forweb_no_HMS)
                    cart["COend"] = get_web_time_str(coupon.COend, format_forweb_no_HMS)
                cart_list.append(cart_pkg)
        except Exception as e:
            print("ERROR: " + e.message)
            return SYSTEM_ERROR
        for pbid in data:
            pass
        response = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = cart_list
        return response


"""
    def add_cardpackage(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = json.loads(request.data)
        print "=================data================="
        print data
        print "=================data================="

        if "token" not in args:
            return PARAMS_MISS
        uid = args.get("token")
        couid = data.get("Couid")

        try:
            cart_pkg = self.scoupons.get_card_by_uid_couid(uid, couid)
            cend = get_db_time_str()  # 后期补充优惠券截止日期计算方法
            if cart_pkg:
                if cart_pkg.CAstatus == 2:
                    from config.status import response_error as status
                    from config.status_code import error_coupon_used as code
                    from config.messages import error_coupons_used as msg
                    return {"status": status, "status_code": code, "message": msg}
                self.scoupons.update_carbackage(cart_pkg.CAid)
            else:
                self.scoupons.add_cardpackage(**{
                    "CAid": str(uuid.uuid4()),
                    "USid": uid,
                    "CAstatus": 1,
                    "CAstart": get_db_time_str(),
                    "CAend": cend,
                    "COid": couid
                })
        except dberror:
            return SYSTEM_ERROR
        except Exception as e:
            print(e.message)
            return SYSTEM_ERROR

        from config.messages import messages_add_coupons_success as msg
        return {"status": ok, "message": msg}
"""
