# -*- coding:utf8 -*-
__author__ = 'Seven'

import json, logging, Global
from  util import OpenRequest
from urllib import quote

domain = Global.domain
token = Global.token
app_key = Global.app_key


def get_item(item_id, access_token, version="1.0", path="api"):
    """
    使用场景

        商家ERP系统根据商品的ID获取微店的单个商品信息，此接口要求APPkey和店铺有绑定关系

    方法名称
        vdian.item.get

    wiki
        http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E5%8D%95%E4%B8%AA%E5%95%86%E5%93%81

    """
    param = {"itemid": str(item_id)}
    pub = {"method": "vdian.item.get", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)

    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def list_shop_items(access_token, page_num=1, page_size=10, orderby=1, version="1.0", path="api"):
    """
    使用场景
        商家系统获取微店的商品列表，进行商品管理，此接口只能获取授权店铺的商品


    方法名称
        vdian.item.list.get

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E5%85%A8%E5%BA%97%E5%95%86%E5%93%81

    """
    param = {"page_num": page_num, "page_size": page_size, "orderby": orderby}
    pub = {"method": "vdian.item.list.get", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def add_item2(access_token,price,stock,imgs,titles,item_name, status=2, item_comment='',
             item_detail_list=[], sku=[],fx_fee_rate=1,merchant_code="",version="1.4",path="api"):
    """
    使用场景

        添加商品

        请注意：

        商品图片需另行上传获取URL，详情见图片上传接口
        创建型号的参数为数组
        商品分类的入参为分类ID需通过“商品分类接口”获取


    方法名称
        vdian.item.add

    wiki
       http://wiki.open.weidian.com/index.php?title=%E5%88%9B%E5%BB%BA%E5%BE%AE%E5%BA%97%E5%95%86%E5%93%81

    """

    # param = {"imgs": imgs, "stock": stock, "price": price, "item_name": item_name, "fx_fee_rate": fx_fee_rate,
    #          "skus": skus, "merchant_code": merchant_code, "item_comment": item_comment}
    param={"bigImgs":imgs,"titles":titles, "stock":stock,"price":price,"item_name":item_name,"fx_fee_rate":fx_fee_rate,
           "sku":sku,"merchant_code":merchant_code,"status": status, "item_comment": item_comment,
           "item_detail_list": item_detail_list, "cate_id": '50050291', 'free_delivery': 0}
    param = json.dumps(param)
    pub = {"method": "vdian.item.add", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    print 'url::', url
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson

def add_item(access_token,price,stock,imgs,titles,item_name, status=2, item_comment='',
             item_detail_list=[], sku=[],fx_fee_rate=1,merchant_code="",version="1.4",path="api"):

    """
    使用场景

        添加商品

        请注意：

        商品图片需另行上传获取URL，详情见图片上传接口
        创建型号的参数为数组
        商品分类的入参为分类ID需通过“商品分类接口”获取


    方法名称
        vdian.item.add

    wiki
       http://wiki.open.weidian.com/index.php?title=%E5%88%9B%E5%BB%BA%E5%BE%AE%E5%BA%97%E5%95%86%E5%93%81

    """

    param={"bigImgs":imgs,"titles":titles, "stock":stock,"price":price,"item_name":item_name,"fx_fee_rate":fx_fee_rate,
           "sku":sku,"merchant_code":merchant_code,"status": status, "item_comment": item_comment,
           "item_detail_list": item_detail_list, "cate_id": '50050291', 'free_delivery': 0}
   # param={"bigImgs":imgs, "stock":stock,"price":price,"itemName":item_name,"fx_fee_rate":fx_fee_rate,
    #       "sku":sku,"merchant_code":merchant_code,"status": status, "item_comment": item_comment,
     #      "item_detail_list": item_detail_list, "cate_id": '50050291', 'free_delivery': "0",'remote_free_delivery': "1"}
    # param = json.dumps(param)
    pub={"method":"vdian.item.add","access_token":access_token,"version":version,"lang":"python","sdkversion":Global.version}
    url="%s%s?param=%s&public=%s" %(domain,path,param,pub)
    print('url:', url)
    content=OpenRequest.http_get(url)
    contentJson=json.loads(content,"utf8")
    return contentJson


def del_item(item_id, access_token, version="1.0", path="api"):
    """
    使用场景
        删除单个商品

    方法名称
        vdian.item.delete

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%88%A0%E9%99%A4%E5%8D%95%E4%B8%AA%E5%95%86%E5%93%81

    """
    param = {"itemid": item_id}
    pub = {"method": "vdian.item.delete", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)

    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def add_item_imgs(item_id, access_token, imgs, version="1.0", path="api"):
    """
    使用场景
        添加商品图片

    方法名称
        vdian.item.image.add

    wiki
        http://wiki.open.weidian.com/index.php?title=%E6%B7%BB%E5%8A%A0%E5%95%86%E5%93%81%E5%9B%BE%E7%89%87

    """
    param = {"itemid": item_id, "imgs": imgs}
    pub = {"method": "vdian.item.image.add", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def del_item_imgs(item_id, access_token, delete_imgs, version="1.0", path="api"):
    """
    使用场景
        为指定商品删除某张商品图片
    方法名称
        vdian.item.image.delete

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%88%A0%E9%99%A4%E5%95%86%E5%93%81%E5%9B%BE%E7%89%87

    """
    param = {"itemid": item_id, "delete_imgs": delete_imgs}
    pub = {"method": "vdian.item.image.delete", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)

    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def up_item(access_token, item_id, price, stock, item_name, skus=[], fx_fee_rate=1, cate_ids=[], merchant_code="",
            version="1.0", path="api"):
    """
    使用场景
        更新商品图片信息

        请注意：
        此接口无法编辑商品图片


    方法名称
        vdian.item.update

    wiki
       http://wiki.open.weidian.com/index.php?title=%E6%9B%B4%E6%96%B0%E5%95%86%E5%93%81%E4%BF%A1%E6%81%AF

    """

    param = {"itemid": item_id, "stock": stock, "price": price, "item_name": item_name, "fx_fee_rate": fx_fee_rate,
             "skus": skus, "merchant_code": merchant_code, "cate_ids": cate_ids}
    pub = {"method": "vdian.item.update", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def add_item_sku(access_token, item_id, skus=[], version="1.0", path="api"):
    """
    使用场景
        添加商品sku

    方法名称
        vdian.item.sku.add

    wiki
       http://wiki.open.weidian.com/index.php?title=%E6%B7%BB%E5%8A%A0%E5%95%86%E5%93%81%E5%9E%8B%E5%8F%B7

    """

    param = {"itemid": item_id, "skus": skus}
    pub = {"method": "vdian.item.sku.add", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def up_item_sku(access_token, item_id, skus=[], version="1.0", path="api"):
    """
    使用场景
        商家系统更新微店商品的某个型号信息，包括型号名称、价格、库存、编码



    方法名称
        vdian.item.sku.update

    wiki
       http://wiki.open.weidian.com/index.php?title=%E6%9B%B4%E6%96%B0%E5%95%86%E5%93%81%E5%9E%8B%E5%8F%B7

    """

    param = {"itemid": item_id, "skus": skus}
    pub = {"method": "vdian.item.sku.update", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def del_item_sku(access_token, item_id, sku_ids, version="1.0", path="api"):
    """
    使用场景
        删除商品的sku

    方法名称
        vdian.item.sku.delete

    wiki
       http://wiki.open.weidian.com/index.php?title=%E5%88%A0%E9%99%A4%E5%95%86%E5%93%81%E5%9E%8B%E5%8F%B7

    """

    param = {"itemid": item_id, "skus": sku_ids}
    pub = {"method": "vdian.item.sku.delete", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def get_category(access_token, version="1.0", path="api"):
    """
    使用场景
        获取商品分类

    方法名称
        vdian.shop.cate.get

    wiki
       http://wiki.open.weidian.com/index.php?title=%E8%8E%B7%E5%8F%96%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB

    """

    param = {}
    pub = {"method": "vdian.shop.cate.get", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def up_item_category(access_token, item_ids, category_ids, version="1.0", path="api"):
    """
    使用场景
        设置商品分类

    方法名称
        vdian.item.cate.set

    wiki
        http://wiki.open.weidian.com/index.php?title=%E8%AE%BE%E7%BD%AE%E5%95%86%E5%93%81%E7%9A%84%E5%88%86%E7%B1%BB
    """

    param = {"item_ids": item_ids, "cate_ids": category_ids}
    pub = {"method": "vdian.item.cate.set", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def cancel_item_category(access_token, item_id, category_ids, version="1.0", path="api"):
    """
    使用场景
        设置商品分类

    方法名称
        vdian.item.cate.cancel

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%8F%96%E6%B6%88%E5%95%86%E5%93%81%E7%9A%84%E5%88%86%E7%B1%BB
    """

    param = {"itemid": item_id, "cate_ids": category_ids}
    pub = {"method": "vdian.item.cate.cancel", "access_token": access_token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def item_on_sale(access_token, item_id, version="1.0", path="api"):
    """
    使用场景
        商品上架

    方法名称
        weidian.item.onSale

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%8F%96%E6%B6%88%E5%95%86%E5%93%81%E7%9A%84%E5%88%86%E7%B1%BB
    """

    param = {"itemid": item_id, "opt": "1"}
    pub = {"method": "weidian.item.onSale", "access_token": token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson


def item_off_sale(access_token, item_id, version="1.0", path="api"):
    """
    使用场景
        商品上架

    方法名称
        weidian.item.onSale

    wiki
        http://wiki.open.weidian.com/index.php?title=%E5%8F%96%E6%B6%88%E5%95%86%E5%93%81%E7%9A%84%E5%88%86%E7%B1%BB
    """

    param = {"itemid": item_id, "opt": "2"}
    pub = {"method": "weidian.item.onSale", "access_token": token, "version": version, "lang": "python",
           "sdkversion": Global.version}
    url = "%s%s?param=%s&public=%s" % (domain, path, param, pub)
    content = OpenRequest.http_get(url)
    contentJson = json.loads(content, "utf8")
    return contentJson
