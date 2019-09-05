# *- coding:utf8 *-
# 兼容linux系统
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
# 引用项目类
from SharpGoods.models import model
from SharpGoods.common.TransformToList import trans_params
from SharpGoods.service.DBSession import get_session

# 操作user表的相关方法
class SProduct():
    def __init__(self):
        """
        self.session 数据库连接会话
        self.status 判断数据库是否连接无异常
        """
        self.session, self.status = get_session()

    def get_product_by_pbid(self, pbid):
        product = None
        try:
            product = self.session.query(model.ProductsBrands.PRid, model.ProductsBrands.BRid,
                                         model.ProductsBrands.PBunit, model.ProductsBrands.PBprice,
                                         model.ProductsBrands.PBsalesvolume, model.ProductsBrands.PBscore,
                                         model.ProductsBrands.PBimage)\
                .filter_by(PBstatus=201).filter_by(PBid=pbid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return product

    def get_all_brand_by_brid_last(self, brid):
        brand_list = {}
        try:
            while brid != "0":
                brand = self.session.query(model.Brands.BRfromid, model.Brands.BRkey,
                                           model.Brands.BRvalue).filter_by(BRid=brid).first()
                brid, brkey, brvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                brand_list.keys().append(brkey)
                brand_list[brkey] = brvalue
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return brand_list

    def get_brand_by_brid(self, brid):
        brand = None
        try:
            brand = self.session.query(model.Brands.BRfromid, model.Brands.BRkey, model.Brands.BRvalue)\
                .filter_by(BRid=brid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return brand

    def get_product_by_prid(self, prid):
        product = None
        try:
            product = self.session.query(model.Products.PRname, model.Products.PRbrand, model.Products.PRinfo,
                                         model.Products.PRvideo, model.Products.PRtype, model.Products.PRimage,
                                         model.Products.PRaboimage, model.Products.PRvideostart).filter_by(PRid=prid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return product

    @trans_params
    def get_pbimg_by_prid(self, prid):
        pbimg = None
        try:
            pbimg = self.session.query(model.ProductsBrands.PBimage).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbimg

    @trans_params
    def get_brid_by_prid(self, prid):
        pbid = None
        try:
            pbid = self.session.query(model.ProductsBrands.BRid).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbid

    @trans_params
    def get_all_prid(self):
        prid = None
        try:
            prid = self.session.query(model.Products.PRid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return prid

    @trans_params
    def get_brid_by_key_value(self, key, value):
        brid = None
        try:
            brid = self.session.query(model.Brands.BRid).filter_by(BRkey=key).filter_by(BRvalue=value).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return brid

    def get_pball_by_brid(self, brid):
        pball = None
        try:
            pball = self.session.query(model.ProductsBrands.PBimage, model.ProductsBrands.PBunit,
                                       model.ProductsBrands.PBprice, model.ProductsBrands.PBscore,
                                       model.ProductsBrands.PBsalesvolume, model.ProductsBrands.PBid)\
                .filter_by(BRid=brid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pball

    def get_volue_score_by_pbid(self, pbid):
        volue_score = None
        try:
            volue_score = self.session.query(model.ProductsBrands.PBsalesvolume, model.ProductsBrands.PBscore)\
                .filter_by(PBid=pbid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return volue_score

    def update_score_by_pbid(self, pbid, product_brand):
        try:
            self.session.query(model.ProductsBrands).filter_by(PBid=pbid).update(product_brand)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            print e.message
            self.session.rollback()
            self.session.close()
            return False

    @trans_params
    def get_pbid_by_prid(self, prid):
        pbid = None
        try:
            pbid = self.session.query(model.ProductsBrands.PBid).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbid

    @trans_params
    def get_pbprice_by_prid(self, prid):
        pbprice = None
        try:
            pbprice = self.session.query(model.ProductsBrands.PBprice).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbprice

    @trans_params
    def get_pbvolume_by_prid(self, prid):
        pbvolume = None
        try:
            pbvolume = self.session.query(model.ProductsBrands.PBsalesvolume).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbvolume

    def get_prid_by_pbid(self, pbid):
        prid = None
        try:
            prid = self.session.query(model.ProductsBrands.PRid).filter_by(PBid=pbid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return prid