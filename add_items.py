# coding=utf8
#
from oldconn import conn,curs
import  json,Global
from urllib import quote
from item import  Item
domain=Global.domain
token=Global.token
app_key=Global.app_key

def getImage(gid):
    sql ="select url from xy_weidian_image where gid=%s" % gid
    curs.execute(sql)
    res= curs.fetchone()
    print(res)
    return res['url']


def add_item(book, gid, name, price, stock, description ):
    imgurl= getImage(gid)
    imgs=[quote(imgurl)]

#    imgs=[quote(r'H:/wdpic/1.jpg')]
    titles= ['123456','789']
    # stock=10
    item_name = name[0:70]
    print 'len(item_name):', len(item_name), item_name
    item_name=quote(item_name)
    print 'len(item_name):', len(item_name), item_name
    price = float(price)
    item_comment = quote(name)
    item_detail_list = [{"type": 1, "text": quote(description)},
                        {"type": 2, "pos": 1, "url": quote(imgurl)}]
    if book['brief']:
        item_detail_list.append({"type": 1, "text": quote(book['brief'])})
    merchant_code = str(gid)
    # sku=[{"title":"type1","price":"12","stock":"12","sku_merchant_code":"xh1"},{"title":"type2","price":"12","stock":"12","sku_merchant_code":"xh2"}]
    # result=Item.add_item(token,price,stock,imgs,quote(item_name),sku)
    result=Item.add_item(token,price,stock,imgs,titles,item_name, status=2, item_comment=item_comment,
                         item_detail_list= item_detail_list, merchant_code=merchant_code )

    print result

def reverseDes(des):
    if des:
        des = des.split('->')
        des.reverse()
        des = ''.join(des)
    return des

def formatdes(book):
    print(book)
    desitems = [('des', '书    名'), ('odes', '原 书 名'), ('ref', '书    号'), ('area', '出 版 社'), ('oarea', '原出版社'),
                ('series', '丛 书 名'), ('writer', '作    者'), ('translator', '译    者'),
                ('date', '出版日期'), ('turn', '版    次'), ('size', '开    本'), ('page', '页    码'), ('price', '定    价'),
                ('brief', '内容简介'), ('catalog', '目录'), ('bjtj', '编辑推荐'), ('wz', '文摘'),
                ('preface', '前言'), ('hj', '后记')]
    des = ''
    for item in desitems:
        k, v = item
        if book[k]:
            if k in ('brief', 'catalog', 'bjtj', 'wz', 'hj', 'preface'):
                book[k] = book[k].replace('\r\n',r'\n')
                book[k] = book[k].replace('\n',r'\n')
                rdes = r'\n' + book[k] + r'\n\n'
            elif k == 'price':
                rdes = str(book[k]) + r'元\n\n'
            else:
                rdes = str(book[k]) + r'\n'
            des += '【%s】 %s' % (v, rdes)
    print('des:', len(des))
    print(des)
    return des[0:2100]

def gbk2utf8(d):
    keys = d.keys()
    for k in keys:
        if isinstance(d[k], str):
            d[k] = d[k].decode('gbk').encode('utf8')
            # d[k] = quote(d[k])
    return d

sql = "select * from goodsall where quantity>0 order by quantity desc limit 50,30"
sql = "select a.*,etag,b.des ctag from goodsall a join xy_category b on dkind=cdes " \
      "where quantity>0  and  cdes>'' and a.id=612894" \
      " order by quantity desc limit 0,10"
print(sql)
curs.execute(sql)
books= curs.fetchall()

for book in books:
    if len(book['isbn']) == 13:
        book = gbk2utf8(book)
        print book
        name = book['des']
        area = book['area']
        description = formatdes(book)
        writer = book['writer']
        writer = writer.replace('　','')
        writer = writer.replace(' ','')
        name = name + (book['odes'] or '') + (book['series'] or '') + writer + (reverseDes(book['ctag']) or '') \
               +area + (book['etag'] or '') \
                + '书籍Book'
        add_item(book, book['id'], name, book['price'], book['quantity'], description)
    else:
        book = gbk2utf8(book)
        print(book)
        print(book['isbn'])
        print(book['des'])

