# remove_no_label_image.py
# encoding:utf-8

import os

cur_dir='C:\\Users\\Jesse Mx\\Desktop'
txt_dir=os.path.join(cur_dir,'labels') # 标注txt文件夹地址
pic_dir=os.path.join(cur_dir,'image-half') # 图片集文件夹地址
txtlist=[]
piclist=[]
for parent,dirnames,filenames in os.walk(txt_dir):
    for txt_name in filenames:
        txt_name=txt_name[:-4]
        txtlist.append(txt_name)
for parent,dirnames,filenames in os.walk(pic_dir):
    for pic_name in filenames:
        pic_name=pic_name[:-4]
        piclist.append(pic_name)
txt_set=set(txtlist)
pic_set=set(piclist)
comp=pic_set.difference(txt_set) # 求补集

print("ok")
print(len(comp)) # 无标注图片数量

for item in comp:
    file=pic_dir+'\\'+item+'.jpg'
    if os.path.exists(file):
        os.remove(file)
        print(file)
