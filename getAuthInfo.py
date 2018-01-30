#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os,sys

url_get_token = "https://api.weibo.com/oauth2/get_token_info"
payload={
    "access_token":"2.00nLmLVG0LyRq68fbfedeeaa0MyQjW"
}
r=requests.post(url_get_token,data=payload)
print (r.text)