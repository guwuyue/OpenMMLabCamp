# 题目：基于RTMPose的耳朵穴位关键点检测

## 背景
    根据中医的“倒置胎儿”学说，耳朵的穴位反映了人体全身脏器的健康，耳穴按摩可以缓解失眠多梦、内分泌失调等疾病。
    耳朵面积较小，但穴位密集，涉及耳舟、耳轮、三角窝、耳甲艇、对耳轮等三维轮廓，普通人难以精准定位耳朵穴位。

## 任务
    1.Labelme标注关键点检测数据集
    2.划分训练集和测试集
    3.Labelme标注转MS COCO格式
    4.使用MMDetection算法库，训练RTMDet耳朵目标检测算法，提交测试集评估指标
    5.使用MMPose算法库，训练RTMPose耳朵关键点检测算法，提交测试集评估指标
    6.用自己耳朵的图像预测，将预测结果发到群里
    7.用自己耳朵的视频预测，将预测结果发到群里
    需提交的测试集评估指标（不能低于baseline指标的50%）

### 目标检测Baseline模型（RTMDet-tiny） 
 1.评估指标

     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.794
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.967
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.958
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.794
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.821
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.831
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.831
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.831
 2.预测图

![avatar](/det_ear_predictor.png)

### 关键点检测Baseline模型（RTMPose-s） 
 1.评估指标

     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.270
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  0.782
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.036
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.270
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.338
     Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  0.833
     Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.143
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.338
 2.预测图
   ![avatar](/ear_predictor2.jpg)