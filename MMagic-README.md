# 题目：ControlNet 的 N 种玩法

## 背景
    使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类  

## 任务
    假设你是某装修公司的设计师，客户发了你毛坯房的照片，想让你设计未来装修好的效果图。
    先将毛坯房照片，用 OpenCV 转为 Canny 边缘检测图，然后输入 ControlNet，用 Prompt 咒语控制生成效果。
    将毛坯房图、Canny 边缘检测图、咒语 Prompt、ControlNet 生成图，做成一页海报，发到群里。

## 代码文件
[config](/MMagic/test.py)

## 毛坯房图 原图
![avatar](/MMagic/maopifang_org.jpg) 

## 毛坯房图 Canny边缘检测图
![avatar](/MMagic/maopifang_canny.jpg) 

## 咒语 Prompt
    
    prompt = 'Room with blue walls and a yellow ceiling.'
    
### 生成图

![avatar](/MMagic/maopifang_control_0.png)
![avatar](/MMagic/maopifang_sample_0.png)

