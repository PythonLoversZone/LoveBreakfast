# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid
from SharpGoods.common.lovebreakfast_error import dberror
from SharpGoods.common.TransformToList import add_model
from SharpGoods.common.import_status import import_status
from SharpGoods.common.get_str import get_str
from SharpGoods.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR


class CCarts():
    def __init__(self):
        from SharpGoods.service.SCarts import SCarts
        self.scarts = SCarts()
        from SharpGoods.service.SProduct import SProduct
        self.sproduct = SProduct()
        from SharpGoods.service.SUsers import SUsers
        self.suser = SUsers()

    def del_cart(self):
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
        user = self.suser.get_usname_by_usid(get_str(args, "token"))
        if not user:
            return TOKEN_ERROR

        pbid = data.get("PBid")
        try:
            cart = self.scarts.get_cart_by_uid_pid(uid, pbid)
            print "=================cart================="
            print cart
            print "=================cart================="
            if not cart:
                return import_status("ERROR_MESSAGE_NONE_PRODUCT", "SHARPGOODS_ERROR", "ERROR_NONE_PRODUCT")
            self.scarts.del_carts(cart.CAid)
            return import_status("SUCCESS_MESSAGE_DEL_CART", "OK")
        except Exception as e:
            print(e.message)
            return SYSTEM_ERROR

    def add_or_update_cart(self):
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
        pbid = data.get("PBid")
        CAnumber = data.get("CAnumber")
        if CAnumber <= 0:
            PBnumber = self.scarts.get_pbnumber_by_pbid_and_usid(pbid, uid)
            pnum = int(CAnumber) + int(PBnumber)
            if pnum <= 0:
                return self.del_cart()
        try:
            if not self.sproduct.get_product_by_pbid(pbid):
                return import_status("ERROR_MESSAGE_NONE_PRODUCT", "SHARPGOODS_ERROR", "ERROR_NONE_PRODUCT")
            cart = self.scarts.get_cart_by_uid_pid(uid, pbid)
            print "=================cart================="
            print cart
            print "=================cart================="
            if cart:
                PBnumber = self.scarts.get_pbnumber_by_pbid_and_usid(pbid, uid)
                pnum = int(CAnumber) + int(PBnumber)
                self.scarts.update_num_cart(pnum, cart.CAid)
            else:
                self.scarts.add_model("Cart",
                          **{
                              "CAid": str(uuid.uuid4()),
                              "CAnumber": CAnumber,
                              "USid": uid,
                              "CAstatus": 1,
                              "PBid": pbid
                          })
        except dberror:
            return SYSTEM_ERROR
        except Exception as e:
            print(e.message)
            return SYSTEM_ERROR

        add_update_cart_ok = import_status("SUCCESS_MESSAGE_ADD_UPDATE_CART", "OK")
        return add_update_cart_ok

    def get_carts_by_uid(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "token" not in args:
            return PARAMS_MISS

        # todo uid 验证未实现
        uid = args["token"]
        # res_get_all = {}

        cart_info_list = []
        cart_list = self.scarts.get_carts_by_Uid(uid)
        print "=================cart_list================="
        print cart_list
        print "=================cart_list================="
        for cart in cart_list:
            if cart.CAstatus != 1:
                continue
            cart_service_info = self.sproduct.get_product_by_pbid(cart.PBid)
            print "=================cart_service_info================="
            print cart_service_info
            print "=================cart_service_info================="
            if not cart_service_info:
                return SYSTEM_ERROR
            PRid = cart_service_info.PRid
            BRid = cart_service_info.BRid
            product = self.sproduct.get_product_by_prid(PRid)
            print "=================product================="
            print product
            print "=================product================="
            if not product:
                return SYSTEM_ERROR
            cart_info = {}
            cart_info["PRquality"] = {}
            quality_list = self.sproduct.get_all_brand_by_brid_last(BRid)
            #cart_info["PRquality"] = self.sproduct.get_all_brand_by_brid_last(BRid)
            for key in quality_list.keys():
                cart_info["PRquality"][key] = {}
                cart_info["PRquality"][key]["name"] = self.choose_key(key)
                cart_info["PRquality"][key]["choice"] = []
                cart_info["PRquality"][key]["choice"].append(quality_list[key])
            cart_info["PBid"] = cart.PBid
            cart_info["PBimage"] = cart_service_info.PBimage
            cart_info["PBsalesvolume"] = cart_service_info.PBsalesvolume
            cart_info["PBprice"] = cart_service_info.PBprice
            cart_info["CAid"] = cart.CAid
            PBunit = cart_service_info.PBunit
            if PBunit == 401:
                cart_info["PBunit"] = "$"
            elif PBunit == 402:
                cart_info["PBunit"] = "￥"
            elif PBunit == 403:
                cart_info["PBunit"] = "欧元"
            elif PBunit == 404:
                cart_info["PBunit"] = "英镑"
            else:
                cart_info["PBunit"] = "其他币种"
            cart_info["PBscore"] = cart_service_info.PBscore
            cart_info["CAnumber"] = cart.CAnumber
            cart_info["PRname"] = product.PRname
            cart_info["PRinfo"] = product.PRinfo
            PRbrand = product.PRbrand
            if PRbrand == 601:
                cart_info["PRbrand"] = "美妆类"
            elif PRbrand == 602:
                cart_info["PRbrand"] = "3C类"
            else:
                cart_info["PRbrand"] = "其他"
            cart_info["PRvideo"] = product.PRvideo
            PRtype = product.PRtype
            if PRtype == 501:
                cart_info["PRtype"] = "自营"
            elif PRtype == 502:
                cart_info["PRtype"] = "非自营"
            else:
                cart_info["PRtype"] = "未知商品"
            cart_info_list.append(cart_info)
        res_get_all = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        res_get_all["data"] = cart_info_list
        return res_get_all

    def get_carts_by_uid_caid(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "token" not in args:
            return PARAMS_MISS

        data = json.loads(request.data, encoding="utf8")
        caidlist = data.get("CAid")

        # todo uid 验证未实现
        uid = args["token"]
        # res_get_all = {}

        cart_info_list = []
        cart_list = self.scarts.get_carts_by_Uid(uid)
        print "=================cart_list================="
        print cart_list
        print "=================cart_list================="
        for cart in cart_list:
            if cart.CAstatus != 1:
                continue
            if caidlist and cart.CAid not in caidlist:
                continue
            cart_service_info = self.sproduct.get_product_by_pbid(cart.PBid)
            print "=================cart_service_info================="
            print cart_service_info
            print "=================cart_service_info================="
            if not cart_service_info:
                return SYSTEM_ERROR
            PRid = cart_service_info.PRid
            BRid = cart_service_info.BRid
            product = self.sproduct.get_product_by_prid(PRid)
            print "=================product================="
            print product
            print "=================product================="
            if not product:
                return SYSTEM_ERROR
            cart_info = {}
            cart_info["PRquality"] = {}
            quality_list = self.sproduct.get_all_brand_by_brid_last(BRid)

            for key in quality_list.keys():
                cart_info["PRquality"][key] = {}
                cart_info["PRquality"][key]["name"] = self.choose_key(key)
                cart_info["PRquality"][key]["choice"] = []
                cart_info["PRquality"][key]["choice"].append(quality_list[key])
            cart_info["PBid"] = cart.PBid
            cart_info["PBimage"] = cart_service_info.PBimage
            cart_info["PBsalesvolume"] = cart_service_info.PBsalesvolume
            cart_info["PBprice"] = cart_service_info.PBprice
            PBunit = cart_service_info.PBunit
            if PBunit == 401:
                cart_info["PBunit"] = "$"
            elif PBunit == 402:
                cart_info["PBunit"] = "￥"
            elif PBunit == 403:
                cart_info["PBunit"] = "欧元"
            elif PBunit == 404:
                cart_info["PBunit"] = "英镑"
            else:
                cart_info["PBunit"] = "其他币种"
            cart_info["PBscore"] = cart_service_info.PBscore
            cart_info["CAnumber"] = cart.CAnumber
            cart_info["PRname"] = product.PRname
            cart_info["PRinfo"] = product.PRinfo
            PRbrand = product.PRbrand
            if PRbrand == 601:
                cart_info["PRbrand"] = "美妆类"
            elif PRbrand == 602:
                cart_info["PRbrand"] = "3C类"
            else:
                cart_info["PRbrand"] = "其他"
            cart_info["PRvideo"] = product.PRvideo
            PRtype = product.PRtype
            if PRtype == 501:
                cart_info["PRtype"] = "自营"
            elif PRtype == 502:
                cart_info["PRtype"] = "非自营"
            else:
                cart_info["PRtype"] = "未知商品"
            cart_info_list.append(cart_info)
        res_get_all = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        res_get_all["data"] = cart_info_list
        return res_get_all

    def choose_key(self, BRkey):
        if BRkey == "BRno":
            return "版本选择"
        elif BRkey == "BRcolor":
            return "颜色选择"
        else:
            return "未知类目"