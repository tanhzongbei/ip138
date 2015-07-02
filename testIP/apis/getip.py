#coding:utf8 
#__author__ = 'xiaobei'
#__time__= '7/2/15'

import flask
from flask import request
from testIP.core import success_response, error_response, application
from testIP.core.config import C
from utils.urltools import curl

@application.route('/testIP/ip', methods=['GET'])
def ip():
    headers = request.headers.environ
    ip = headers.get('REMOTE_ADDR', '')
    port = headers.get('REMOTE_PORT', '')
    return success_response({'ip' : ip, 'port' : port})


@application.route('/testIP/ip138', methods = ['GET'])
def fullip():
    headers = request.headers.environ
    ip = headers.get('REMOTE_ADDR', '')
    port = headers.get('REMOTE_PORT', '')
    url = 'http://api.map.baidu.com/location/ip?' + 'ak=%s&' % C.BAIDU_AK + '&ip=%s&coor=bd09ll' % (str(ip))
    res = curl.openurl(url)
    addr = ''
    if res and res['status'] == 0:
        addr = res['content']['address']

    return success_response({'ip' : ip, 'port' : port, 'addr':addr})