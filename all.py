# -*- encoding=utf8 -*-
__author__ = "yinguai"

from airtest.core.api import *

auto_setup(__file__)
#启动游戏
touch(Template(r"tpl1674117226075.png", record_pos=(0.071, -0.147), resolution=(1600, 900)))
sleep(10.0)
touch(Template(r"tpl1674117261859.png", record_pos=(0.001, 0.187), resolution=(1600, 900)))
sleep(20.0)
touch(Template(r"tpl1674117289028.png", record_pos=(0.444, 0.184), resolution=(1600, 900)))
sleep(20.0)

#关公告加签到（if）
if exists(Template(r"tpl1674178960023.png", threshold=0.9, record_pos=(0.416, -0.226), resolution=(1600, 900))):
    touch(Template(r"tpl1674178960023.png", record_pos=(0.416, -0.226), resolution=(1600, 900)))
    sleep(2.0)
    touch(Template(r"tpl1674179018507.png", record_pos=(-0.322, -0.251), resolution=(1600, 900)))
    sleep(2.0)
    touch(Template(r"tpl1674179036494.png", record_pos=(-0.434, -0.255), resolution=(1600, 900)))
    sleep(2.0)

#后勤（if）
if exists(Template(r"tpl1674179148369.png", threshold=0.9, record_pos=(0.396, 0.239), resolution=(1600, 900))):
    touch(Template(r"tpl1674179148369.png", record_pos=(0.396, 0.239), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674179164179.png", record_pos=(0.086, 0.099), resolution=(1600, 900)))
    sleep(5.0)

#收邮件
touch(Template(r"tpl1674117664709.png", record_pos=(0.374, 0.247), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674117684967.png", record_pos=(-0.411, 0.231), resolution=(1600, 900)))
sleep(8.0)
if exists(Template(r"tpl1674179115156.png", threshold=0.9, record_pos=(-0.246, -0.248), resolution=(1600, 900))):
    touch(Template(r"tpl1674179115156.png", record_pos=(-0.246, -0.248), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674117771839.png", record_pos=(-0.406, -0.237), resolution=(1600, 900)))
sleep(3.0)

#建造-步枪
touch(Template(r"tpl1674118483987.png", record_pos=(0.389, -0.059), resolution=(1600, 900)))
sleep(3.0)
if exists(Template(r"tpl1674179390639.png", record_pos=(-0.296, 0.244), resolution=(1600, 900))):
    touch(Template(r"tpl1674179390639.png", record_pos=(-0.296, 0.244), resolution=(1600, 900)))
    sleep(10.0)
    if exists(Template(r"tpl1674194654088.png", threshold=0.9, record_pos=(-0.147, 0.099), resolution=(1600, 900))):
        touch(Template(r"tpl1674194667582.png", record_pos=(0.06, 0.108), resolution=(1600, 900)))

    elif exists(Template(r"tpl1674179370479.png", record_pos=(0.344, 0.204), resolution=(1600, 900))):
        touch(Template(r"tpl1674179370479.png", record_pos=(0.344, 0.204), resolution=(1600, 900)))
        sleep(5.0)
        touch(Template(r"tpl1674118561672.png", record_pos=(-0.156, -0.091), resolution=(1600, 900)))
        sleep(2.0)
        touch(Template(r"tpl1674118580188.png", record_pos=(-0.292, 0.096), resolution=(1600, 900)))
        sleep(2.0)
        touch(Template(r"tpl1674118645493.png", record_pos=(-0.427, -0.082), resolution=(1600, 900)))
        sleep(2.0)
        touch(Template(r"tpl1674118661651.png", record_pos=(0.34, -0.148), resolution=(1600, 900)))
        sleep(2.0)
        touch(Template(r"tpl1674118714907.png", record_pos=(-0.262, 0.236), resolution=(1600, 900)))
        sleep(3.0)
touch(Template(r"tpl1674118734627.png", record_pos=(-0.414, -0.241), resolution=(1600, 900)))
sleep(3.0)

#建造装备
touch(Template(r"tpl1674118483987.png", record_pos=(0.389, -0.059), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674196725316.png", record_pos=(-0.426, 0.109), resolution=(1600, 900)))
sleep(3.0)
if exists(Template(r"tpl1674197025506.png", record_pos=(-0.298, 0.244), resolution=(1600, 900))):
    touch(Template(r"tpl1674197025506.png", record_pos=(-0.298, 0.244), resolution=(1600, 900)))
    sleep(8.0)
    if exists(Template(r"tpl1674197038908.png", record_pos=(-0.083, -0.039), resolution=(1600, 900))):
        touch(Template(r"tpl1674197047766.png", record_pos=(0.064, 0.113), resolution=(1600, 900)))
        sleep(3.0)
    else:
        touch(Template(r"tpl1674197076468.png", record_pos=(0.341, 0.199), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674196771592.png", record_pos=(-0.102, -0.099), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674196782911.png", record_pos=(-0.291, 0.095), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674196925430.png", record_pos=(-0.418, -0.086), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674196939572.png", record_pos=(0.341, -0.152), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674196955221.png", record_pos=(-0.261, 0.232), resolution=(1600, 900)))
        sleep(3.0)
touch(Template(r"tpl1674197094808.png", record_pos=(-0.42, -0.244), resolution=(1600, 900)))
sleep(5.0)

#情报中心
touch(Template(r"tpl1674117378368.png", record_pos=(0.389, -0.059), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674117405896.png", record_pos=(-0.333, -0.238), resolution=(1600, 900)))
sleep(2.0)
touch(Template(r"tpl1674117433817.png", record_pos=(0.269, -0.099), resolution=(1600, 900)))
sleep(8.0)
touch(Template(r"tpl1674117461537.png", record_pos=(0.198, 0.237), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674117481430.png", record_pos=(-0.416, -0.036), resolution=(1600, 900)))
sleep(8.0)
if exists(Template(r"tpl1674194828584.png", threshold=0.9, record_pos=(-0.084, -0.037), resolution=(1600, 900))):
    touch(Template(r"tpl1674194838250.png", record_pos=(0.054, 0.109), resolution=(1600, 900)))
else:
    touch(Template(r"tpl1674117501027.png", record_pos=(0.198, 0.237), resolution=(1600, 900)))
    sleep(8.0)
    touch(Template(r"tpl1674117523231.png", record_pos=(-0.354, -0.049), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674117543673.png", record_pos=(0.219, 0.131), resolution=(1600, 900)))
    sleep(3.0)
touch(Template(r"tpl1674117562169.png", record_pos=(-0.423, -0.185), resolution=(1600, 900)))
sleep(2.0)
if exists(Template(r"tpl1674194934247.png", threshold=0.9, record_pos=(-0.297, -0.066), resolution=(1600, 900))):
    touch(Template(r"tpl1674194934247.png", threshold=0.9, record_pos=(-0.297, -0.066), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674194967788.png", record_pos=(-0.149, -0.251), resolution=(1600, 900)))
touch(Template(r"tpl1674117616402.png", record_pos=(-0.415, -0.237), resolution=(1600, 900)))
sleep(3.0)

#商城爱心
touch(Template(r"tpl1674192512966.png", record_pos=(0.154, 0.25), resolution=(1600, 900)))
sleep(3.0)
while exists(Template(r"tpl1674192538132.png", threshold=0.85, record_pos=(0.288, -0.127), resolution=(1600, 900))):
    touch(Template(r"tpl1674192551365.png", record_pos=(0.286, -0.125), resolution=(1600, 900)))
    sleep(2.0)
touch(Template(r"tpl1674192565173.png", record_pos=(-0.438, -0.251), resolution=(1600, 900)))
sleep(5.0)

#宿舍爱心
touch(Template(r"tpl1674181374720.png", record_pos=(0.384, -0.058), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674181379426.png", record_pos=(-0.335, -0.236), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674181385943.png", record_pos=(0.285, -0.009), resolution=(1600, 900)))
sleep(8.0)
a=1
while a<300:
    a=a+1
    touch(Template(r"tpl1674181745198.png", threshold=0.8, record_pos=(0.172, -0.044), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674181979454.png", record_pos=(-0.411, -0.247), resolution=(1600, 900)))
sleep(8.0)

#收电池
touch(Template(r"tpl1674182028491.png", record_pos=(0.388, -0.062), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674182034602.png", record_pos=(-0.33, -0.24), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674182058245.png", record_pos=(0.29, -0.01), resolution=(1600, 900)))
sleep(5.0)
if exists(Template(r"tpl1674182074965.png", threshold=0.9, record_pos=(-0.349, -0.006), resolution=(1600, 900))):
    touch(Template(r"tpl1674182074965.png", record_pos=(-0.349, -0.006), resolution=(1600, 900)))
sleep(5.0)
touch(Template(r"tpl1674182094462.png", record_pos=(-0.416, -0.246), resolution=(1600, 900)))
sleep(5.0)

#偷电池
touch(Template(r"tpl1674183270391.png", record_pos=(0.386, -0.062), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674183300664.png", record_pos=(-0.341, -0.24), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674183314543.png", record_pos=(0.284, -0.006), resolution=(1600, 900)))
sleep(5.0)

a=1
while a<30:
    a=a+1
    touch(Template(r"tpl1674183333760.png", record_pos=(-0.424, 0.239), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674183352472.png", record_pos=(0.348, 0.218), resolution=(1600, 900)))
    sleep(5.0)
    if exists(Template(r"tpl1674183393034.png", record_pos=(-0.395, 0.036), resolution=(1600, 900))):
        touch(Template(r"tpl1674183393034.png", record_pos=(-0.395, 0.036), resolution=(1600, 900)))
        sleep(3.0)
        touch(Template(r"tpl1674183420130.png", record_pos=(-0.005, 0.121), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674184600609.png", record_pos=(0.416, 0.233), resolution=(1600, 900)))
    sleep(3.0)
touch(Template(r"tpl1674185264499.png", record_pos=(-0.438, -0.246), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674185286188.png", record_pos=(-0.421, -0.249), resolution=(1600, 900)))
sleep(5.0)

#装备强化
touch(Template(r"tpl1674119018841.png", record_pos=(0.268, -0.059), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674119032181.png", record_pos=(-0.43, -0.098), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674119065460.png", record_pos=(-0.255, 0.034), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674119093124.png", record_pos=(-0.144, 0.157), resolution=(1600, 900)))
sleep(2.0)
touch(Template(r"tpl1674119109799.png", record_pos=(-0.074, -0.119), resolution=(1600, 900)))
sleep(3.0)
if exists(Template(r"tpl1674119128584.png", threshold=0.95, record_pos=(-0.394, -0.185), resolution=(1600, 900))):
    touch(Template(r"tpl1674119128584.png", record_pos=(-0.394, -0.185), resolution=(1600, 900)))
    sleep(2.0)
    touch(Template(r"tpl1674119168783.png", record_pos=(0.419, 0.225), resolution=(1600, 900)))
    sleep(2.0)
    touch(Template(r"tpl1674119191633.png", record_pos=(0.407, 0.214), resolution=(1600, 900)))
else:
    touch(Template(r"tpl1674119344175.png", record_pos=(-0.411, -0.243), resolution=(1600, 900)))
sleep(8.0)
touch(Template(r"tpl1674119344175.png", record_pos=(-0.411, -0.243), resolution=(1600, 900)))
sleep(8.0)

#装备校准
touch(Template(r"tpl1674179691849.png", record_pos=(0.266, -0.065), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674179711758.png", record_pos=(-0.43, -0.03), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674179732617.png", record_pos=(-0.066, -0.106), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674179746099.png", record_pos=(0.273, 0.152), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674179759950.png", record_pos=(0.392, 0.214), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674179780877.png", record_pos=(-0.417, -0.247), resolution=(1600, 900)))
sleep(5.0)

#资源回收
touch(Template(r"tpl1674185740840.png", record_pos=(0.389, -0.062), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674185762523.png", record_pos=(-0.426, 0.042), resolution=(1600, 900)))
sleep(3.0)
b=1
while b<4:
    b=b+1
    touch(Template(r"tpl1674185774224.png", threshold=0.9, record_pos=(-0.241, -0.122), resolution=(1600, 900)))
    sleep(3.0)
    if exists(Template(r"tpl1674185798710.png", threshold=0.95, record_pos=(-0.374, -0.186), resolution=(1600, 900))):
        touch(Template(r"tpl1674185798710.png", threshold=0.95, record_pos=(-0.374, -0.186), resolution=(1600, 900)))
        sleep(3.0)
    elif exists(Template(r"tpl1674187201695.png", threshold=0.95, record_pos=(-0.384, -0.183), resolution=(1600, 900))):
        touch(Template(r"tpl1674187201695.png", threshold=0.95, record_pos=(-0.384, -0.183), resolution=(1600, 900)))
    else:break
    touch(Template(r"tpl1674185808207.png", record_pos=(0.414, 0.224), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674185823447.png", record_pos=(0.379, 0.189), resolution=(1600, 900)))
    sleep(3.0)
    if exists(Template(r"tpl1674186211805.png", record_pos=(0.016, -0.159), resolution=(1600, 900))):
        touch(Template(r"tpl1674186223867.png", record_pos=(0.101, 0.202), resolution=(1600, 900)))
    sleep(5.0)
touch(Template(r"tpl1674187428013.png", record_pos=(-0.411, -0.244), resolution=(1600, 900)))
sleep(5.0)

#前进营地
touch(Template(r"tpl1674182186017.png", record_pos=(0.392, -0.066), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674182191319.png", record_pos=(-0.339, -0.236), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674182285187.png", record_pos=(0.383, -0.101), resolution=(1600, 900)))
sleep(5.0)
touch(Template(r"tpl1674182298740.png", record_pos=(-0.333, -0.242), resolution=(1600, 900)))
sleep(3.0)
touch(Template(r"tpl1674182309693.png", record_pos=(0.051, -0.103), resolution=(1600, 900)))
sleep(5.0)
touch(Template(r"tpl1674182322911.png", record_pos=(-0.341, 0.001), resolution=(1600, 900)))
if exists(Template(r"tpl1674183105110.png", record_pos=(-0.359, -0.203), resolution=(1600, 900))):
    touch(Template(r"tpl1674183105110.png", record_pos=(-0.359, -0.203), resolution=(1600, 900)))
else:
    sleep(3.0)
    touch(Template(r"tpl1674182445763.png", record_pos=(0.402, 0.245), resolution=(1600, 900)))
sleep(3.0)
if exists(Template(r"tpl1674182523581.png", threshold=0.9, record_pos=(0.404, 0.247), resolution=(1600, 900))):
    touch(Template(r"tpl1674182523581.png", threshold=0.9, record_pos=(0.404, 0.247), resolution=(1600, 900)))
else:
    touch(Template(r"tpl1674182469533.png", record_pos=(-0.411, -0.244), resolution=(1600, 900)))

#任务奖励
touch(Template(r"tpl1674197246876.png", record_pos=(-0.051, 0.247), resolution=(1600, 900)))
sleep(5.0)
if exists(Template(r"tpl1674197263174.png", threshold=0.9, record_pos=(0.39, 0.249), resolution=(1600, 900))):
    touch(Template(r"tpl1674197263174.png", record_pos=(0.39, 0.249), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674197274432.png", record_pos=(-0.224, -0.244), resolution=(1600, 900)))
    sleep(3.0)
if exists(Template(r"tpl1674198449087.png", record_pos=(0.347, 0.134), resolution=(1600, 900))):
    touch(Template(r"tpl1674198449087.png", record_pos=(0.347, 0.134), resolution=(1600, 900)))
    sleep(3.0)
    touch(Template(r"tpl1674197484333.png", record_pos=(-0.228, -0.241), resolution=(1600, 900))) 
sleep(3.0)
touch(Template(r"tpl1674197417165.png", record_pos=(-0.414, -0.244), resolution=(1600, 900)))
sleep(5.0)



