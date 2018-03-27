# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:08:02 2018

@author: Administrator
"""

#!/usr/bin/evn python 
#coding:utf-8 
import os

try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
  
file_srx = open("train.set")  #其中包含所有待计算的文件名
line = file_srx.readline()
while line:
  f = line[:-1]    # 除去末尾的换行符
  tree = ET.parse(f)     #打开xml文档 
  root = tree.getroot()         #获得root节点  
  print "*"*10
  filename = root.find('filename').text
  filename = filename[:-4]
  print filename 
  file_object = open(filename + ".txt", 'w') #写文件
 # file_object_log = open(filename + ".log", 'w') #写文件
  flag = False
  
  ########################################
  for size in root.findall('size'): #找到root节点下的size节点 
    width = size.find('width').text   #子节点下节点width的值 
    height = size.find('height').text   #子节点下节点height的值 
    print width, height
  ########################################
  
  for object in root.findall('object'): #找到root节点下的所有object节点 
    name = object.find('name').text   #子节点下节点name的值 
    print name
    bndbox = object.find('bndbox')      #子节点下属性bndbox的值 
    xmin = bndbox.find('xmin').text
    ymin = bndbox.find('ymin').text
    xmax = bndbox.find('xmax').text
    ymax = bndbox.find('ymax').text
    print xmin, ymin, xmax, ymax
    if name == ("Cyclist"):
      file_object.write("Cyclist" + "  " + xmin + " " + ymin + " " + xmax + " " + ymax + " " + "      " + "\n")
      #file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
      flag = True
    if name == ("Car"):
      file_object.write("Car" + "  " + xmin + " " + ymin + " " + xmax + " " + ymax + " " + "      " + "\n")
      #file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
      flag = True
    if name == ("Pedestrian"):
      file_object.write("Pedestrian" + "  " + xmin + " " + ymin + " " + xmax + " " + ymax + " " + "      " + "\n")
      #file_object_log.write(str(float(int(xmax) - int(xmin)) * 1920.0 / float(width)) + " " + str(float(int(ymax) - int(ymin)) * 1080.0 / float(height)) + "\n")
      flag = True
  file_object.close( )
 # file_object_log.close()
  if flag == False:  #如果没有符合条件的信息，则删掉相应的txt文件以及jpg文件
    os.remove(filename + ".txt")
    #os.remove(filename + ".jpg")
    #os.remove(filename + ".log")
  line = file_srx.readline()
