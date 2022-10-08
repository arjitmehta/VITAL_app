#!/usr/bin/env python
# coding: utf-8

# <center><span style="font-family:Times New Roman; font-size:5em;">VITAL</span> 
# <center><span style="font-family:Product Sans; font-size:2em;">Virtually Intelligent Technology for an Active Lifestyle</span>

# </br>
# <center><img src="logo.png" alt="Drawing" style="width: 300px;"/></center>
# </br>

# 
# #### It is an application incorporated with AI technology which not just helps the user to do the exercise or yoga but ensures that the user does it correctly. It comes with a posture correction and guides the user when they are doing the asana/exercise wrongly. VITAL also comes with a repetition counter. 
# 
# #### In this file, the backend python source code is present where all the necessary functions are created along with importation of the required modules such as 
# 'Mediapipe' ,'PoseModule' and 'OpenCV'.
# 
# >This file covers three yoga plans
# >* Beginner
# >* Intermediate
# >* Advance  
# > Along with Weightlifting exercise and Calesthenics
# </br>

# <center><span style="font-family:Product Sans; font-size:1em;">Copyright © 2021 Anirudh Roy, Arjit Mehta, Hitesh Beniwal, Palakshee, Saksham Jain</span></center>
# <center><span style="font-family:Product Sans; font-size:1em;">All Rights Reserved.</span>

# In[ ]:


import cv2
import numpy as np
import time
import PoseModule as pm
from flask import Flask,render_template,Response
app=Flask(__name__)
class VITAL():
    def yoga_beg_aasana0(img,detector):
        angle = detector.findAngle(img, 11, 13, 15, False)
        angle1 = detector.findAngle(img, 27, 25, 23, False)
        if angle <168 or angle >170:            
            angle = detector.findAngle(img, 11, 13, 15)
        if angle1 <75 or angle1 >80:
            angle1 = detector.findAngle(img, 27, 25, 23)
    def yoga_beg_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        #feet ka KARNA POSSIBLE NAHI HO RAHAA
        angle4 = detector.findAngle(img, 31, 27, 25, False)
        if angle1 <160 or angle1>184:            
            angle = detector.findAngle(img, 15, 13, 11)
        if angle2 <170 or angle2 >182:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <154 or angle3 >178:
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <154 or angle4 >178:
            angle4 = detector.findAngle(img, 31, 27, 25)
        
    def yoga_beg_aasana2(img,detector):
        angle1 = detector.findAngle(img, 25, 23, 11, False)
        angle2 = detector.findAngle(img, 15, 13, 11, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        if angle1 <70 or angle1>82:            
            angle1 = detector.findAngle(img, 25, 23, 11)
        if angle2 <162 or angle2>172:            
            angle2 = detector.findAngle(img, 15, 13, 11)
        if angle3 <172 or angle3 >200:
            angle3 = detector.findAngle(img, 27, 25, 23)

    def yoga_beg_aasana3(img,detector):
                
        angle1 = detector.findAngle(img, 11, 23, 25, False)
        angle2 = detector.findAngle(img, 27, 25, 23, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <65 or angle1 >135:            
            angle1 = detector.findAngle(img, 11, 23, 25)
        if angle2 <15 or angle2 >45:
            angle2 = detector.findAngle(img, 27, 25, 23)
        if angle3 <155 or angle3>185:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <160 or angle4>184:
            angle4 = detector.findAngle(img, 23, 11, 13)
     
        
    def yoga_beg_aasana4(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 24, 26, 28, False)
        angle3 = detector.findAngle(img, 24, 12, 14, False)
        if angle1 <170 or angle1>180:            
            angle = detector.findAngle(img, 16, 14, 12)
        if angle2 <172 or angle2 >190:
            angle2 = detector.findAngle(img, 24, 26, 28)
        if angle3 <5 or angle3>30:            
            angle3 = detector.findAngle(img, 24, 12, 14)
        pass
    def yoga_beg_aasana5(img,detector):
        #angle1 = detector.findAngle(img, 12, 14, 16, False)
        #angle2 = detector.findAngle(img, 26, 24, 12, False)
        angle3 = detector.findAngle(img, 28, 26, 24, False)
        angle4 = detector.findAngle(img, 27, 25, 23, False)
        angle5 = detector.findAngle(img, 11, 13, 15, False)
        #if angle1 <159 or angle1>163:            
            #angle1 = detector.findAngle(img,  12, 14, 16)
        if angle5 <160 or angle5 >200:
            angle5 = detector.findAngle(img, 11, 13, 15)
        if angle3 <220 or angle3>260:            
            angle3 = detector.findAngle(img, 28, 26, 24)
        if angle4 <180 or angle4>210:
            angle4 = detector.findAngle(img, 27, 25, 23)
        
        
    def yoga_beg_aasana6(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        if angle1 <170 or angle1>190:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        
        if angle2 <160 or angle2>182:            
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <90 or angle3>120:
            angle3 = detector.findAngle(img, 24, 26, 28)
        pass
    def yoga_beg_aasana7(img,detector):
        #9/10/21
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <170 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <100 or angle2 >120:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <85 or angle3>108:            
            angle3 = detector.findAngle(img, 25, 23, 11)
        if angle4 <140 or angle4>180:
            angle4 = detector.findAngle(img, 23, 11, 13)
            
    def yoga_beg_aasana8(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        if angle1 <155 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <160 or angle2 >176:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <130 or angle3>150:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        pass
    def yoga_beg_aasana9(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <160 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <160 or angle2 >180:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <160 or angle3>180:            
            angle3 = detector.findAngle(img, 25, 23, 11)
        if angle4 <40 or angle4>70:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_beg_aasana10(img,detector):
        angle1 = detector.findAngle(img, 11, 13, 15, False)
        angle2 = detector.findAngle(img, 16, 14, 12, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        angle4 = detector.findAngle(img, 24, 26, 28, False)
        angle5 = detector.findAngle(img, 13, 11, 23, False)
        angle6 = detector.findAngle(img, 24, 12, 14, False)
        
        if angle1 <90 or angle1>115:            
            angle1 = detector.findAngle(img,  11, 13, 15)
        if angle2 <90 or angle2 >115:
            angle2 = detector.findAngle(img,  16, 14, 12)
        if angle3 <120 or angle3>150:            
            angle3 = detector.findAngle(img, 27, 25, 23)
        if angle4 <120 or angle4>150:
            angle4 = detector.findAngle(img, 24, 26, 28)
        if angle5 <90 or angle5>115:            
            angle5 = detector.findAngle(img, 13, 11, 23)
        if angle6 <90 or angle6>115:
            angle6 = detector.findAngle(img, 24, 12, 14)
            
            
   #******************************************************************************************************         
    def yoga_inter_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11)
        angle2 = detector.findAngle(img, 12, 14, 16)
        if angle1 <35 or angle1>80:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <35 or angle2 >80:
            angle2 = detector.findAngle(img,12, 14, 16)
            
    def yoga_inter_aasana2(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 25, 23, 11, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <162 or angle1>180:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <82 or angle2 >92:
            angle2 = detector.findAngle(img, 25, 23, 11)
        if angle3 <160 or angle3>175:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <48 or angle4>58:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_inter_aasana3(img,detector):
        angle1 = detector.findAngle(img, 24, 12, 14, False)
        angle2 = detector.findAngle(img, 16, 14, 12, False)
        angle3 = detector.findAngle(img, 27, 25, 23, False)
        angle4 = detector.findAngle(img, 24, 26, 32, False)
        angle5 = detector.findAngle(img, 26, 24, 12, False)
        if angle1 <80 or angle1>110:            
            angle1 = detector.findAngle(img,  24, 12, 14)
        if angle2 <160 or angle2 >191:
            angle2 = detector.findAngle(img,  16, 14, 12)
        if angle3 <160 or angle3>191:            
            angle3 = detector.findAngle(img, 27, 25, 23)
        if angle4 <160 or angle4>191:
            angle4 = detector.findAngle(img, 24, 26, 28)
        if angle5 <35 or angle5>60:            
            angle5 = detector.findAngle(img, 26, 24, 12)
        
        
    def yoga_inter_aasana4(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 25, 23, 11, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 31, 27, 25, False)
        angle5 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <102 or angle1>106:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <174 or angle2 >178:
            angle2 = detector.findAngle(img, 25, 23, 11)
        if angle3 <169 or angle3>173:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <105 or angle4>109:
            angle4 = detector.findAngle(img, 31, 27, 25)
        if angle5 <5 or angle5>15:            
            angle5 = detector.findAngle(img, 23, 11, 13)
        pass
    def yoga_inter_aasana5(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 24, 12, 14, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 26, 28, False)
        
        if angle1 <160 or angle1>181:            
            angle1 = detector.findAngle(img,  16, 14, 12)
        if angle2 <40 or angle2 >70:
            angle2 = detector.findAngle(img,  24, 12, 14)
        if angle3 <160 or angle3>181:            
            angle3 = detector.findAngle(img, 26, 24, 12)
        if angle4 <160 or angle4>181:
            angle4 = detector.findAngle(img, 24, 26, 28)
            
            
    def yoga_inter_aasana6(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 26, 24, 12, False)
        if angle1 <164 or angle1>168:            
            angle1 = detector.findAngle(img,  15, 13, 11)
        if angle2 <140 or angle2 >160:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <160 or angle3>180:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <70 or angle4>90:
            angle4 = detector.findAngle(img, 26, 24, 12)
            
            
        
    def yoga_inter_aasana7(img,detector):
        angle1 = detector.findAngle(img, 27, 25, 23)
        angle2 = detector.findAngle(img, 24, 26, 28)
        if angle1 <15 or angle1>25:
            angle1 = detector.findAngle(img,  23, 25, 27)
        if angle2 <15 or angle2 >25:
            angle2 = detector.findAngle(img, 28, 26, 24)
        pass
    def yoga_inter_aasana8(img,detector):
        
        angle1 = detector.findAngle(img, 24, 26, 28, False)
        angle2 = detector.findAngle(img, 11, 13, 15, False)
        angle3 = detector.findAngle(img, 13, 11, 23, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        
       
        if angle1 <170 or angle1 >180:
            angle1 = detector.findAngle(img,  24, 26, 28)
        if angle2 <165 or angle2>185:            
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <100 or angle3>130:            
            angle3 = detector.findAngle(img, 13, 11, 23)
        if angle4 <45 or angle4>75:
            angle4 = detector.findAngle(img, 24, 12, 14)
        
       
    def yoga_inter_aasana9(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 24, 26, 28, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        angle5 = detector.findAngle(img, 25, 23, 11, False)
       
        if angle1 <166 or angle1>170:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <166 or angle2 >170:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <168 or angle3>172:            
            angle3 = detector.findAngle(img, 24, 26, 28)
        if angle4 <166 or angle4>170:
            angle4 = detector.findAngle(img, 23, 11, 13)
        if angle5 <88 or angle5>92:            
            angle5 = detector.findAngle(img, 25, 23, 11)
        
    
    def yoga_inter_aasana10(img,detector):
        angle1 = detector.findAngle(img, 12, 14, 16, False)
        angle2 = detector.findAngle(img, 24, 12, 14, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 28, 26, 24, False)
        if angle1 <165 or angle1>187:            
            angle1 = detector.findAngle(img, 12, 14, 16)
        if angle2 <22 or angle2 >45:
            angle2 = detector.findAngle(img, 24, 12, 14)
        if angle3 <165 or angle3>187:            
            angle3 = detector.findAngle(img,26, 24, 12)
        if angle4 <60 or angle4>80:
            angle4 = detector.findAngle(img, 28, 26, 24)
            
   #****************************************************************************************************** 
        
    def yoga_adv_aasana1(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <57 or angle1>63:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <145 or angle2 >156:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <142 or angle3>158:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <78 or angle4>98:
            angle4 = detector.findAngle(img, 13, 11, 23)
        
    def yoga_adv_aasana2(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <57 or angle1>63:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <145 or angle2 >156:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <142 or angle3>158:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <78 or angle4>98:
            angle4 = detector.findAngle(img, 13, 11, 23)
    
    def yoga_adv_aasana3(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 25, 23, 11, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <133 or angle1>143:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <162 or angle2 >180:
            angle2 = detector.findAngle(img,  23, 25, 27)
        if angle3 <7 or angle3>30:            
            angle3 = detector.findAngle(img,25, 23, 11)
        if angle4 <120 or angle4>128:
            angle4 = detector.findAngle(img, 23, 11, 13)
            
    def yoga_adv_aasana4(img,detector):
        angle1 = detector.findAngle(img, 11, 13, 15, False)
        angle2 = detector.findAngle(img, 27, 25, 23, False)
        angle3 = detector.findAngle(img, 12, 24, 26, False)
        angle4 = detector.findAngle(img, 14, 12, 24, False)
        if angle1 <174 or angle1>182:            
            angle1 = detector.findAngle(img, 11, 13, 15)
        if angle2 <118 or angle2 >126:
            angle2 = detector.findAngle(img,  27, 25, 23)
        if angle3 <72 or angle3>92:            
            angle3 = detector.findAngle(img, 12, 24, 26)
        if angle4 <32 or angle4>40:
            angle4 = detector.findAngle(img, 14, 12, 24)
        
    def yoga_adv_aasana5(img,detector):
        angle1 = detector.findAngle(img, 12, 14, 16, False)
        angle2 = detector.findAngle(img, 28, 26, 24, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        angle5 = detector.findAngle(img, 14, 18, 26, False)
        if angle1 <163 or angle1>171:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <163 or angle2 >171:
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <155 or angle3>167:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <52 or angle4>72:
            angle4 = detector.findAngle(img, 11, 23, 25)
        if angle5 <95 or angle5>107:
            angle5 = detector.findAngle(img, 13, 11, 23)
        
        
        
        
    def yoga_adv_aasana6(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 11, 13, 15, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 11, 23, 25, False)
        angle5 = detector.findAngle(img, 13, 11, 23, False)
        if angle1 <163 or angle1>171:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <163 or angle2 >171:
            angle2 = detector.findAngle(img, 11, 13, 15)
        if angle3 <155 or angle3>167:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <52 or angle4>72:
            angle4 = detector.findAngle(img, 11, 23, 25)
        if angle5 <95 or angle5>107:
            angle5 = detector.findAngle(img, 13, 11, 23)
        
    def yoga_adv_aasana7(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <113 or angle1>133:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <164 or angle2 >184:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <170 or angle3>190:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <5 or angle4>25:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
        
    def yoga_adv_aasana8(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 23, 25, 27, False)
        angle3 = detector.findAngle(img, 11, 23, 25, False)
        angle4 = detector.findAngle(img, 23, 11, 13, False)
        if angle1 <37 or angle1>67:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <166 or angle2 >190:
            angle2 = detector.findAngle(img, 23, 25, 27)
        if angle3 <162 or angle3>186:            
            angle3 = detector.findAngle(img, 11, 23, 25)
        if angle4 <108 or angle4>132:
            angle4 = detector.findAngle(img, 23, 11, 13)
        
    def yoga_adv_aasana9(img,detector):
        angle1 = detector.findAngle(img, 16, 14, 12, False)
        angle2 = detector.findAngle(img, 28, 26, 24, False)
        angle3 = detector.findAngle(img, 26, 24, 12, False)
        angle4 = detector.findAngle(img, 24, 12, 14, False)
        angle5 = detector.findAngle(img, 27, 25, 23, False)
        if angle1 <142 or angle1>158:            
            angle1 = detector.findAngle(img, 16, 14, 12)
        if angle2 <154 or angle2 >170:
            angle2 = detector.findAngle(img, 28, 26, 24)
        if angle3 <161 or angle3>181:            
            angle3 = detector.findAngle(img, 26, 24, 12)
        if angle4 <56 or angle4>76:
            angle4 = detector.findAngle(img, 24, 12, 14)
        if angle5 <36 or angle5>50:
            angle5 = detector.findAngle(img, 27, 25, 23)
        
        
    def yoga_adv_aasana10(img,detector):
        angle1 = detector.findAngle(img, 15, 13, 11, False)
        angle2 = detector.findAngle(img, 24, 26, 28, False)
        angle3 = detector.findAngle(img, 23, 25, 27, False)
        angle4 = detector.findAngle(img, 11, 23, 25, False)
        
        if angle1 <61 or angle1>91:            
            angle1 = detector.findAngle(img, 15, 13, 11)
        if angle2 <133 or angle2 >167:
            angle2 = detector.findAngle(img, 24, 26, 28)
        if angle3 <73 or angle3>113:            
            angle3 = detector.findAngle(img, 23, 25, 27)
        if angle4 <70 or angle4>100:
            angle4 = detector.findAngle(img, 11, 23, 25)
            
         
   #****************************************************************************************************** 

    
    def lifting_curls_biceps(img,detector):
        x,y,z=15,13,11
        #left arm
        angle = detector.findAngle(img, x, y, z)
        #right arm
        #angle = detector.findAngle(img, 12, 14, 16)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (150, 50), (0, 100))
        
        
        return per
    def lifting_curls_biceps(img,detector):
        x,y,z=15,13,11
        #left arm
        angle = detector.findAngle(img, x, y, z)
        #right arm
        #angle = detector.findAngle(img, 12, 14, 16)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (150, 50), (0, 100))
        return per
    def lifting_floor_press(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_bentover_dumbbell(img,detector):
        x,y,z=15,13,11
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (150, 75), (0, 100))
        return per
        
    def lifting_forearms(img,detector):  
        #x,y,z=15,13,11
        #left arm
        #angle = detector.findAngle(img, x, y, z)
        #right arm
        angle = detector.findAngle(img, 22, 16, 14)
        #per = np.interp(angle, (210, 310), (0, 100))
        per = np.interp(angle, (192, 184), (0, 100))
        return per
        
    def lifting_dumbell_squats(img,detector):
        x,y,z=23,25,27
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (182, 300), (0, 100))
        return per
        
    def lifting_shoulder_press(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_tricep_overhead_left(img,detector): 
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex8():
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex9():
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
    
    def lifting_ex10():
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (165, 100), (0, 100))
        return per
             
   #****************************************************************************************************** 
    
    def calisthenics_pushup(img,detector):
        x,y,z=12,14,16
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (160,100 ), (0, 100))
        return per
    def calisthenics_pullup(img,detector):
        x,y,z=14,12,24
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (150, 60), (0, 100))
        return per
    def calisthenics_squats(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (230, 250), (0, 100))
        return per
    def calisthenics_benchdips(img,detector):
        x,y,z=24,12,14
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (30, 90), (0, 100))
        return per
    def calisthenics_crunches(img,detector):
        x,y,z=25,23,11
        angle = detector.findAngle(img, x, y, z)
        per = np.interp(angle, (120, 40), (0, 100))
        return per
    
             
   #****************************************************************************************************** 
    
    
def main(): 
    health = VITAL()
    a="inter_9"
    b=0
    ex=0
    cap = cv2.VideoCapture(0)
    

    detector = pm.poseDetector()
    count = 0
    dir = 0
    per=0
    pTime = 0
    while True:

        success, img = cap.read()

        #img = cv2.imread("Yoga_test_images/Beginner/beg_6.png")
        #img = cv2.resize(img, (720, 720))
        
        img = detector.findPose(img,False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
           
            
            if a== 'ex_1' :
                per = VITAL.lifting_curls_biceps(img,detector)
                ex=1
            if a== 'ex_2' :
                per = VITAL.lifting_floor_press(img,detector) #make new conditions for respective functions
                ex=1
            if a== 'ex_3' :
                per = VITAL.lifting_bentover_dumbbell(img,detector)
                ex=1
            if a== 'ex_4' :
                per = VITAL.lifting_forearms(img,detector)
                ex=1
            if a== 'ex_5' :
                per = VITAL.lifting_dumbell_squats(img,detector)
                ex=1
            if a== 'ex_6' :
                per = VITAL.lifting_shoulder_press(img,detector)
                ex=1
            if a =='beg_1':
                VITAL.yoga_beg_aasana1(img,detector)
            if a =='beg_2':
                VITAL.yoga_beg_aasana2(img,detector)
            if a =='beg_3':
                VITAL.yoga_beg_aasana3(img,detector)
            if a =='beg_4':
                VITAL.yoga_beg_aasana4(img,detector)
            if a =='beg_5':
                VITAL.yoga_beg_aasana5(img,detector)
            if a =='beg_6':
                VITAL.yoga_beg_aasana6(img,detector)
            if a =='beg_7':
                VITAL.yoga_beg_aasana7(img,detector)
            if a =='beg_8':
                VITAL.yoga_beg_aasana8(img,detector)
            if a =='beg_9':
                VITAL.yoga_beg_aasana9(img,detector)
            if a =='beg_10':
                VITAL.yoga_beg_aasana10(img,detector)
            if a =='inter_1':
                VITAL.yoga_inter_aasana1(img,detector)
            if a =='inter_2':
                VITAL.yoga_inter_aasana2 (img,detector)
            if a =='inter_3':
                VITAL.yoga_inter_aasana3(img,detector)
            if a =='inter_4':
                VITAL.yoga_inter_aasana4(img,detector)
            if a =='inter_5':
                VITAL.yoga_inter_aasana5(img,detector)
            if a =='inter_6':
                VITAL.yoga_inter_aasana6(img,detector)
            if a =='inter_7':
                VITAL.yoga_inter_aasana7(img,detector)
            if a =='inter_8':
                VITAL.yoga_inter_aasana8(img,detector)
            if a =='inter_9':
                VITAL.yoga_inter_aasana9(img,detector)
            if a =='inter_10':
                VITAL.yoga_inter_aasana10(img,detector)
            if a =='adv_1':
                VITAL.yoga_adv_aasana1(img,detector)
            if a =='adv_2':
                VITAL.yoga_adv_aasana2(img,detector)
            if a =='adv_3':
                VITAL.yoga_adv_aasana3(img,detector)
            if a =='adv_4':
                VITAL.yoga_adv_aasana4(img,detector)
            if a =='adv_5':
                VITAL.yoga_adv_aasana5(img,detector)
            if a =='adv_6':
                VITAL.yoga_adv_aasana6(img,detector)
            if a =='adv_7':
                VITAL.yoga_adv_aasana7(img,detector)
            if a =='adv_8':
                VITAL.yoga_adv_aasana8(img,detector)
            if a =='adv_9':
                VITAL.yoga_adv_aasana9(img,detector)
            if a =='adv_10':
                VITAL.yoga_adv_aasana10(img,detector)
            
                
                #print(angle, per)
                #Counting Reps
            if ex==1:
                color = (255, 0, 255)
                if per == 100:
                    color = (0, 255, 0)
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if per == 0:
                    color = (0, 255, 0)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                #cv2.putText(img, "maintain", (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,(0, 0, 255), 5)
                #print(count)
                # Draw Rep Count
                    cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                                (255, 0, 0), 25)
#         #FPS
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
#                    (0, 255, 0), 5)

 #****************************************************************************************************** 

#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) == 13: #13 is the Enter Key
#             break
    
#     cap.release()
#     cv2.destroyAllWindows() 
# if __name__ == "__main__":
#     main()

 #****************************************************************************************************** 
    
    
    
        ret,buffer=cv2.imencode('.jpg',img)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(main(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    # from werkzeug.serving import run_simple
    # run_simple('localhost', 9000, app)
    app.run(debug=True)

