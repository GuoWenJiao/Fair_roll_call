#!/usr/bin/env python
# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui
import random,os,time
import pandas as pd


# 中文字体
text_font = 'SimSun'
winsize = [1920,1080]
win = visual.Window(winsize,fullscr=True,color='#D0D0D0',units='pix')
def drawimage(image1,location = [-290,-12.5]):
    pic = visual.ImageStim(win, image= image1, pos=location)
    pic.draw(win)
def drawText(text,location=[0,0],color=[-1, -1, -1],height= 50):
    text = visual.TextStim(win, text=text, pos=location,color=color,height=height,font=text_font)
    text.draw(win)



# 读文件
path = os.path.abspath('.')
df = pd.read_csv(path+'/num_file/xuehao.csv', encoding='utf-8-sig')
num_list = []
num_list_file = df['学号']
for j in num_list_file:
    num_list.append(j)
print(len(num_list))
text = '1'
text_list = []
# text_list = ['\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n']
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
        # facted_secong += 1
        drawText(str(int(time_gap)),[250,0],'red',100)
    if time_gap > duration :
        print('计时结束啦')
        # drawText('计时结束啦!',[0,-384],[1, 0, 0])
        drawText(str(int(time_gap)),[250,0],'red',100)
        drawText(text,[0,locationx -xiaxian])
        win.flip()
        # win.flip()
        while thisResp is None:
            allKeys = event.waitKeys()
            for thisKey in allKeys:
                if thisKey == 'space':
                    thisResp = True
                elif thisKey in ['space', 'escape']:
                    thisResp = True
                    break  # abort experiment
            if thisResp == True:    # time.sleep(5)
                break
        # if thisResp == True:    # time.sleep(5)
        #     break
    if thisResp == True:    # time.sleep(5)
            break
    # elif len(text_list) > chengxianhangshu:
    #     # if locationx %(height/2) != 0 or is_add == True:
    #     if locationx %(height/2) != 0:
    #         locationx += move_juli
    #         #shishi
    #         drawText(text,[0,locationx -xiaxian])
    #         print(text,locationx)
    #         win.flip()
    #         time.sleep(stop_time)
    #         is_add = False
    #
    #     elif locationx %(height/2) == 0 :
    #         if is_add == False:
    #             text_list.pop(0)
    #             selected_num = random.choice(list(num_list))
    #             text_list.append(str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n')
    #             text = ''
    #             for i in text_list:
    #                 text += i
    #             #shishi
    #             locationx = 0.5* height*len(text_list)
    #             drawText(text,[0,locationx -xiaxian])
    #             print(text,locationx)
    #             win.flip()
    #             time.sleep(stop_time)
    #             is_add = True
    #         elif is_add == True:
    #             locationx += move_juli
    #             #shishi
    #             drawText(text,[0,locationx -xiaxian])
    #             print(text,locationx)
    #             win.flip()
    #             time.sleep(stop_time)
    #             is_add = False

    # elif len(text_list) == chengxianhangshu:
    if locationx %(height/2) != 0 :
        # if is_add == True:
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
                 
    # else:
    print(locationx,is_add)
        # locationx += move_juli
        # drawText(text,[0,locationx -364])
        # print(text,locationx)
        # win.flip()
        # time.sleep(0.1)
        # is_add = False

        # break

