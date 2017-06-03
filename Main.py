#!python3
#encoding:utf-8
from authentication.Authentication import Authentication
from authentication.NonAuthentication import NonAuthentication
from authentication.BasicAuthentication import BasicAuthentication
from authentication.TwoFactorAuthentication import TwoFactorAuthentication
from authentication.OAuthAuthentication import OAuthAuthentication
from authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
class Main:
    def __init__(self):
        pass
    def Run(self):
        reqp = RequestParameter.RequestParameter()
