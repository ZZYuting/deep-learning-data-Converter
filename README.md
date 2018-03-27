# deep learning data Converter

## Introduction

useful methods for usual data transform in deep learning

convert from  txt  to json  and xml; from xml to txt.

i am using python2.7 with anaconda in windows.



## txt2xml.py

class_end include the classes that in your images.In my case,they are Pedestrian,Car,Cyclist. 

**image_2**: image that you want to use for train or val
**label_2**: txt doc that you want to convert to xml; such as 00001.txt 
**Annotations**: xml is generated in there; sucah as 00001.xml
**txt2voc2.py should in the same folder with all of above**.
**just run txt2xml.py**

## txt2coco.py

To use it ,make sure that you have folder like that:

data/annos

data/images

data/classes.txt

data/annotations

annos includes txt doc like 00001.txt

images includes image like 00001.png(i am using png ,you can also using jpg )

classes.txt includes classes(in my case, they are Pedestrian,Car,Cyclist )

**i have used  it by  Anaconda Prompt(cmd in Anaconda environment) and use the code : python txt2coco.py e:\bishe\data trains 1000;**

it will produce trains.json in your annotations folder. If you just want to test ,you can use train instead of trains(it will produce train.json,but there is nothing in json file.)

## xml2txt.py

train.set include xml path 

i just using 3 classes Cyclist,Car,Pedestrian.Maybe, you can try more.

**just run xml2txt.py**

## xml2json.py

i didn't test it.If you want to know more about it you can visit https://github.com/fengzhongyouxia/TensorExpand

## kiit2txt.py

kiit data is very useful for car , cyclist, pedestrian detection in Deep Learning.

The data format of kiit is txt with 3d box and something else.In my case, i just want use bbox of kiit,so the code is used to transform that.

kiit annotation is in E:\bishe\train\label_2, when you run kiit2txt.py the new txt will replace kiit annotation with same name.

**just run kiit2txt.py to use it.**



