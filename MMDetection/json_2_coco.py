import json
import os
import re
from pathlib import Path
from collections import defaultdict

# 读取JSON文件
import cv2

data_roots = [
    'data/balloon_dataset/balloon/train/', 'data/balloon_dataset/balloon/val/'
]
for data_root in data_roots:
    with open(f'{data_root}via_region_data.json') as f:
        annotations = json.load(f)

    # 初始化COCO格式字典
    coco_dict = defaultdict(list)
    coco_dict['info'] = {}
    coco_dict['licenses'] = []
    coco_dict['categories'] = []
    coco_dict['images'] = []
    coco_dict['annotations'] = []

    # 添加info信息
    coco_dict['info']['version'] = '1.0'
    coco_dict['info']['description'] = 'Balloon Dataset'
    coco_dict['info']['year'] = 2023
    coco_dict['info']['contributor'] = 'GUWUYUE'
    coco_dict['info']['date_created'] = '2023-6-10'

    # 添加categories信息
    category_id = 1
    category = {
        'id': category_id,
        'name': 'balloon',
        'supercategory': 'object'
    }
    coco_dict['categories'].append(category)

    # 遍历每个图像的注释信息
    annotation_id = 1
    for image_id, image_info in annotations.items():
        # 从image_id中提取出正确的图像ID
        match = re.search(r'(\d+)_.*', image_id)
        if match:
            image_id = match.group(1)
        else:
            continue

        # 获取图像的文件名和大小
        filename = image_info['filename']
        size = image_info['size']
        # 获取图像的height和width
        img = cv2.imread(os.path.join(data_root, filename))
        height, width, _ = img.shape
        # print(filename,height,width)

        # 添加图像信息
        image = {
            'id': int(image_id),
            'file_name': filename,
            'width': width,
            'height': height
        }
        coco_dict['images'].append(image)

        # 获取多边形注释信息
        regions = image_info['regions']
        for region_id, region_info in regions.items():
            # 获取多边形顶点坐标
            x = region_info['shape_attributes']['all_points_x']
            y = region_info['shape_attributes']['all_points_y']
            points = list(zip(x, y))

            # 计算多边形的边界框
            xmin = min(x)
            xmax = max(x)
            ymin = min(y)
            ymax = max(y)
            width = xmax - xmin
            height = ymax - ymin

            # 添加注释信息
            annotation = {
                'id': annotation_id,
                'image_id': int(image_id),
                'category_id': category_id,
                'segmentation': [points],
                'area': width * height,
                'bbox': [xmin, ymin, width, height],
                'iscrowd': 0
            }
            coco_dict['annotations'].append(annotation)
            annotation_id += 1

    # 保存COCO格式文件
    with open(f'{data_root}balloon_{Path(data_root).name}.json', 'w') as f:
        json.dump(coco_dict, f)

    print(f'save {data_root} json success！')
