#!/usr/bin/env python
# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui
import random,os,time
import pandas as pd

height = 50
# 中文字体
text_font = 'SimSun'
win = visual.Window([1920,1080],fullscr=True,color='#D0D0D0',units='pix')
def drawimage(image1,location = [-300,0]):
    pic = visual.ImageStim(win, image= image1, pos=location)
    pic.draw(win)
def drawText(text,location=[0,0],color=[-1, -1, -1]):
    text = visual.TextStim(win, text=text, pos=location,color=[-1, -1, -1],height=height,font=text_font)
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
locationx = 0
t1 = time.clock()
chengxianhangshu = 10
move_juli = 5 #每次移动的距离
is_add = False
for i in range(134):
    drawimage('zhizheng.png')
    # win.flip()
    t2 = time.clock()
    print(t1-t2 )
    if t2 - t1 > 20:
        print('计时结束啦')
        drawText('计时结束啦!',[0,-384],[1, 0, 0])
        win.flip()
        time.sleep(5)
        break
    if len(text_list) < chengxianhangshu: # 有21行
        if locationx == 0 or is_add == True:
            # locationx += 5
            selected_num = random.choice(list(num_list))
            xintext = str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
            text_list.append(xintext)
            # text += str(selected_num)  + '\n'
            text += str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
            #shishi
            drawText(text,[0,locationx -304])
            print(text,locationx)
            win.flip()
            time.sleep(0.016)
            locationx += move_juli
            is_add = False

        elif locationx %(height/2) != 0 or is_add == True:
            #shishi
            drawText(text,[0,locationx -304])
            print(text,locationx)
            win.flip()
            time.sleep(0.016)
            locationx += move_juli
            is_add = False
        elif locationx %(height/2) == 0 and locationx != 0 :
            if is_add == False:
                # locationx += 5
                locationx=  0.5* height*len(text_list)
                selected_num = random.choice(list(num_list))
                xintext = str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n'
                text_list.append(xintext)
                # text += str(selected_num)  + '\n'
                text += xintext
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
                is_add = True
            if is_add == True:
                locationx += move_juli
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
                is_add = False
    elif len(text_list) > chengxianhangshu:
        if locationx %(height/2) != 0 or is_add == True:
            locationx += move_juli
            #shishi
            drawText(text,[0,locationx -304])
            print(text,locationx)
            win.flip()
            time.sleep(0.016)
            is_add = False

        elif locationx %(height/2) == 0 :
            if is_add == False:
                text_list.pop(0)
                locationx = 0.5* height*len(text_list)
                selected_num = random.choice(list(num_list))
                text_list.append(str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n')
                text = ''
                for i in text_list:
                    text += i
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
                is_add = True
            elif is_add == True:
                locationx += move_juli
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
                is_add = False

    elif len(text_list) == chengxianhangshu:
        if locationx %(height/2) != 0 or is_add == True:
            locationx += move_juli
            #shishi
            drawText(text,[0,locationx -304])
            print(text,locationx)
            win.flip()
            time.sleep(0.016)
            is_add = False

        elif locationx %(height/2) == 0 :
            if is_add == False:
                text_list.pop(0)
                locationx = 0.5*  height*len(text_list)
                selected_num = random.choice(list(num_list))
                text_list.append(str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n')
                text = ''
                for i in text_list:
                    text += i
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
                is_add = True
            elif is_add == True:
                locationx += move_juli
                #shishi
                drawText(text,[0,locationx -304])
                print(text,locationx)
                win.flip()
                time.sleep(0.016)
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

