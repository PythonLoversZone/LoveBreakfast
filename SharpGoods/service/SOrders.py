# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from SharpGoods.service.SBase import SBase, close_session
from SharpGoods.models.model import OrderMain, Orderpart


class SOrders(SBase):
    def __init__(self):
        super(SOrders, self).__init__()

    def get_uid_by_omid(self, omid):
        uid = None
        try:
            uid = self.session.query(OrderMain.USid).filter_by(OMid=omid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return uid

    def get_omstatus_by_omid(self, omid):
        uid = None
        try:
            uid = self.session.query(OrderMain.OMstatus).filter_by(OMid=omid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return uid

    def update_omstatus_by_omid(self, omid, order_main):
        try:
            self.session.query(OrderMain).filter_by(OMid=omid).update(order_main)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print e.message
            return False

    @close_session
    def get_order_part_list_by_omid(self, omid):
        return self.session.query(
            Orderpart.OPid, Orderpart.PBid, Orderpart.PRnumber).filter(Orderpart.OMid == omid).all()

    @close_session
    def get_order_main_list_by_usid(self, usid):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice, OrderMain.OMlogisticsName
        ).filter(OrderMain.USid == usid).order_by(OrderMain.OMtime.desc()).all()

    @close_session
    def get_order_main_by_om_id(self, omid):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice, OrderMain.OMlogisticsName
        ).filter(OrderMain.OMid == omid).first()

    @close_session
    def get_omprice_by_omid(self, omid):
        return self.session.query(OrderMain.OMprice).filter_by(OMid=omid).scalar()

    @close_session
    def get_order_main_list(self, start, end):
        return self.session.query(OrderMain.OMid, OrderMain.LOid, OrderMain.OMabo, OrderMain.OMtime)\
            .filter(start <= OrderMain.OMtime, OrderMain.OMtime <= end).order_by(OrderMain.OMtime).all()
