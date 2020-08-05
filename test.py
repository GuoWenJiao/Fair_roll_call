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
path = os.path.abspath('.')
class_list = file_name(path)
choiced_class = Get_Class(class_list)
df = pd.read_csv(path+'/num_file/'+ choiced_class['Class'] + '.csv', encoding='utf-8-sig')
print(df)
#
# height = 50
# # 中文字体
# text_font = 'SimSun'
# win = visual.Window([1920,1080],fullscr=True,color='#D0D0D0',units='pix')
# def drawimage(image1,location = [-300,0]):
#     pic = visual.ImageStim(win, image= image1, pos=location)
#     pic.draw(win)
# def drawText(text,location=[0,0],color=[-1, -1, -1]):
#     text = visual.TextStim(win, text=text, pos=location,color=[-1, -1, -1],height=height,font=text_font)
#     text.draw(win)
#
# # drawText('1 \n 2',location=[0,0],color=[-1, -1, -1])
# drawText('111111111111111\n22222222222222\n333333333333',location=[0,0],color=[-1, -1, -1])
# win.flip()
# time.sleep(3)