# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from SharpGoods.models.model import Cart
from SharpGoods.service.SBase import SBase, close_session


class SCarts(SBase):

    def __init__(self):
        super(SCarts, self).__init__()

    def get_carts_by_Uid(self, uid):
        all_cart = None
        try:
            all_cart = self.session.query(Cart.CAid, Cart.PBid, Cart.CAnumber, Cart.CAstatus).filter_by(USid=uid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return all_cart

    # @close_session
    # def add_carts(self, **kwargs):
    #     cart = Cart()
    #     for key in cart.__table__.columns.keys():
    #         if key in kwargs:
    #             setattr(cart, key, kwargs.get(key))
    #     self.session.add(cart)

    @close_session
    def del_carts(self, caid):
        self.session.query(Cart).filter(Cart.CAid == caid).delete()

    @close_session
    def update_num_cart(self, pnum, caid):
        self.session.query(Cart).filter(Cart.CAid == caid).update({"CAnumber": pnum, "CAstatus": 1})

    @close_session
    def get_cart_by_uid_pid(self, uid, pid):
        return self.session.query(Cart.CAid, Cart.CAnumber, Cart.CAstatus).filter(Cart.USid == uid, Cart.PBid == pid).first()

    @close_session
    def get_pbnumber_by_pbid_and_usid(self, pbid, usid):
        return self.session.query(Cart.CAnumber).filter_by(PBid=pbid).filter_by(USid=usid).scalar()