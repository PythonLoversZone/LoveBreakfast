# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import uuid
from SharpGoods.service import DBSession
from SharpGoods.models import model
import datetime

class SReview():
    def __init__(self):
        try:
            self.session = DBSession.db_session()
        except Exception as e:
            print(e.message)

    def new_review(self, pbid, usid, recontent):
        try:
            review = model.Review()
            review.REid = str(uuid.uuid4())
            review.USid = usid
            review.PRid = pbid
            review.REtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            review.REcontent = recontent
            review.REtype = 701
            review.USRid = None
            self.session.add(review)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            print e.message
            self.session.rollback()
            self.session.close()
            return False

    def get_review_by_pbid(self, pbid):
        all_review = None
        try:
            all_review = self.session.query(model.Review.USid, model.Review.REcontent, model.Review.REtime, model.Review.REid)\
                .filter_by(REtype=701).filter_by(PRid=pbid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return all_review