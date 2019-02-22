# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json,Global
from urllib import  quote
from item import  Item
domain=Global.domain
token=Global.token
app_key=Global.app_key
item_id="1602006086"



def test_get_item():
    result= Item.get_item(item_id=item_id,access_token=token)
    print result['result']['item_name']
    print json.dumps(result);






def test_list_shop_items():
    print Item.list_shop_items(token)




def test_add_item2():
    imgs=[quote('http://wd.geilicdn.com/vshop395640-1390204649-1.jpg')]
    stock=10
    price='23.98'
    item_name='test add item '
    item_name=quote(item_name)
    item_comment = item_name
    sku=[{"title":"型号1","price":"12","stock":"12","sku_merchant_code":"xh1"},{"title":"型号2","price":"12","stock":"12","sku_merchant_code":"xh2"}]
    result=Item.add_item(token,price,stock,imgs,item_name,item_comment,sku)

    print result

def test_add_item():
    imgs=[quote('http://wd.geilicdn.com/vshop395640-1390204649-1.jpg'),quote('https://si.geilicdn.com/open1403792579-3626000001690d29df830a217216_546_727.jpg')]
#    imgs=[quote(r'H:/wdpic/1.jpg')]
    titles= ['123456','789']
    stock=10
    price='4123.98'
    item_name='我爱简笔画（全4册）'
    item_detail_list = [{"type": 1, "text": 'abc'*9},
                        {"type": 2, "pos": 1, "url": quote('https://si.geilicdn.com/open1403792579-3626000001690d29df830a217216_546_727.jpg')}]
    merchant_code = 1234
    # sku=[{"title":"type1","price":"12","stock":"12","sku_merchant_code":"xh1"},{"title":"type2","price":"12","stock":"12","sku_merchant_code":"xh2"}]
    # result=Item.add_item(token,price,stock,imgs,quote(item_name),sku)
    result=Item.add_item(token,price,stock,imgs,titles,quote(item_name), status=2, item_comment=item_name*22,
                         item_detail_list= item_detail_list, merchant_code=merchant_code )

    print result




def test_del_item(item_id):
    result= Item.del_item(item_id=item_id,access_token=token)
    print result;



def test_add_item_imgs():
    imgs=[quote('http://wd.geilicdn.com/vshop1005600-1415182281695-2399763.jpg?w=310&h=125')]
    result= Item.add_item_imgs(item_id=item_id,access_token=token,imgs=imgs)
    print result;



def test_del_item_imgs():
    del_imgs=[quote("http://wd.geilicdn.com/vshop1005600-1415182281695-2399763.jpg?w=310&h=125"),quote("http://wd.geilicdn.com/vshop167963282-1439696805666-06830-s1.jpg?w=1080&h=0")]
    result= Item.del_item(item_id=item_id,access_token=token)
    print result;



def test_up_item():
    imgs=[quote('http://wd.geilicdn.com/vshop395640-1390204649-1.jpg')]
    stock=10
    price='23.98'
    item_name='test add item-1 '
    sku=[{"title":"型号1","price":"1234","stock":"2332","sku_merchant_code":"xhasdf","id":"4196132217"},{"title":"型号2","price":"12","stock":"12","sku_merchant_code":"xh2","id":"4196132218"}]
    result=Item.up_item(token,item_id,price,stock,quote(item_name),sku)

    print result



def test_add_item_sku():

    sku=[{"title":"style1","price":"12345","stock":"12","sku_merchant_code":"xhasdfadd"},{"title":"style2","price":"12","stock":"12","sku_merchant_code":"xh2d"}]
    result=Item.add_item_sku(token,item_id,sku)

    print json.dumps(result)



def test_up_item_sku():
    sku=[{"title":"style1_up","price":"232","stock":"24","sku_merchant_code":"xhasdfadd","id":"4196676240"},{"title":"style2_up","price":"233","stock":"23","sku_merchant_code":"xh2d_up","id":"4196676241"}]
    result=Item.up_item_sku(token,item_id,sku)
    print json.dumps(result)



def test_del_item_sku():
    sku=["4196676240","4196676241"]
    result=Item.del_item_sku(token,item_id,sku)
    print json.dumps(result)


def test_get_category():
    sku=["4196676240","4196676241"]
    result=Item.get_category(token)
    print json.dumps(result)



def test_up_item_category():
    category_ids=["58717889","4950564"]
    item_ids=[item_id,"1602327116"]
    result=Item.up_item_category(token,item_ids,category_ids)
    print json.dumps(result)





def test_cancel_item_category():
    category_ids=["58717889","4950564"]
    item_ids=[item_id]
    result=Item.cancel_item_category(token,item_id,category_ids)
    print json.dumps(result)




def test_item_on_sale():

    result=Item.item_on_sale(token,item_id)
    print json.dumps(result)

def test_item_off_sale():

    result=Item.item_off_sale(token,item_id)
    print json.dumps(result)





if __name__=="__main__":
    # test_get_item();
    # test_list_shop_items()
    test_add_item()
    # test_del_item(item_id=1600580324)
    # test_add_item_imgs()
    # test_del_item_imgs()
    # test_up_item()
    # test_add_item_sku()
    # test_up_item_sku()
    # test_del_item_sku()
    # test_get_category()
    # test_up_item_category()
    # test_cancel_item_category()
    # test_item_off_sale()
    # test_item_on_sale()
    # pass