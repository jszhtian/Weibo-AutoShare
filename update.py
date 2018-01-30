#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os,sys

url_post_a_text = "https://api.weibo.com/2/statuses/share.json"
playload = {
"access_token":"2.00nLmLVG0LyRq68fbfedeeaa0MyQjW",
"status":"This is a text test"
}
r = requests.post(url_post_a_text,data = playload)
print (r.text)