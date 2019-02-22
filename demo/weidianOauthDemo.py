from flask import  Flask,request,redirect
from oauth.WeidianOauth import Oauth4SelfUseClient,OauthClient
import Global
app=Flask(__name__)
app_key=Global.app_key
app_sec="69c972307ab84405b647f107819d051e"
redirect_url="http://wd.com:5000/token"
client=OauthClient(app_key,app_sec,redirect_uri=redirect_url)
@app.route("/auth")

def get_auth():
    client=OauthClient(app_key,app_sec,redirect_uri="http://wd.com:5000/token")
    url=client.get_auth_url()
    return  redirect(url)

@app.route("/token")
def get_token():
    code=request.args.get("code")
    token=client.get_access_token(code)
    return str(token)

@app.route("/selfToken")
def get_selftoken():
    self_use_app_key="632470"
    self_use_app_secret="587a9638ce307c5e2900a40e390c2b40"
    client= Oauth4SelfUseClient(app_key=self_use_app_key,app_secret=self_use_app_secret)
    token=client.get_token()
    return str(token)

if __name__=="__main__":
    app.run(port=5000)

