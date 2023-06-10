# 题目：基于 RTMDet 的气球检测

## 背景
    熟悉目标检测和 MMDetection 常用自定义流程。

## 任务
    基于提供的 notebook，将 cat 数据集换成气球数据集  
    按照视频中 notebook 步骤，可视化数据集和标签  
    使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标  
    用网上下载的任意包括气球的图片进行预测，将预测结果发到群里   
    按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里  
    需提交的测试集评估指标（不能低于baseline指标的50%）  

    目标检测 RTMDet-tiny 模型性能不能 65 mAP   

## 数据集
    
    气球数据集可以直接下载 https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip


### 目标检测Baseline模型（RTMDet-tiny） 

    Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.762
    Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.876
    Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.842
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
    Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.502
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.881
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.244
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.782
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.826
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.692
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.917

### json转coco

@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMDetection/json_2_coco.py"

### 可视化数据集

    MMDetection/vis.py
    

### 预测图 可视化

![avatar](/MMDetection/vis.png)
    