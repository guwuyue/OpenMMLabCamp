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

## 配置文件
    [config](/MMPretrain/config.py)

## 训练日志
    [log](/MMPretrain/20230607_221833.log)   

## 测试结果

    06/07 22:26:17 - mmengine - INFO - Epoch(val) [20][28/28]    accuracy/top1: 93.3559  data_time: 0.0038  time: 0.0657
     

### 预测图

![avatar](/MMPretrain/1.png)

