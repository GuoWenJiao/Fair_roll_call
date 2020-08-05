#!/usr/bin/env python
# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui
import random,os,time
import pandas as pd

height = 30
def drawText(text,location=[0,0],color=[-1, -1, -1]):
    text = visual.TextStim(win, text=text, pos=location,color=[-1, -1, -1],height=height,font=text_font)
    text.draw()

# 中文字体
text_font = 'SimSun'
win = visual.Window([1024,768],fullscr=True,color='#D0D0D0',units='pix')

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
locationx = 0
t1 = time.clock()
for i in range(134):
    t2 = time.clock()
    print(t1-t2 )
    if t2 - t1 > 20:
        print('计时结束啦')
        drawText('计时结束啦!',[0,-384],[1, 0, 0])
        win.flip()
        time.sleep(1)
        break
    if len(text_list) < 21: # 有21行
        if locationx == 0:
            selected_num = random.choice(list(num_list))
            xintext = str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
            text_list.append(xintext)
            text += str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
            locationx += 5
        elif locationx %(height/2) != 0:
            locationx += 5
        elif locationx %height == 0 and locationx != 0:
            # locationx += 5
            locationx =  height*len(num_list)
            selected_num = random.choice(list(num_list))
            xintext = str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
            text_list.append(xintext)
            text += str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'