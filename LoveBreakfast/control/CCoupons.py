# *- coding:utf8 *-
import datetime
import json
import os
import sys
import uuid

from flask import request

from LoveBreakfast.common.MakeToken import token_to_usid
from LoveBreakfast.common.import_status import import_status
from LoveBreakfast.common.lovebreakfast_error import dberror
from LoveBreakfast.common.timeformate import get_db_time_str, get_web_time_str, format_forweb_no_HMS
from LoveBreakfast.config.response import SYSTEM_ERROR, PARAMS_MISS

sys.path.append(os.path.dirname(os.getcwd()))


class CCoupons():
    def __init__(self):
        self.title = "============{0}==============="
        from LoveBreakfast.services.SCoupons import SCoupons
        self.scoupons = SCoupons()

    def add_cardpackage(self):
        args = request.args.to_dict()
        data = json.loads(request.data)

        if "token" not in args:
            return PARAMS_MISS
        token = args.get("token")
        uid = token_to_usid(token)

        couid = data.get("COid")

        try:
            cart_pkg = self.scoupons.get_card_by_uid_couid(uid, couid)
            cend = get_db_time_str()  # 后期补充优惠券截止日期计算方法
            if cart_pkg:
                if cart_pkg.CAstatus == 2:
                    return import_status("error_coupons_used", "LOVEBREAKFAST_ERROR", "error_coupons_used")

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

        return import_status("messages_add_coupons_success", "OK")

    def get_cart_pkg(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        token = args.get("token")
        uid = token_to_usid(token)

        try:
            cart_list = []
            cart_pkgs = self.scoupons.get_cardpackage_by_uid(uid)
            print(self.title.format("cart_pkgs"))
            print(cart_pkgs)
            print(self.title.format("cart_pkgs"))
            for cart_pkg in cart_pkgs:
                if cart_pkg.CAstatus == 2:
                    continue
                coupon = self.scoupons.get_coupons_by_couid(cart_pkg.COid)
                print(self.title.format("coupon"))
                print(coupon)
                print(self.title.format("coupon"))

                cart = {}
                COtype = coupon.COtype
                print(self.title.format("COtype"))
                print(COtype)
                print(self.title.format("COtype"))
                cart["CAid"] = cart_pkg.CAid
                cart["COid"] = cart_pkg.COid
                if COtype == 801:
                    COfilter = coupon.COfilter
                    cart["COuse"] = "满{0}元可用".format(COfilter)
                    COcut = coupon.COamount
                    cart["COcut"] = str(COcut) + "元"
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 802:
                    COfilter = coupon.COfilter
                    cart["COuse"] = "满{0}元可用".format(COfilter)
                    cart["COcut"] = str(coupon.COdiscount * 10) + "折"
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 803:
                    CObrand = coupon.CObrand.encode("utf8")
                    cart["COuse"] = "限{0}商品可用".format(str(CObrand))
                    cart["COcut"] = str(coupon.COamount) + "元"
                    COstart = coupon.COstart
                    cart["COstart"] = get_web_time_str(COstart, format_forweb_no_HMS)
                    COend = coupon.COend
                    cart["COend"] = get_web_time_str(COend, format_forweb_no_HMS)
                elif COtype == 804:
                    cart["COuse"] = "无限制"
                    cart["COcut"] = str(coupon.COamount) + "元"
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
        result = import_status("messages_get_carpkg_success", "OK")
        result["data"] = cart_list
        return result

    def check_carttime(self, cartpkg):
        time_now = datetime.datetime.now().date()
        if cartpkg.get("CAend") and \
                time_now > datetime.datetime.strptime(cartpkg.get("CAend"), format_forweb_no_HMS).date():
            return False
        if cartpkg.get("CAstart") and \
                time_now < datetime.datetime.strptime(cartpkg.get("CAstart"), format_forweb_no_HMS).date():
            return False
        if cartpkg.get("COend") and \
                time_now > datetime.datetime.strptime(cartpkg.get("COend"), format_forweb_no_HMS).date():
            return False
        if cartpkg.get("COstart") and \
                time_now < datetime.datetime.strptime(cartpkg.get("COstart"), format_forweb_no_HMS).date():
            return False
        return True
