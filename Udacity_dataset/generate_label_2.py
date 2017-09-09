# generate_label_2.py
# encoding:utf-8
file=open('D:\\DataSet\\labels.txt','r') # 原始labels.txt的地址
for eachline in file:
    data=eachline.strip().split(' ')
    filename=data[0]
    filename=filename[:-4]
    txt_path='D:\\DataSet\\labels\\'+filename+'.txt' # 生成的txt标注文件地址
    txt=open(txt_path,'a')
    if data[6]!='trafficLight': # 忽略信号灯的标注信息    
        new_line=data[6]+' '+str(int(data[1])/2)+' '+str(int(data[2])/2)+' '+str(int(data[3])/2)+' '+str(int(data[4])/2) # 使用了1/4图片尺寸，坐标均除以2
        txt.writelines(new_line)
        txt.write('\n')
        txt.close()
file.close()
print('generate label success')
