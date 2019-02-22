# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json, Global
from  util import  OpenRequest
from order import Order
domain=Global.domain
token=Global.token
app_key=Global.app_key
item_id="1602006086"


def test_get_orders():
    result=Order.get_orders(token,add_start='2015-10-09 12:00:00')
    print json.dumps(result)

def test_get_order_detail():
    order_id="774304979506247"
    result=Order.get_order_detail(token,order_id)
    print json.dumps(result)

def test_order_deliver():
    order_id="774213752686027"
    express_type=999
    express_no=0;
    result=Order.order_deliver(token,order_id,express_type,express_no)
    print json.dumps(result)

def test_up_order_deliver():
    order_id="774071859769744"
    express_type=999
    express_no=0;
    result=Order.up_order_deliver(token,order_id,express_type,express_no,express_custom="test物流")
    print json.dumps(result)

def test_up_order_price():
    order_id="774072250266000"
    total_items_price=1.02
    express_price=0.02
    result=Order.up_order_price(token,order_id,total_items_price,express_price)
    print json.dumps(result)

def test_order_refund_accept():
    order_id="774071859769744"
    result=Order.order_refund_accept(token,order_id,1)
    print json.dumps(result)


if __name__=="__main__":

    test_get_orders()
    test_get_order_detail()
    # test_order_deliver()
    # test_up_order_deliver()
    # test_order_refund_accept()
    # test_order_refund_accept()
    # pass