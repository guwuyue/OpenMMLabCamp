# 题目：MMSeg 语义分割

# 背景
    西瓜瓤、西瓜皮、西瓜籽像素级语义分割

# 任务
    Labelme 标注语义分割数据集（子豪兄已经帮你完成了）
    划分训练集和测试集（子豪兄已经帮你完成了）
    Labelme 标注转 Mask 灰度图格式（子豪兄已经帮你完成了）
    使用 MMSegmentation 算法库，撰写 config 配置文件，训练 PSPNet 语义分割算法
    提交测试集评估指标
    自己拍摄西瓜图片和视频，将预测结果发到群里
    （选做）训练 Segformer 语义分割算法，提交测试集评估指标

# 数据集
![avatar](/MMSegmentation/1.png)
![avatar](/MMSegmentation/2.png)
![avatar](/MMSegmentation/img.png)

# 数据集下载链接
    Labelme标注格式（没有划分训练集和测试集）：
@import "https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20230130-mmseg/dataset/watermelon/Watermelon87_Semantic_Seg_Labelme.zip"
    
    Mask灰度图格式（没有划分训练集和测试集）：
@import "https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20230130-mmseg/dataset/watermelon/Watermelon87_Semantic_Seg_Mask.zip"

# 需提交的测试集评估指标：（不能低于 baseline 指标的 50% ）
    aAcc: 60.6200
    mIoU: 21.1400
    mAcc: 28.4600

## 准备config配置文件
### 1. 定义数据集类
@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMSegmentation/Watermelon87SemanticSegMaskDataset.py"
    
    存储位置 mmseg/datasets
### 2. 注册数据集类
@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMSegmentation/__init__.py"
    
    存储位置 mmseg/datasets
### 3. 定义训练及测试pipeline
@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMSegmentation/Watermelon87_Semantic_Seg_Mask_pipeline.py"
    
    存储位置 configs/_base_/datasets
### 4. config配置文件
@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMSegmentation/pspnet_r50-d8_4xb2-40k_Watermelon87SemanticSegMaskDataset.py"
    
    存储位置 configs/pspnet 


## 训练结果
    06/17 16:31:18 - mmengine - INFO - per class results:
    06/17 16:31:18 - mmengine - INFO - 
    +------------+-------+-------+
    |   Class    |  IoU  |  Acc  |
    +------------+-------+-------+
    |    red     | 81.67 | 87.68 |
    |   green    | 83.94 |  99.0 |
    |   white    | 56.09 | 60.63 |
    | seed-black | 30.64 | 50.04 |
    | seed-white |  40.9 |  49.4 |
    | Unlabeled  |  0.0  |  0.0  |
    +------------+-------+-------+
    06/17 16:31:18 - mmengine - INFO - Iter(val) [11/11]    aAcc: 85.8900  mIoU: 48.8700  mAcc: 57.7900  data_time: 0.0037  time: 0.2214



## 原图
![avatar](/MMSegmentation/test_img.jpg)

## 可视化图示
![avatar](/MMSegmentation/可视化语义分割预测结果.png)
![avatar](/MMSegmentation/可视化预测结果1.png)
![avatar](/MMSegmentation/可视化预测结果2.png)


    