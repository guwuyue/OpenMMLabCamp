import matplotlib.pyplot as plt
import os.path as osp
from PIL import Image

from mmdet.registry import DATASETS, VISUALIZERS
from mmengine.config import Config
from mmengine.registry import init_default_scope

cfg = Config.fromfile('data/balloon_rtmdet.py')
init_default_scope(cfg.get('default_scope', 'mmdet'))

dataset = DATASETS.build(cfg.train_dataloader.dataset)
visualizer = VISUALIZERS.build(cfg.visualizer)
visualizer.dataset_meta = dataset.metainfo

plt.figure(figsize=(16, 5))
# 可视化前8张图片
for i in range(8):
    img_path = dataset[i]['data_samples'].img_path
    image = Image.open(img_path).convert('RGB')
    plt.subplot(2, 4, i + 1)
    plt.imshow(image)
    plt.title(f'{osp.basename(img_path)}')
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()

k = 0
