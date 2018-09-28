# *- coding:utf8 *-
import os
import sys

from LoveBreakfast.models.model import Machinery
from LoveBreakfast.services.SBase import SBase, close_session

sys.path.append(os.path.dirname(os.getcwd()))


class SMachinery(SBase):
    @close_session
    def get_pro_by_aaid(self, aaid):
        return self.session.query(Machinery.PRid).filter(Machinery.AAid == aaid).all()

    @close_session
    def get_aaid_by_prid(self, prid):
        return self.session.query(Machinery.AAid).filter(Machinery.PRid == prid).all()

    @close_session
    def get_maid_by_aaid_prid(self, aaid, prid):
        return self.session.query(Machinery.MAid).filter(Machinery.PRid == prid, Machinery.AAid == aaid).scalar()


if __name__ == "__main__":
    sma = SMachinery()
    import uuid

    prname = "周一早餐"
    prid = str(uuid.uuid1())
