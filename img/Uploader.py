# -*- coding:utf8 -*-
__author__ = 'Seven'

import  json,logging,Global,urllib2,time,os
from util import  ErrorInfo
domain=Global.domain
token=Global.token
app_key=Global.app_key

def upload_img(access_token,file_path,path="media/upload"):
    """
    使用场景
        图片上传

    方法名称
        weidian.item.onSale

    wiki
        http://wiki.open.weidian.com/index.php?title=%E4%B8%8A%E4%BC%A0%E5%95%86%E5%93%81%E5%9B%BE%E7%89%87
    """
    if(not access_token or not os.path.exists(file_path)):
        raise ErrorInfo("10001","参数错误")

    boundary = '------------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)

    data.append('Content-Disposition: form-data; name="%s"\r\n' % "access_token")
    data.append(token)
    data.append('--%s' % boundary)


    fr=open(file_path,'rb')
    file_name=file_path[file_path.rfind("/")+1:]
    data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('media',file_name))
    data.append('Content-Type: %s\r\n' % 'image/png')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)

    http_body='\r\n'.join(data)
    http_url="%s%s" %(domain,path)
    try:
        req=urllib2.Request(http_url, data=http_body)
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        content = urllib2.urlopen(req, timeout=5).read()
        return  json.loads(content)

    except Exception,e:
        logging.error(e)


