# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import cv2
from random import randint
from PIL import Image
import re
from sklearn.model_selection import train_test_split
import skimage
import pandas as pd

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
    ii = 0
    label=[]
    SizeWidth=[]  

    while ( ii<Num):
      
      x = int(a +(b-a)*np.random.rand(1))
      y = int(a +(b-a)*np.random.rand(1))
      #x=randint(a, b)
      #y=randint(a, b)
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
        
      soma =0
      for kk in range(Width):
        for jj in range(Width):
            soma = soma + img[kk,jj]
      
      valor = soma/(255*Width*Width)
      if (valor> 0.80):
        filtro ='bad'
      else:
        filtro ='ok'
            
      if(filtro =='ok'):
        ii = ii +1
        ww.append(img_1st)
        SizeWidth.append(Width)
        nome = "W=" + str(Width)+" x="+str(x)+" y="+str(y)
        label.append(nome)
      # end of while

    #2nd top: convert image in 28x28 PS: while is conclued before this line
    
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
    


    # 5th top : each image in one line
    
    img28_ravel_all=[]
    for i in range(Num):
      img28_ravel=np.copy(img28_all[i].ravel())
      img28_ravel_all.append(img28_ravel)


    # 6th top

    img28_top=pd.DataFrame(img28_ravel_all)
    #img28_top.insert(0,"Type",TypesTop)
    img28_top.insert(0, "Width", SizeWidth)

    

    return(img28_top)
