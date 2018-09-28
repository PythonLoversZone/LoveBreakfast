# *- coding:utf8 *-
# 兼容linux系统
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from LoveBreakfast.models import model
from LoveBreakfast.services import DBSession


class SCategory():
    def __init__(self):
        """
        self.session 数据库连接会话
        self.status 判断数据库是否连接无异常
        """
        self.session, self.status = DBSession.get_session()
        pass

    # 获取所有的分类名称与id
    def get_all_category(self):
        try:
            category_list = self.session.query(model.Category.Cid, model.Category.Cname).all()
        except Exception as e:
            print(e.message)
        finally:
            self.session.close()
        return category_list

    # 获取店铺id获取全部的分类id与名称
    def get_all_cid_cname(self, sid):
        cid_list = None
        try:
            cid_list = self.session.query(model.Products.Pcategoryid, model.Products.Pcatgoryname).filter_by(Sid=sid).all()
        except Exception as e:
            print(e.message)
        finally:
            self.session.close()
        return cid_list
