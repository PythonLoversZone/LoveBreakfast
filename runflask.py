# *- coding:utf8 *-
from flask import Flask
import flask_restful
from LoveBreakfast.apis.AUsers import AUsers as lbuser
from LoveBreakfast.apis.AProduct import AProduct as lbproduct
from LoveBreakfast.apis.ACarts import ACarts as lbcarts
from LoveBreakfast.apis.ACategory import ACategory as lbcategory
#from LoveBreakfast.apis.AShop import AShop as lbshop
from LoveBreakfast.apis.AReview import AReview as lbreview
from LoveBreakfast.apis.AOrders import AOrders as lborder
from LoveBreakfast.apis.ALocations import ALocations as lblocations
from LoveBreakfast.apis.ACoupons import ACoupons as lbcoupons
from LoveBreakfast.apis.AAddress import AAddress as lbaddress
from LoveBreakfast.apis.AOther import AOther as lbother
from LoveBreakfast.apis.AVotes import AVotes as lbvote
from SharpGoods.apis.AUsers import AUsers as sguser
from SharpGoods.apis.AProducts import AProducts as sgproduct
from SharpGoods.apis.ACarts import ACarts as sgcarts
from SharpGoods.apis.AReviews import AReviews as sgreview
from SharpGoods.apis.AOrders import AOrders as sgorder
from SharpGoods.apis.ALocations import ALocations as sglocations
from SharpGoods.apis.ACoupons import ACoupons as sgcoupons
from SharpGoods.apis.AOther import AOther as sgother
from SharpGoods.apis.ACards import ACards as sgcards

bk = Flask(__name__)
api = flask_restful.Api(bk)

api.add_resource(lbuser, "/love/breakfast/users/<string:users>")
api.add_resource(lbproduct, "/love/breakfast/product/<string:product>")
api.add_resource(lbcarts, "/love/breakfast/salelist/<string:cart>")
api.add_resource(lbreview, "/love/breakfast/review/<string:review>")
api.add_resource(lbcategory, "/love/breakfast/category/<string:category>")
#api.add_resource(AShop, "/love/breakfast/shop/<string:shop>")
api.add_resource(lborder, "/love/breakfast/orders/<string:orders>")
api.add_resource(lblocations, "/love/breakfast/locations/<string:locations>")
api.add_resource(lbcoupons, "/love/breakfast/cardpkg/<string:card>")
api.add_resource(lbaddress, "/love/breakfast/address/<string:address>")
api.add_resource(lbother, "/love/breakfast/other/<string:other>")
api.add_resource(lbvote, "/love/breakfast/votes/<string:votes>")

api.add_resource(sguser, "/sharp/goods/users/<string:users>")
api.add_resource(sgproduct, "/sharp/goods/product/<string:product>")
api.add_resource(sgcarts, "/sharp/goods/cart/<string:cart>")
api.add_resource(sgreview, "/sharp/goods/review/<string:review>")
api.add_resource(sgorder, "/sharp/goods/orders/<string:orders>")
api.add_resource(sglocations, "/sharp/goods/locations/<string:locations>")
api.add_resource(sgcoupons, "/sharp/goods/card/<string:card>")
api.add_resource(sgother, "/sharp/goods/other/<string:other>")
api.add_resource(sgcards, "/card/<string:card>")

if __name__ == '__main__':
    bk.run('0.0.0.0', 443, debug=True, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
'''
if __name__ == '__main__':
    bk.run('0.0.0.0', 7444, debug=True)
'''