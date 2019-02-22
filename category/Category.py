# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json,logging,Global
from  util import  OpenRequest
domain=Global.domain

def get_category(access_token,version="1.0",path="api"):

    """
    使用场景
        获取商品分类

    方法名称
        vdian.shop.cate.get

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB

    """

    param={}
    pub={"method":"vdian.shop.cate.get","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

def add_category(access_token,cates,version="1.0",path="api"):

    """
    使用场景
        添加商品分类

    方法名称
        vdian.shop.cate.add

    wiki
      http://wiki.open.weidian.com/index.php?title=%E6%96%B0%E5%A2%9E%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB

    """

    param={"cates":cates}
    pub={"method":"vdian.shop.cate.add","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

def up_category(access_token,cates,version="1.0",path="api"):

    """
    使用场景
        更新商品分类

    方法名称
        vdian.shop.cate.update

    wiki
      http://wiki.open.weidian.com/index.php?title=%E7%BC%96%E8%BE%91%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB

    """

    param={"cates":cates}
    pub={"method":"vdian.shop.cate.update","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson

def del_category(access_token,category_id,version="1.0",path="api"):

    """
    使用场景
        删除商品分类

    方法名称
        vdian.shop.cate.delete

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%88%A0%E9%99%A4%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB
    """

    param={"cate_id":category_id}
    pub={"method":"vdian.shop.cate.delete","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson
