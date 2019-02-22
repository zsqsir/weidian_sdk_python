# -*- coding:utf-8 -*-
__author__ = 'Seven'

from  util import  OpenRequest
import json, Global
domain=Global.domain
token=Global.token
app_key=Global.app_key

def get_cps_items(access_token,keyword,page=1,page_size=20,min_price=0,max_price=10000,min_cps_rate=0,max_cps_rate=50,version="1.0",path="api"):

    """
    使用场景

        搜索CPS商品

    方法名称
        vdian.cps.item.search

    wiki
       http://wiki.open.weidian.com/index.php?title=%E6%90%9C%E7%B4%A2CPS%E5%95%86%E5%93%81

    """
    param={"keyword":keyword,"page_size":page_size,"page":page,"min_price":min_price,"max_price":max_price,"min_cps_rate":str(min_cps_rate),"max_cps_rate":str(max_cps_rate)}

    pub={"method":"vdian.cps.item.search","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

def get_cps_item_detail(access_token,itemid,version="1.0",path="api"):

    """
    使用场景
        获取CPS商品详情

    方法名称
        vdian.cps.item.get

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96CPS%E5%95%86%E5%93%81

    """
    param={"itemid":itemid}

    pub={"method":"vdian.cps.item.get","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

def get_item_pubinfo(access_token,itemid,version="1.0",path="api"):

    """
    使用场景
        获取CPS商品详情

    方法名称
        vdian.item.getpublic

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96CPS%E5%95%86%E5%93%81

    """
    param={"itemid":itemid}

    pub={"method":"vdian.item.getpublic","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf-8")
    return contentJson

