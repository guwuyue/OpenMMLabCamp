# 题目：基于 RTMDet 的气球检测

# 背景
    熟悉目标检测和 MMDetection 常用自定义流程。

# 任务
    基于提供的 notebook，将 cat 数据集换成气球数据集  
    按照视频中 notebook 步骤，可视化数据集和标签  
    使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标  
    用网上下载的任意包括气球的图片进行预测，将预测结果发到群里   
    按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里  
    需提交的测试集评估指标（不能低于baseline指标的50%）  

    目标检测 RTMDet-tiny 模型性能不能 65 mAP   

# 数据集
    
    气球数据集可以直接下载 https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip


# 可视化数据集
## 代码
    
    import os
    import matplotlib.pyplot as plt
    from PIL import Image
    
    # 数据集可视化
    plt.figure(figsize=(16, 5))
    
    root_path = r'data/balloon_dataset/balloon/val/'
    image_paths = [filename for filename in os.listdir(root_path)][:8]
    
    for idx, filename in enumerate(image_paths):
        name = os.path.splitext(filename)[0]
        image = Image.open(root_path + filename).convert('RGB')
    
        plt.subplot(2, 4, idx + 1)
        plt.imshow(image)
        plt.title(f"{filename}")
        plt.xticks([])
        plt.yticks([])
    
    plt.tight_layout()
    plt.show()

## 可视化图示
![avatar](/MMDetection/vis1.png)
    
# json转coco

@import "https://github.com/guwuyue/OpenMMLabCamp/blob/master/MMDetection/json_2_coco.py"

# 训练前可视化
## coco可视化 代码
    from pycocotools.coco import COCO
    import numpy as np
    import os.path as osp
    from matplotlib.collections import PatchCollection
    from matplotlib.patches import Polygon
    import matplotlib.pyplot as plt
    from PIL import Image
    
    def apply_exif_orientation(image):
        _EXIF_ORIENT = 274
        if not hasattr(image, 'getexif'):
            return image
        try:
            exif = image.getexif()
        except Exception:
            exif = None
    
        if exif is None:
            return image
    
        orientation = exif.get(_EXIF_ORIENT)
        method = {
            2: Image.FLIP_LEFT_RIGHT,
            3: Image.ROTATE_180,
            4: Image.FLIP_TOP_BOTTOM,
            5: Image.TRANSPOSE,
            6: Image.ROTATE_270,
            7: Image.TRANSVERSE,
            8: Image.ROTATE_90,
        }.get(orientation)
        if method is not None:
            return image.transpose(method)
        return image
    
    
    def show_bbox_only(coco, anns, show_label_bbox=True, is_filling=True):
        """Show bounding box of annotations Only."""
        if len(anns) == 0:
            return
        ax = plt.gca()
        ax.set_autoscale_on(False)
        image2color = dict()
        for cat in coco.getCatIds():
            image2color[cat] = (np.random.random((1, 3)) * 0.7 + 0.3).tolist()[0]
    
        polygons = []
        colors = []
        for ann in anns:
            color = image2color[ann['category_id']]
            bbox_x, bbox_y, bbox_w, bbox_h = ann['bbox']
            poly = [
                [bbox_x, bbox_y], [bbox_x, bbox_y + bbox_h],
                [bbox_x + bbox_w, bbox_y + bbox_h], [bbox_x + bbox_w, bbox_y]
            ]
            polygons.append(Polygon(np.array(poly).reshape((4, 2))))
            colors.append(color)
    
            if show_label_bbox:
                label_bbox = dict(facecolor=color)
            else:
                label_bbox = None
    
            ax.text(
                bbox_x,
                bbox_y,
                '%s' % (coco.loadCats(ann['category_id'])[0]['name']),
                color='white',
                bbox=label_bbox)
        if is_filling:
            p = PatchCollection(
                polygons, facecolor=colors, linewidths=0, alpha=0.4)
            ax.add_collection(p)
        p = PatchCollection(
            polygons, facecolor='none', edgecolors=colors, linewidths=2)
        ax.add_collection(p)
    
    
    coco = COCO('data/balloon_dataset/balloon/train/balloon_train.json')
    image_ids = coco.getImgIds()
    print(image_ids)
    np.random.shuffle(image_ids)
    
    plt.figure(figsize=(16, 5))
    
    # 只可视化 8 张图片
    for i in range(8):
        image_data = coco.loadImgs(image_ids[i])[0]
        image_path = osp.join(
            'data/balloon_dataset/balloon/train/', image_data['file_name'])
        title = image_path.split('/')[-1]
        annotation_ids = coco.getAnnIds(
            imgIds=image_data['id'], catIds=[], iscrowd=0)
        annotations = coco.loadAnns(annotation_ids)
    
        ax = plt.subplot(2, 4, i + 1)
        image = Image.open(image_path).convert("RGB")
    
        # 这行代码很关键，否则可能图片和标签对不上
        image = apply_exif_orientation(image)
    
        ax.imshow(image)
    
        show_bbox_only(coco, annotations)
    
        plt.title(f"{title}")
        plt.xticks([])
        plt.yticks([])
    
    plt.tight_layout()
    plt.show()
## mmdet可视化 代码
    import matplotlib.pyplot as plt
    import os.path as osp
    from mmdet.registry import DATASETS, VISUALIZERS
    from mmengine.config import Config
    from mmengine.registry import init_default_scope
    cfg = Config.fromfile('data/balloon_rtmdet.py')
    
    init_default_scope(cfg.get('default_scope', 'mmdet'))
    dataset = DATASETS.build(cfg.train_dataloader.dataset)
    visualizer = VISUALIZERS.build(cfg.visualizer)
    visualizer.dataset_meta = dataset.metainfo
    plt.figure(figsize=(16, 5))
    # 只可视化前 8 张图片
    for i in range(8):
        item = dataset[i]
        img = item['inputs'].permute(1, 2, 0).numpy()
        data_sample = item['data_samples'].numpy()
        gt_instances = data_sample.gt_instances
        img_path = osp.basename(item['data_samples'].img_path)
        gt_bboxes = gt_instances.get('bboxes', None)
        gt_instances.bboxes = gt_bboxes.tensor
        data_sample.gt_instances = gt_instances
        visualizer.add_datasample(
            osp.basename(img_path),
            img,
            data_sample,
            draw_pred=False,
            show=False)
        drawed_image = visualizer.get_image()
        plt.subplot(2, 4, i + 1)
        plt.imshow(drawed_image[..., [2, 1, 0]])
        plt.title(f"{osp.basename(img_path)}")
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout()
    plt.show()
## 可视化结果
![avatar](/MMDetection/vis.png)

    
# 配置文件
    [config](/MMDetection/balloon_rtmdet.py)


# 目标检测Baseline模型（RTMDet-tiny） 

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

# 模型推理
    python tools/test.py data/balloon_rtmdet.py work_dirs/balloon_rtmdet/best_coco_bbox_mAP_epoch_190.pth --show-dir results

## 可视化结果
![avatar](/MMDetection/vis2.png)


# 可视化
    
    git clone -b tutorials https://github.com/open-mmlab/mmyolo.git 

    python demo/featmap_vis_demo.py  resized_image.jpg ../mmdetection/data/balloon_rtmdet.py \
          ../mmdetection/work_dirs/balloon_rtmdet/best_coco_bbox_mAP_epoch_190.pth  \
          --target-layers backbone  \
          --channel-reduction squeeze_mean
    Image.open('output/resized_image.jpg')   
    
    python demo/boxam_vis_demo.py resized_image.jpg ../mmdetection/data/balloon_rtmdet.py \
      ../mmdetection/work_dirs/balloon_rtmdet/best_coco_bbox_mAP_epoch_190.pth  \
      --target-layer neck.out_convs[1]
    