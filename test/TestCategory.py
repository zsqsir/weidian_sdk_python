# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json,logging,Global
from category import Category
from urllib import  quote
domain=Global.domain
token=Global.token;
app_key=Global.app_key

item_id="1602006086"

def test_get_category():
    sku=["4196676240","4196676241"]
    result=Category.get_category(token)
    print json.dumps(result)

def test_add_category():
    cates=[{"cate_name":quote("22 水果 12s3"),"sort_num":1}]
    result=Category.add_category(token,cates)
    print json.dumps(result)

def test_up_category():
    # cates=[{"cate_name":quote("22 水果 123"),"sort_num":1}]
    cates=[{"cate_name": quote("天然的美味"), "cate_id": "4950564", "sort_num": 0}]
    result=Category.up_category(token,cates)
    print json.dumps(result)

def test_del_category():
    category_id=58715683
    result=Category.del_category(token,category_id)
    print json.dumps(result)

if __name__=="__main__":

    # test_get_category()
    # test_add_category()
    # test_up_category()
    # test_del_category()
    pass