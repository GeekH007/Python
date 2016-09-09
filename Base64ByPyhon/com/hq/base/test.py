'''
Created on 2016��9��8��

@author: Administrator
'''
# （1）import qrcode :引入qrcode库
# （2）from PIL import Image：引入Pillow库，注意写法哦
# （3）q=qrcode.main.QRCode（)：定义q变量
# （4）q.add_data(" ")：设置二维码内容，可以是文字，也可以是链接
# （5）m=q.make_image()：生成二维码图像
# （6）m.save("hello.png")：保存图像为指定名称