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

# drawText('1 \n 2',location=[0,0],color=[-1, -1, -1])
drawText('111111111111111\n22222222222222\n333333333333',location=[0,0],color=[-1, -1, -1])
win.flip()
time.sleep(3)