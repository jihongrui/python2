#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "jihongrui@jsqix.com"
import subprocess

ip_check_url = 'http://python.1876.cn/weixin/'

pip = "122.228.179.178:80"

command = ["curl","-x",pip,ip_check_url]
subprocess.Popen()