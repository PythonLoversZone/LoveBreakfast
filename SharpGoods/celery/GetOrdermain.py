# *- coding:utf8 *-
import sys
import os
import datetime
import xlwt

sys.path.append("/opt")
from SharpGoods.common.timeformate import fomat_for_db
from SharpGoods.common.get_model_return_list import get_model_return_list, get_model_return_dict

import platform


class GetOrdermain():
    def __init__(self):
        from SharpGoods.service.SOrders import SOrders
        self.sorder = SOrders()
        from SharpGoods.service.SUsers import SUsers
        self.suser = SUsers()
        from SharpGoods.service.SLocations import SLocations
        self.sloc = SLocations()
        self.title = "==========={0}==========="
        self.exceltitle = ["LOname", "LOtelphone", "LOno", "LOprovince", "LOcity",
                           "LOarea", "LOdetail", "OMabo", "OMtime"]

    def print_log(self, name, value):
        print(self.title.format(name))
        print(value)
        print(self.title.format(name))

    def task(self):
        print("run task")
        start = datetime.datetime.now()
        end = start - datetime.timedelta(days=1)

        start = start.strftime(fomat_for_db)
        end = end.strftime(fomat_for_db)
        self.print_log("start", start)
        self.print_log("end", end)

        order_list = get_model_return_list(self.sorder.get_order_main_list(start, end))
        for ordermain in order_list:
            location = get_model_return_dict(self.sloc.get_location_by_loid(ordermain.get("LOid")))
            self.print_log("location", location)
            ordermain.update(location)
        file_path = "/tmp/sharpgoodsorder"
        if platform.system().lower() == "windows":
            file_path = r"d:\sharpgoodsorder"

        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        name = "ordermain{0}-{1}.xlsx".format(start, end)
        filename = os.path.join(file_path, name)
        wb = xlwt.Workbook()
        ws = wb.add_sheet("ordermain")
        line = 0
        # init excel
        for index, title in enumerate(self.exceltitle):
            ws.write(line, index, title)

        line += 1
        for index, value in enumerate(order_list):
            print (index, value)
            for i, title in enumerate(self.exceltitle):
                ws.write(line, i, value.get(title))
            line += 1
        wb.save(filename)

#     def timer(self):
#         print("start")
#         flag = False
#         stime = datetime.datetime(2018, 6, 20, 9, 39)
#         stime_bk = datetime.datetime(2018, 6, 20, 9)
#         while True:
#             now = datetime.datetime.now()
#             if now.year == stime.year and now.day == stime.day and now.hour == stime.hour and now.minute == stime.minute:
#                 self.task(stime_bk, stime)
#                 stime_bk = stime
#                 flag = True
#             elif now > stime:
#                 self.task(stime, now)
#                 stime_bk = now
#                 stime = now
#
#                 flag = True
#             if flag:
#                 stime = stime + datetime.timedelta(days=1)
#                 flag = False
#             time.sleep(3600)

if __name__ == "__main__":
    GetOrdermain().task()
    # start = datetime.datetime(2018, 6, 1, 0, 0, 0)
    # end = datetime.datetime(2018, 6, 19, 0, 0, 0)
    # GetOrdermain().task(start, end)
