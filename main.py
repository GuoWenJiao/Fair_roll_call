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

# opacity 调整透明度 1 不透明 0透明 浮点数
def drawimage(image1,size,location = [-290,0],opacity =1):
    pic = visual.ImageStim(win, image= image1, pos=location,size = (size[0], size[1]),opacity = opacity)
    pic.draw(win)
def drawText(text,location=[0,0],color=[-1, -1, -1],height= 150):
    text = visual.TextStim(win, text=text, pos=location,color=color,height=height,font=text_font,bold=True)
    text.draw(win)
# 选择、读取文件
path = os.path.abspath('.')
class_list = file_name(path)
# 如果只有一个文件，直接读该文件，如果有多个文件，可以选择文件
if len(class_list) == 1:
    df = pd.read_csv(path+'/num_file/'+ class_list[0] + '.csv', encoding='utf-8-sig')
elif len(class_list) > 1:
    choiced_class = Get_Class(class_list)
    df = pd.read_csv(path+'/num_file/'+ choiced_class['Class'] + '.csv', encoding='utf-8-sig')
elif len(class_list) == 0:
    print('请在‘num_file中添加文件’')
num_list = []
num_list_file = df['学号']
for j in num_list_file:
    num_list.append(j)

# 中文字体 窗口
text_font = 'SimSun'  # 字体
winsize = [1920,1080] # 窗口大小
win = visual.Window(winsize,fullscr=True,color='#D0D0D0',units='pix')
text_list = []
#--------------------------------------------------------------
# 调试时的一些参数
duration = 10 # 倒计时持续时间
chengxianhangshu = 1 # 屏幕呈现多少行字
height = 150 # 字有多大
move_juli = 5 #每次移动的距离
count_down_location = [-0,-50] # 倒计时的位置
text_x = -370  # text的横坐标
stop_time = 0.0016 # 刷新到下一屏的间隔时间
# 循环前的一些参数和列表的填充
time_gap = 0
locationy = 0  # 最初的文字的纵坐标
# xiaxian = 0.5 * ((chengxianhangshu)*height)# 最最下方文字的y坐标
xiaxian = -200
#--------------------------------------------------
is_add = False # 该循环是否添加新的一行
facted_secong = [] # 秒数取整用于比较
for i in range(duration+1):
    facted_secong.append(i)
thisResp = None
# 先填充n行空白文字
for i in range(chengxianhangshu):
    text_list.append('\n')
t1 = time.clock()
image = random.randint(1,9)
while True:
    drawimage('image/' + str(image) + '.png',[1920,1080],[0,0],opacity = 0.7)
    # drawimage('image/3.png',[1920*0.3,1080*0.3],[500,-150],opacity = 1)
    drawimage('image/kuang.png',[1400,height + 20],[0,height-xiaxian],opacity = 0.6)
    t2 = time.clock()
    time_gap = t2 - t1
    if int(time_gap) in facted_secong:
        drawText(str(facted_secong[-( int(time_gap)+1)]),[count_down_location[0],count_down_location[1]],'red',500)
    if str(facted_secong[-( int(time_gap)+1)])== '0':
        drawText('0',[count_down_location[0],count_down_location[1]],'red',500) #为了补上暂停时的一秒的画面)
        drawText(text,[text_x,locationy-xiaxian])
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
    text_list.pop(0)
    selected_num = random.choice(list(num_list))
    text_list.append(str(selected_num) + ':' + df['姓名'][num_list.index(selected_num)] + '\n')
    text = ''
    for i in text_list:
        text += i
    locationy = 0.5*  height*len(text_list)
    drawText(text,[text_x,locationy -xiaxian])
    win.flip()
    time.sleep(stop_time)