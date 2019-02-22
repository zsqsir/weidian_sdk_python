# -*- coding:utf-8 -*-
__author__ = 'Seven'

import  json, Global
import  Global
from cps import Cps
domain=Global.domain
token=Global.token
app_key=Global.app_key
item_id="1602006086"

def test_get_cps_items():
    result=Cps.get_cps_items(token,"裙子",min_price=1000,max_price=3000)
    print json.dumps(result)

def test_get_cps_item_detail():
    item_id="1235967158"
    result=Cps.get_cps_item_detail(token,item_id)
    print json.dumps(result)

def test_get_item_pubinfo():
    item_id="1236245992"
    result=Cps.get_item_pubinfo(token,item_id)
    print result['result']['item_name'].encode("utf-8")

if __name__=="__main__":
    test_get_cps_items()
    # pass
    test_get_cps_item_detail();
    test_get_item_pubinfo();