import {
  wxRequest
} from '@/utils/wxRequest';

let env = "-test" //-dev 或者 -test
const api= 'http://123.207.97.185:7444';

/**
 * 获取发现好商品接口
 * @param  {[type]} params [description]
 * @return {[type]}        [description]
 */
const register = (params) => wxRequest(params, api + '/love/breakfast/users/register');//注册
const login = (params) => wxRequest(params, api + '/love/breakfast/users/login');//登录
const update_info = (params) => wxRequest(params, api + '/love/breakfast/users/update_info');//修改个人信息
const update_pwd = (params) => wxRequest(params, api + '/love/breakfast/users/update_pwd');//修改密码
const all_info = (params) => wxRequest(params, api + '/love/breakfast/users/all_info');//获取个人信息
const make_main_order = (params) => wxRequest(params, api + '/love/breakfast/orders/make_main_order');//创建订单
const update_order_status = (params) => wxRequest(params, api + '/love/breakfast/orders/update_order_status');//更新订单状态
const get_order_list = (params) => wxRequest(params, api + '/love/breakfast/orders/get_order_list');//获取订单列表
const get_order_abo = (params) => wxRequest(params, api + '/love/breakfast/orders/get_order_abo');//获取订单详情
const get_all_location = (params) => wxRequest(params, api + '/love/breakfast/locations/get_all_location');// 获取全部站点
const get_lno = (params) => wxRequest(params, api + '/love/breakfast/locations/get_lno');//获取出口
const sale_update = (params) => wxRequest(params, api + '/love/breakfast/salelist/update');//往购物车添加商品或者减少商品，可处理多个
const get_all_car = (params) => wxRequest(params, api + '/love/breakfast/salelist/get_all');//获取购物车信息
const delete_product = (params) => wxRequest(params, api + '/love/breakfast/salelist/delete_product');//购物车批量删除商品
const get_all_product = (params) => wxRequest(params, api + '/love/breakfast/product/get_all');//获取所有商品信息
const get_info_by_id = (params) => wxRequest(params, api + '/love/breakfast/product/get_info_by_id');//通过商品id获取商品详情
const create_review = (params) => wxRequest(params, api + '/love/breakfast/review/create_review');// 添加评论
const get_review = (params) => wxRequest(params, api + '/love/breakfast/review/get_review');//通过评论id获取评论详情
const get_cardpkg = (params) => wxRequest(params, api + '/love/breakfast/cardpkg/get_cardpkg');// 查看个人所有优惠券
const update_coupons = (params) => wxRequest(params, api + '/love/breakfast/cardpkg/update_coupons');//更新优惠券
const get_citys = (params) => wxRequest(params, api + '/love/breakfast/address/get_citys');//获取所有可选城市
const get_addfirst = (params) => wxRequest(params, api + '/love/breakfast/address/get_addfirst');//通过所选类型获取城市的已开通区域或线路信息
const get_addsecond = (params) => wxRequest(params, api + '/love/breakfast/address/get_addsecond');//通过区域或线路id 获取园区或站点信息
const get_addabo = (params) => wxRequest(params, api + '/love/breakfast/address/get_addabo');//通过asid获取机器详情地址及图片
const get_city_location = (params) => wxRequest(params, api + '/love/breakfast/locations/get_city_location');//根据经纬度获取城市
const picture = (params) => wxRequest(params, api + '/love/breakfast/other/picture');//获取首页图片
export default {
  register,login,update_info,update_pwd,all_info,make_main_order,
  update_order_status,get_order_list,get_order_abo,get_all_location,
  get_lno,sale_update,get_all_car,delete_product,get_all_product,get_info_by_id,
  get_cardpkg,update_coupons,get_citys,get_addfirst,get_addsecond,get_addabo,
  get_city_location,picture,create_review,get_review

}