# *- coding:utf8 *-
from flask import Flask
import flask_restful
from SharpGoods.apis.AUsers import SGUsers
from SharpGoods.apis.AProducts import SGProducts
from SharpGoods.apis.ACarts import SGCarts
from SharpGoods.apis.AReviews import SGReviews
from SharpGoods.apis.AOrders import SGOrders
from SharpGoods.apis.ALocations import SGLocations
from SharpGoods.apis.ACoupons import SGCoupons
from SharpGoods.apis.AOther import SGOther
from SharpGoods.apis.ACards import SGCards

sg = Flask(__name__)
api = flask_restful.Api(sg)

api.add_resource(SGUsers, "/sharp/goods/users/<string:users>")
api.add_resource(SGProducts, "/sharp/goods/product/<string:product>")
api.add_resource(SGCarts, "/sharp/goods/cart/<string:cart>")
api.add_resource(SGReviews, "/sharp/goods/review/<string:review>")
api.add_resource(SGOrders, "/sharp/goods/orders/<string:orders>")
api.add_resource(SGLocations, "/sharp/goods/locations/<string:locations>")
api.add_resource(SGCoupons, "/sharp/goods/card/<string:card>")
api.add_resource(SGOther, "/sharp/goods/other/<string:other>")
api.add_resource(SGCards, "/card/<string:card>")
# '''
if __name__ == '__main__':
    sg.run('0.0.0.0', 443, debug=False, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
    
'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 7444, debug=False)

'''