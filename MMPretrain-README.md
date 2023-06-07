# 题目：基于 ResNet50 的水果分类

## 背景
    使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类  

## 任务
    划分训练集和验证集；  
    按照 MMPreTrain CustomDataset 格式组织训练集和验证集；  
    使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型； 
    在水果数据集上进行微调训练；  
    使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类。
    需提交的验证集评估指标（不能低于 60%）
    ResNet-50

## 作业数据集下载 
    链接：(https://pan.baidu.com/s/1YgoU1M_v7ridtXB9xxbA1Q)  
    [百度网盘地址](https://pan.baidu.com/s/1YgoU1M_v7ridtXB9xxbA1Q?pwd=52m9)    
    提取码：52m9  

目标检测Baseline模型（RTMDet-tiny） 

    Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.821
    Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.967
    Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.967
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
    Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.821
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.845
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.845
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.845
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.845
    

### 关键点检测Baseline模型（RTMPose-s） 


     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.743
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.930
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.743
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.783
     Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
     Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.952
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.783

     
### 预测视频

[https://github.com/guwuyue/OpenMMLabCamp/blob/master/video.mp4](/https://github.com/guwuyue/OpenMMLabCamp/blob/master/video.mp4)

### 预测图

![avatar](/MMPose/opencv1.png)

![avatar](/MMPose/visualizer.jpg)

