#!/usr/bin/env python
#  Raspberry Pi Personal assistant
#
#  Sai Yamanoor & Srihari Yamanoor
#  yamanoorsai@gmail.com
#

import sys
import feedparser

newEmail=""
username="username@gmail.com"
password="password"
proto="https://"
server="mail.google.com"
path="/gmail/feed/atom"




def mail():
    email = int(feedparser.parse(proto+username+":"+password+"@"+server+path)["feed"]["fullcount"])
    return email
    
