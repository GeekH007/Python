#coding:utf-8
'''
Created on 2016年9月8日

@author: Administrator
'''
import base64
#Base64加密
def base(info):
    #转成bytes string
    bytesString = info.encode(encoding="utf-8")
    bm = base64.b64encode(bytesString)    #加密
    # jm = base64.b64decode(bm) # python base64解码      
    print('加密')
    print(bm)
    print(bm.decode())
    print("解码")
    decodestr = base64.b64decode(bm)
    print(decodestr)


base('aes-256-cfb:83228762@USA.ISS.TF:23456')

