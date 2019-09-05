# *- coding:utf8 *-
"""
获取对应宽高比图片的文件夹
目前是
大于1.6的宽高比的屏幕用hhdp文件夹下图片
在1.6和1.4 之间的用dhdp下
小于1.4 的用ddhdp
"""

htv_list = [1.6, 1.4, 0]
hdp_list = ["hhdp", "dhdp", "ddhdp"]


def get_hdp(htv):
    for index, htv_item in enumerate(htv_list):
        if htv > htv_item:
            return hdp_list[index]
