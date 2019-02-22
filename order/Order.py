# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json, Global
from  util import  OpenRequest
from urllib import  quote
domain=Global.domain
token=Global.token
app_key=Global.app_key

def get_orders(access_token,order_type="",page_num=1,page_size=30,add_start="",add_end="",update_start="",update_end="",version="1.1",path="api"):

    """
    使用场景
        获取订单列表

    方法名称
        vdian.order.list.get

    参数说明：
        order_type： 当version为1.1时： 此参数为可选，不传返回全部状态的订单
            unpay（未付款订单）
            pend（待处理订单，已就是待发货订单）
            refund（退款中订单，version参数必须传1.1）
            close（关闭的订单）
            finish（完成的订单）
            refund（退款中订单）

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8

    """
    # if(q)
    param={"page_num":page_num,"page_size":page_size,"order_type":order_type}
    if  add_start and len(add_start)>0:
        param['add_start']=quote(add_start)
    if  add_end and len(add_end)>0:
        param['add_end']=quote(add_end)
    if  update_start and len(update_start)>0:
        param['update_start']=quote(update_start)
    if  update_end and len(update_end)>0:
        param['update_end']=quote(update_end)

    pub={"method":"vdian.order.list.get","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson


def get_order_detail(access_token,order_id,version="1.0",path="api"):

    """
    使用场景
        获取订单详情


    方法名称
        vdian.order.get

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E8%AE%A2%E5%8D%95%E8%AF%A6%E6%83%85

    """
    # if(q)
    param={"order_id":str(order_id)}

    pub={"method":"vdian.order.get","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson


def order_deliver(access_token,order_id,express_type,express_no,express_custom,version="1.0",path="api"):

    """
    使用场景
        订单发货

    方法名称
        vdian.order.deliver

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%AE%A2%E5%8D%95%E5%8F%91%E8%B4%A7

    """
    # if(q)
    param={"order_id":str(order_id),"express_type":str(express_type),"express_no":str(express_no),"express_custom":express_custom}
    pub={"method":"vdian.order.deliver","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson



def up_order_deliver(access_token,order_id,express_type,express_no,express_custom,express_note="",version="1.0",path="api"):

    """
    使用场景
        修改物流信息

    方法名称
        vdian.order.express.modify

    wiki
        http://wiki.open.weidian.com/index.php?title=%E4%BF%AE%E6%94%B9%E7%89%A9%E6%B5%81%E4%BF%A1%E6%81%AF

    """
    # if(q)
    param={"order_id":str(order_id),"express_type":str(express_type),"express_no":str(express_no),"express_custom":express_custom,"express_note":express_note}
    pub={"method":"vdian.order.express.modify","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson



def up_order_price(access_token,order_id,total_items_price,express_price,version="1.0",path="api"):

    """
    使用场景
        修改订单价格

    方法名称
        vdian.order.modify

    wiki
        http://wiki.open.weidian.com/index.php?title=%E4%BF%AE%E6%94%B9%E8%AE%A2%E5%8D%95%E4%BB%B7%E6%A0%BC

    """
    # if(q)
    param={"order_id":str(order_id),"express_price":str(express_price),"total_items_price":str(total_items_price)}
    pub={"method":"vdian.order.modify","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson



def order_refund_accept(access_token,order_id,is_accept,version="1.0",path="api"):

    """
    使用场景
        同意退款

    方法名称
        vdian.order.refund.accept
        is_accept参数说明：
            只有传1时才会进行退款
            传0拒绝退款
            只有在订单状态为“accept_refunding”时，商家才能传0拒绝退款

    wiki
        http://wiki.open.weidian.com/index.php?title=%E8%AE%A2%E5%8D%95%E9%80%80%E6%AC%BE

    """
    # if(q)
    param={"order_id":str(order_id),"is_accept":str(is_accept)}
    pub={"method":"vdian.order.refund.accept","access_token":access_token,"version":version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

