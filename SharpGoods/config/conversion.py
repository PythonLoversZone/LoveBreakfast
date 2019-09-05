# *- coding:utf8 *-
conversion_PBunit = {401: "$", 402: "￥", 403: "欧元", 404: "英镑"}
conversion_PRtype = {501: "自营", 502: "非自营"}
conversion_PRbrand = {601: "美妆类", 602: "3C类"}
conversion_OMstatus = {0: "已取消", 7: "未支付", 14: "已支付", 21: "已接单",
                       28: "配送中", 35: "已装箱", 42: "已完成", 49: "已评价"}
conversion_COtype = {801: "满减", 802: "满折", 803: "商品类目限制", 804: "无限制", 805: "用户类型限制"}
# value 和 key 转置的dict
conversion_OMstatus_reverse = {v: k for k, v in conversion_OMstatus.items()}
conversion_PBunit_reverse = {v: k for k, v in conversion_PBunit.items()}
conversion_PRtype_reverse = {v: k for k, v in conversion_PRtype.items()}
conversion_PRbrand_reverse = {v: k for k, v in conversion_PRbrand.items()}


MTR = 1 / 6.3753
RTM = 1 / 0.1569
MTO = 1 / 0.8492
OTM = 1 / 1.1776
MTY = 1 / 0.7424
YTM = 1 / 1.347
RTO = 1 / 0.1332
OTR = 1 / 7.5082
RTY = 1 / 0.1163
YTR = 1 / 8.5958
OTY = 1 / 0.8742
YTO = 1 / 1.1439
