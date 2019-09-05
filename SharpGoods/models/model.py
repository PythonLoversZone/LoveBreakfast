# *- coding:utf-8 *-

import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text, Float
from SharpGoods.config import dbconfig as cfg


DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    USid = Column(String(64), primary_key=True)
    UStelphone = Column(String(14), nullable=False)  # 用户联系方式
    USpassword = Column(String(32), nullable=False)  # 用户密码
    USname = Column(String(64))                      # 用户昵称
    USsex = Column(Integer)                          # 用户性别 {101男， 102女}
    UScoin = Column(Float)                           # 用户积分，根据用户购买商品生成
    USinvate = Column(String(64))                    # 用户邀请码，算法生成待设计


class Locations(Base):
    __tablename__ = "Locations"
    LOid = Column(String(64), primary_key=True)
    LOtelphone = Column(String(14), nullable=False)  # 收件人联系方式
    LOname = Column(String(128), nullable=False)     # 收件人姓名
    LOno = Column(String(8), nullable=False)         # 邮编
    LOdetail = Column(Text, nullable=False)          # 收件人详细地址
    LOprovince = Column(String(64), nullable=False)  # 收件人省份
    LOcity = Column(String(64), nullable=False)      # 收件人城市
    LOarea = Column(String(64), nullable=False)      # 收件人城区
    LOisedit = Column(Integer, nullable=False)       # 是否可编辑 {301:可编辑,302:不可编辑,303:已删除}
    USid = Column(String(64), nullable=False)        # 用户id


class Products(Base):
    __tablename__ = "Products"
    PRid = Column(String(64), primary_key=True)  # 商品id
    PRname = Column(String(64), nullable=False)  # 商品名称
    PRvideo = Column(Text, nullable=False)       # 宣传视频
    PRimage = Column(Text, nullable=False)       # 商品图片存放地址
    PRaboimage = Column(Text)                    # 商品详情图存放地址
    PRinfo = Column(Text)                        # 商品介绍
    PRtype = Column(Integer, nullable=False)     # 营销类型 {501自营， 502非自营}
    PRbrand = Column(Integer, nullable=False)    # 类目 {601美妆类， 602 3C类}
    PRvideostart = Column(Text)                  # 商品视频未启动图片
    MAid = Column(String(64))                    # 商家id
    # PRprice = Column(Float, nullable=False)  # 商品价格
    # PRunit = Column(Integer, nullable=False) # 货币单位 {401美元， 402人民币， 403欧元， 404英镑}
    # PRstatus = Column(Integer, default=1)  # 商品状态 {201:在售状态 202:下架状态}
    # PRsalesvolume = Column(Integer, nullable=False)  # 商品销量
    # PRscore = Column(Float, nullable=True)  # 商品评分
    # PRno = Column(String(8), nullable=False)  # 版本号
    # PRcolor = Column(Text) # 颜色，一对多
    # PRquality = Column(String(64)) # 商品属性，包含类目、颜色等等，以json进行保存


class ProductsBrands(Base):
    __tablename__ = "ProductsBrands"
    PBid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)        # 商品id
    BRid = Column(String(64), nullable=False)        # 叶子类目id
    PBprice = Column(Float, nullable=Float)          # 商品价格
    PBunit = Column(Integer, nullable=False)         # 货币单位 {401美元， 402人民币， 403欧元， 404英镑}
    PBstatus = Column(Integer, default=201)          # 商品状态 {201:在售状态 202:下架状态}
    PBsalesvolume = Column(Integer, nullable=False)  # 商品销量
    PBscore = Column(Float, nullable=True)           # 商品评分
    PBimage = Column(Text, nullable=False)           # 商品图片存放地址


class Brands(Base):
    __tablename__ = "Brands"
    BRid = Column(String(64), primary_key=True)
    BRfromid = Column(String(64), nullable=False)  # 父节点id，如果没有父节点则为0
    BRvalue = Column(String(128), nullable=False)  # 属性值
    BRkey = Column(String(128), nullable=False)    # 属性类型


class Review(Base):
    __tablename__ = "Review"
    REid = Column(String(64), primary_key=True)  # 评论id
    PRid = Column(String(64), nullable=False)    # 对应的评论对象，根据REtype判断
    USid = Column(String(64), nullable=False)    # 用户id
    REtime = Column(String(14), nullable=False)  # 评论时间
    USRid = Column(String(64))                   # 被评论人
    REcontent = Column(Text, nullable=True)      # 评价内容
    REtype = Column(Integer, default=1)          # 对应的评论对象类型 {701:商品评价 702:帖子评价}


class Shops(Base):
    __tablename__ = "Shops"
    SHid = Column(String(64), primary_key=True)
    SHname = Column(String(64), nullable=False)  # 供应商名称
    SHtype = Column(Integer, nullable=True)      # 供应商类型
    SHdetail = Column(Text, nullable=True)       # 供应商详细信息
    SHtelphone = Column(String(14))              # 供应商联系方式
    SHemain = Column(Text)
    SHidnumber = Column(String(18), nullable=False)
    SHidImgFront = Column(Text)
    SHidImgReverse = Column(Text)
    SHbusinessLicense = Column(Text, nullable=False)
    SHcredit = Column(String(18), nullable=False)


class OrderMain(Base):
    __tablename__ = "OrderMain"
    OMid = Column(String(64), primary_key=True)         # 主订单id
    OMtime = Column(String(14), nullable=False)         # 下单时间
    OMstatus = Column(Integer, nullable=False)          # 订单状态 具体状态如下：
    # {0 : 已取消, 7 : 未支付, 14 : 已支付, 21 : 已接单, 28 : 配送中, 35 : 已装箱, 42 : 已完成,  49 : 已评价}
    OMprice = Column(Float)                             # 订单总额
    USid = Column(String(64))                           # 用户id
    LOid = Column(String(64))                           # 配送地址id
    OMlogisticsName = Column(Text, default="顺丰速运")    # 物流公司
    OMabo = Column(Text)                                # 订单备注
    OMcointype = Column(Integer, nullable=False)        # 货币单位 {401美元， 402人民币， 403欧元， 404英镑}
    COid = Column(String(64))                           # 优惠券id


class Orderpart(Base):
    __tablename__ = "OrderPart"
    OPid = Column(String(64), primary_key=True)  # 分订单id
    OMid = Column(String(64), nullable=False)    # 主订单id
    PBid = Column(String(64), nullable=False)    # 商品id
    PRnumber = Column(Integer, nullable=False)   # 商品数量


class Cart(Base):
    __tablename__ = "Cart"
    CAid = Column(String(64), primary_key=True)  # 购物车id
    USid = Column(String(64), nullable=False)    # 用户id
    PBid = Column(String(64), nullable=False)    # 产品id
    CAnumber = Column(Integer)                   # 商品在购物车中的数量
    CAstatus = Column(Integer, default=1)        # 商品在购物车状态，1 在购物车， 2 已从购物车移除 目前直接从数据库中移除


class Coupons(Base):
    __tablename__ = "Coupon"
    COid = Column(String(64), primary_key=True)
    COfilter = Column(Float)      # 优惠券优惠条件，到达金额
    COdiscount = Column(Float)    # 折扣，值为0-1，其中0为免单
    COamount = Column(Float)      # 优惠金额，减免金额，限制最大数目
    CObrand = Column(String(64))  # 商品类别，限制部分商品使用
    COstart = Column(String(14))  # 优惠券的开始时间
    COend = Column(String(14))    # 优惠券的结束时间
    COutype = Column(Integer)     # 优惠券限制的使用人群，用于后期扩展会员
    COtype = Column(Integer)      # 优惠券类型 {801 满减， 802 满折， 803 商品类目限制， 804 无限制， 805 用户类型限制}


class Cardpackage(Base):
    __tablename__ = "Cardpackage"
    CAid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    CAstatus = Column(Integer, default=1)  # 卡包中优惠券的状态 {1:可使用，2: 不可使用}
    COid = Column(String(64), nullable=False)


class IdentifyingCode(Base):
    __tablename__ = "IdentifyingCode"
    ICid = Column(String(64), primary_key=True)
    ICtelphone = Column(String(14), nullable=False)  # 获取验证码的手机号
    ICcode = Column(String(8), nullable=False)       # 获取到的验证码
    ICtime = Column(String(14), nullable=False)      # 获取的时间，格式为20180503100322


class BlackUsers(Base):
    __tablename__ = "BlackUsers"
    BUid = Column(String(64), primary_key=True)
    BUtelphone = Column(String(14), nullable=False)   # 黑名单电话
    BUreason = Column(Text)   # 加入黑名单的原因

'''
以下内容用于名片
'''
class Cards(Base):
    __tablename__ = 'Cards'
    Cid = Column(String(64), primary_key=True)
    Cname = Column(String(64))
    Ctelphone = Column(String(14))
    Ccompany = Column(Text)
    Cposition = Column(Text)
    Clocation = Column(Text)
    openid = Column(String(64))

class Stocks(Base):
    __tablename__ = "Stocks"
    STid = Column(String(64), primary_key=True)
    STamount = Column(Integer, default=0)
    PBid = Column(String(64))


if __name__ == "__main__":
    '''
    运行该文件就可以在对应的数据库里生成本文件声明的所有table
    '''
    Base.metadata.create_all(mysql_engine)