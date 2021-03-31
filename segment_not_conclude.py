# -*- coding: utf-8 -*-
"""SEGMENT_NOT_CONCLUDE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ucfilho/marquesgabi_paper_fev_2021/blob/main/Segment_Ajuste_mar_2021/SEGMENT_NOT_CONCLUDE.ipynb
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
from random import randint
from PIL import Image
import re
from sklearn.model_selection import train_test_split
import skimage
import pandas as pd
import mahotas
import mahotas.features.texture as mht
import mahotas.features

# Commented out IPython magic to ensure Python compatibility.
#!git clone https://github.com/ucfilho/marquesgabi_fev_2020 #clonar do Github
#%cd marquesgabi_fev_2020

import Go2BlackWhite
import Go2Mahotas



# Segmentation: start here......


def Segmenta(img):
    #Start to use the big image
    img_ver=img.copy()
    Size=1200 # tamanho da foto
    Sub_Size=int(Size/5) # tamanho do fracionamento
    Row_Crop=1/10 # posicao do corte
    Crop=int(Size*Row_Crop)

    Num=50

    #First top

    a=0
    b=1200
    c=100
    d=200

    ww=[]
    label=[]
    SizeWidth=[]  

    for i in range(Num):
      x=randint(a, b)
      y=randint(a, b)
      Width=randint(c, d)
      img_1st=np.zeros((Width,Width)).astype(np.int64)

      for k in range(Width):
        for j in range(Width):

          size_x=Width+x
          size_y=Width+y

          if(size_x>=Size):
            x=Size-Width

          if(size_y>= Size):
            y=Size-Width

          img_1st[k,j]=np.copy(img[k+y,j+x])

      ww.append(img_1st)
      SizeWidth.append(Width)
      nome = "W=" + str(Width)+" x="+str(x)+" y="+str(y)
      label.append(nome)

    #2nd top
    
    Size=28
    img28_all=[]
    for i in range(Num):
      data=np.array(ww[i])
      img = Image.fromarray(data.astype('uint8'), mode='L')
      img=np.float32(img)
      img28=cv2.resize(img,(Size,Size), interpolation = cv2.INTER_AREA)
      img28_all.append(img28)

    img28_all=np.array(img28_all)

    #3th top


    #4th top
    
    #TypesTop=[]

    #for i in range(Num):
      #Valor='Z'
      #TypesTop.append(Valor)
    


    # 5th top
    
    img28_ravel_all=[]
    for i in range(Num):
      img28_ravel=np.copy(img28_all[i].ravel())
      img28_ravel_all.append(img28_ravel)


    # 6th top

    img28_top=pd.DataFrame(img28_ravel_all)
    #img28_top.insert(0,"Type",TypesTop)
    img28_top.insert(0, "Width", SizeWidth)

    

    return(img28_top)
