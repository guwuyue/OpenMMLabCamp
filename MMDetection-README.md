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

    2023/06/10 17:34:19 - mmengine - INFO - Evaluating bbox...
    2023/06/10 17:34:19 - mmengine - INFO - bbox_mAP_copypaste: 0.764 0.863 0.853 0.000 0.365 0.899
    2023/06/10 17:34:19 - mmengine - INFO - Epoch(val) [200][13/13]    coco/bbox_mAP: 0.7640  coco/bbox_mAP_50: 0.8630  coco/bbox_mAP_75: 0.8530  coco/bbox_mAP_s: 0.0000  coco/bbox_mAP_m: 0.3650  coco/bbox_mAP_l: 0.8990  data_time: 0.0026  time: 0.0294

### json转coco
    
### 预测图

![avatar](/MMDetection/vis_show.png)

