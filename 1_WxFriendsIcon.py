# -*- coding:utf-8 -*-
import itchat
import os
import math
import PIL.Image as Image
import sys

itchat.auto_login()
friends = itchat.get_friends(update=True)
friendsNum = len(friends)
user = friends[0]["PYQuanPin"][0:]
print(user,' have ',friendsNum,' friends.')
os.mkdir(user)
os.chdir(user)

for i in friends:
    try:
        i['img'] = itchat.get_head_img(userName=i["UserName"])
        i['ImageName'] = i["UserName"][1:] + '.jpg'
    except:
        print('Get '+i["UserName"][1:]+' fail')
    fileImage = open(i['ImageName'],'wb')
    fileImage.write(i['img'])
    fileImage.close()

imageList = os.listdir(os.getcwd())
imageNum = len(imageList)

eachSize = 64
eachLine = int(math.sqrt(imageNum)) + 1
print("单个图像边长", eachSize, "像素；每行共", eachLine, "个图像；最终图像边长", eachSize*eachLine)

toImage = Image.new('RGB', (eachSize*eachLine, eachSize*eachLine))
x = 0
y = 0
for i in imageList:
    try:
        img = Image.open(i)
    except:
        print("打开图像失败", i)
    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
    toImage.paste(img, (x*eachSize, y*eachSize))
    x += 1
    if  x == eachLine:
        x = 0
        y += 1
print("图像拼接完成")

toImage.show()

os.chdir(os.path.pardir)

iconName = friends[0]["PYQuanPin"][0:]+".jpg"
toImage.save(iconName)
itchat.send_image(iconName, "filehelper")

itchat.logout()

