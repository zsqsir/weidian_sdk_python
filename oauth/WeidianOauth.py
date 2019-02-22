# -*- coding: utf-8 -*-
__author__ = 'Seven'
'''
Python SDK for Weidian Open OAuth 2.
'''

import  json, time,logging
from util.ErrorInfo import OpenError
from util import  OpenRequest

class Oauth4SelfUseClient():
    def __init__(self, app_key,app_secret,  domain='api.vdian.com', version='1'):
        self.app_key = str(app_key)
        self.app_secret=app_secret
        self.access_token_url = 'https://%s/token' % domain
        self.expires = 0.0
        self.token=""

    def get_token(self):
        params={"appkey":self.app_key,"secret":self.app_secret,"grant_type":"client_credential"}
        now=time.time()
        body=OpenRequest.http_get(self.access_token_url,params=params)
        rootResult=json.loads(body)
        access_token=""
        expire_at=0
        try:
            if((rootResult is not None) and (rootResult.get("result") is not None)):
                result=rootResult.get("result")
                access_token=result.get("access_token")
                expire_at=int(now)+int(result.get("expire_in"))
        except  Exception:
            raise OpenError("10001","获取AccessToken出错",None)
        return (access_token,expire_at)


class OauthClient(object):
    def __init__(self, app_key,app_secret, redirect_uri=None, response_type='code', domain='api.vdian.com'):
        self.app_key = str(app_key)
        self.app_secret=app_secret
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.auth_url = 'https://%s/oauth2/authorize' % domain
        self.access_token_url = 'https://%s/oauth2/access_token' % domain
        self.refresh_url = 'https://%s/oauth2/refresh_token' % domain
        self.access_token = None
        self.expires = 0.0

    def get_access_token(self,code):
        params={"appkey":self.app_key,"secret":self.app_secret,"code":code,"grant_type":"authorization_code"}
        now=time.time()
        body=OpenRequest.http_get(self.access_token_url,params=params)
        rootResult=json.loads(body)
        access_token=""
        expire_at=0
        try:
            if((rootResult is not None) and (rootResult.get("result") is not None)):
                result=rootResult.get("result")
                access_token=result.get("access_token")
                expire_at=int(now)+int(result.get("expire_in"))
        except  Exception:
            raise OpenError("10001","获取AccessToken出错",None)
        return (access_token,expire_at)

    def get_auth_url(self,state="state"):
        if state is None or state =='':
            state="state"
        params={"appkey":self.app_key,"redirect_uri":self.redirect_uri,"response_type":"code","state":state}
        # print OpenRequest._encode_params(**params)
        url=self.auth_url+"?"+OpenRequest._encode_params(**params)
        return url



    def refresh_token(self,refresh_token):
        params={"appkey":self.app_key,"refresh_token":refresh_token,"grant_type":"refresh_token"}
        now=time.time()
        body=OpenRequest.http_get(self.refresh_url,params)
        resJson=json.loads(body)
        if(resJson.get("result") is None):
            raise  OpenError("10001","刷新token出错了")
        else:
            resultJson=resJson.get("result")
            access_token=resJson.get("access_token")
            expires_at=int(now)+int(resJson.get("expire_in"))
            refresh_token=resJson.get("refresh_token")
            return(access_token,expires_at,refresh_token)

    def isExpires(self,expire_at):
        if expire_at>int(time.time()):
            return True
        else:
            return False;
if __name__=='__main__':
    pass

    # param={"grant_type":"client_credential","appkey":"632714","secret":"96a1c6a5f43ca2ad3ca76e95559cba43"}
    # url="https://api.vdian.com/token"
    # body=http_get(url,param)
    # result=json.loads(body)
    #
    #
    # print result["status"]["status_reason"]
    # print result.get("sdf")