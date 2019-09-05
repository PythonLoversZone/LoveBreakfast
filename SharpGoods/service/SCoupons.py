# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from SharpGoods.models.model import Cardpackage
from SharpGoods.service.SBase import SBase, close_session
from SharpGoods.models.model import Coupons


class SCoupons(SBase):
    def __init__(self):
        super(SCoupons, self).__init__()

    @close_session
    def get_cardpackage_by_uid(self, uid):

        return self.session.query(
            Cardpackage.COid, Cardpackage.CAid,
            Cardpackage.USid, Cardpackage.CAstatus
        ).filter(Cardpackage.USid == uid).all()

    @close_session
    def add_coupons(self, **kwargs):
        coupons = Coupons()
        for key in coupons.__table__.columns.keys():
            if key in kwargs:
                setattr(coupons, key, kwargs.get(key))
        self.session.add(coupons)

    @close_session
    def add_cardpackage(self, **kwargs):
        cardpackage = Cardpackage()
        for key in cardpackage.__table__.columns.keys():
            if key in kwargs:
                setattr(cardpackage, key, kwargs.get(key))
        self.session.add(cardpackage)

    @close_session
    def update_carbackage(self, cardid):
        self.session.query(Cardpackage).filter(Cardpackage.CAid == cardid).update({"CAstatus": 2})

    @close_session
    def get_card_by_uid_couid(self, uid, couid):
        return self.session.query(
            Cardpackage.COid, Cardpackage.CAid, Cardpackage.CAstatus,
            Cardpackage.CAend, Cardpackage.CAstart, Cardpackage.USid
        ).filter(Cardpackage.USid == uid, Cardpackage.COid == couid).first()


    def get_coupons_by_couid(self, couid):
        coupons = None
        try:
            coupons = self.session.query(
                Coupons.COid, Coupons.COamount, Coupons.COdiscount,
                Coupons.COstart, Coupons.COend, Coupons.COfilter, Coupons.CObrand, Coupons.COutype, Coupons.COtype
            ).filter(Coupons.COid == couid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return coupons

    def get_coid_by_caid(self, caid):
        coid = None
        try:
            coid = self.session.query(Cardpackage.COid).filter_by(CAid=caid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return coid