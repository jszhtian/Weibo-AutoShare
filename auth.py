#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os,sys

url_get_token = "https://api.weibo.com/oauth2/access_token"
payload={
    "client_id":"381870535",
    "client_secret":"f4c57acf40cfce02b67679de62c0bc64",
    "grant_type":"authorization_code",
    "code":"3350f0ca5335c5ee44abbfe50f178b8f",
    "redirect_uri":"https://api.weibo.com/oauth2/default.html"
}
r=requests.post(url_get_token,data=payload)
print (r.text)