# -*- coding:utf8 -*-
__author__ = 'Seven'

import  Global
from img import Uploader
domain=Global.domain
token=Global.token
app_key=Global.app_key

def test_upload_img():
    file_path="//a/k/phpdoc/tbpic/53/532342.jpg"
    # file_path=""
    result=Uploader.upload_img(token,file_path)
    print result;

if __name__=="__main__":
    try:
        test_upload_img();
    except Exception,e:
        print e
