#!/usr/bin/env python
# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui
import random,os,time
import pandas as pd

# 获得某路径csv文件名list
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.csv':
                # L.append(os.path.join(root, file))
                L.append(os.path.splitext(file)[0])
    return L
# 老师选择一下嘛
def Get_Class(class_list):
    myDlg = gui.Dlg(title="Choice Class")
    myDlg.addText("---------------Choice Class-------------")
    myDlg.addField('Class:',choices=class_list)
    myDlg.show()
    if myDlg.OK:
        thisInfo = myDlg.data
    else:
        exit(0)
    choiced_class = {}
    choiced_class['Class'] = thisInfo[0]
    return choiced_class


def drawimage(image1,location = [-290,-12.5]):
    pic = visual.ImageStim(win, image= image1, pos=location)
    pic.draw(win)
def drawText(text,location=[0,0],color=[-1, -1, -1],height= 50):
    text = visual.TextStim(win, text=text, pos=location,color=color,height=height,font=text_font)
    text.draw(win)
# 选择、读取文件
path = os.path.abspath('.')
class_list = file_name(path)
choiced_class = Get_Class(class_list)
df = pd.read_csv(path+'/num_file/'+ choiced_class['Class'] + '.csv', encoding='utf-8-sig')
print(df)

num_list = []
num_list_file = df['学号']
for j in num_list_file:
    num_list.append(j)
print(len(num_list))
# 中文字体 窗口
text_font = 'SimSun'  # 字体
winsize = [1920,1080] # 窗口大小
win = visual.Window(winsize,fullscr=True,color='#D0D0D0',units='pix')
text_list = []
locationx = 0
t1 = time.clock()
chengxianhangshu = 11 # 屏幕呈现多少行字
height = 50 # 字有多大
# 先填充n行空白文字
for i in range(chengxianhangshu):
    text_list.append('\n')
move_juli = 5 #每次移动的距离
duration = 15 # 倒计时持续时间
stop_time = 0.0166 # 刷新到下一屏的间隔时间
xiaxian = 0.5 * ((chengxianhangshu)*height)# 最最下方的y坐标
is_add = False
facted_secong = [] # 秒数取整用于比较
for i in range(duration+1):
    facted_secong.append(i)
thisResp = None
# facted_secong = -1
for i in range(3000):
    drawimage('zhizheng.png')
    # win.flip()
    t2 = time.clock()
    print(t2- t1)
    time_gap = t2- t1
    if int(time_gap) in facted_secong:
        drawText(str(int(time_gap)),[250,0],'red',100)
    if time_gap > duration :
        drawText(str(int(time_gap)),[250,0],'red',100) #为了补上暂停时的一秒的画面
        drawText(text,[0,locationx -xiaxian])
        win.flip()
        # win.flip()
        # 计时结束按空格退出
        while thisResp is None:
            allKeys = event.waitKeys()
            for thisKey in allKeys:
                if thisKey == 'space':
                    thisResp = True
                elif thisKey in ['space', 'escape']:
                    thisResp = True
                    break
            if thisResp == True:
                break
    if thisResp == True:
            break
    if locationx %(height/2) != 0 :
        locationx += move_juli
        #shishi
        drawText(text,[0,locationx -xiaxian])
        print(text,locationx)
        win.flip()
        time.sleep(stop_time)
        is_add = False
    elif locationx %(height/2) == 0 or locationx == 0:
        if is_add == False:
            text_list.pop(0)
            selected_num = random.choice(list(num_list))
            text_list.append(str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n')
            text = ''
            for i in text_list:
                text += i
            #shishi
            locationx = 0.5*  height*len(text_list)
            drawText(text,[0,locationx -xiaxian])
            print(text,locationx)
            win.flip()
            time.sleep(stop_time)
            is_add = True
        elif is_add == True:
            locationx += move_juli
            #shishi
            drawText(text,[0,locationx -xiaxian])
            print(text,locationx)
            win.flip()
            time.sleep(stop_time)
            is_add = False
    print(locationx,is_add)
