#微店开放平台sdk python版

##当前版本信息

    当前版本： V0.1.0
    发布日期： 2015-11-10

##修改历史

    V0.1.0  2015-11-10  版本发布。

##文件结构信息

    category/
        Category.py:            商品分类的相关接口

    cps /
        Cps.py:                 商品Cps相关信息接口

    demo/
        weidianOauthDemo.py:    Oauth的Demo

    img/
        Uploader.py:            图片上传接口

    item/
        Item.py:                商品信息相关的接口

    oauth/
        WeidianOauth.py:        授权验证的相关接口

    order/
        Order.py:               订单信息的相关接口

    util/
        ErrorInfo.py:           错误信息的相关接口
        OpenRequest.py:         Request的相关接口

    readme.md                   使用须知

    test/                       运行测试需要将项目地址设置到环境变量
                                    例如:PYTHONPATH=/Users/your_name/weidian_sdk_python
                                        export PYTHONPATH
        TestCategory.py:        商品分类接口的相关测试代码
        TestCps.py:             Cps接口的相关测试代码
        TestItem.py:            商品信息相关接口的测试代码
        TestOrder.py:           订单相关接口的测试代码
        TestUploader.py:        图片上传接口的测试代码
    
 

    微店开放平台api还在不断增加中，详见： http://wiki.open.weidian.com/

##使用示例说明

   具体接口使用示例请参考test中对应使用示例。
   对于示例中未使用的参数可以依据需要参考接口文档进行添加。
   

##联系我们
    微店开放平台官网：https://web.open.weidian.com/index
    可以访问我们的资料库获得详尽的技术文档：https://wiki.open.weidian.com/
    在线接口测试工具： https://web.open.weidian.com/playground/index
    此外，您可以通过企业QQ群 (577531386) 直接咨询