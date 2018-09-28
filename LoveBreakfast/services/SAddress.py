# *- coding:utf8 *-
import os
import sys

from LoveBreakfast.models.model import AddCity, AddressAbo, AddressFirst, AddressSecond
from LoveBreakfast.services.SBase import SBase, close_session

sys.path.append(os.path.dirname(os.getcwd()))


class SAddress(SBase):

    @close_session
    def get_addfirst_by_acid_astype(self, acid, aftype):
        return self.session.query(AddressFirst.ACid, AddressFirst.AFid, AddressFirst.AFname, AddressFirst.AFtype) \
            .filter(AddressFirst.ACid == acid, AddressFirst.AFtype == aftype).all()

    @close_session
    def get_city_by_name(self, city):
        return self.session.query(AddCity.ACid, AddCity.ACname).filter(AddCity.ACname == city).first()

    @close_session
    def get_addsecond_by_afid(self, afid):
        return self.session.query(AddressSecond.ASid, AddressSecond.ASname).filter(AddressSecond.AFid == afid).all()

    @close_session
    def get_addabo_by_asid(self, asid):
        return self.session.query(AddressAbo.AAid, AddressAbo.AAimage, AddressAbo.AAmessage) \
            .filter(AddressAbo.ASid == asid).all()

    @close_session
    def get_citys(self):
        return self.session.query(AddCity.ACname, AddCity.ACid).all()

    @close_session
    def get_addabo_by_addid(self, aaid):
        return self.session.query(AddressAbo.AAid, AddressAbo.AAmessage).filter(AddressAbo.AAid == aaid).first()
