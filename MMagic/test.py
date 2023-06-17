# 导入工具包
import cv2
import numpy as np
import mmcv
from mmengine import Config
from PIL import Image
from mmagic.registry import MODELS
from mmagic.utils import register_all_modules

register_all_modules()

# 输入Canny边缘图
control_url = r"maopifang_org.jpg"
control_img = mmcv.imread(control_url)
control = cv2.Canny(control_img, 100, 200)
control = control[:, :, None]
control = np.concatenate([control] * 3, axis=2)
control = Image.fromarray(control)
control.save(r"maopifang_canny.jpg")
# 载入ControNet模型
cfg = Config.fromfile('configs/controlnet/controlnet-canny.py')
controlnet = MODELS.build(cfg.model).cuda()

# 咒语Prompt
prompt = 'Room with blue walls and a yellow ceiling.'

# 执行预测
output_dict = controlnet.infer(prompt, control=control)
samples = output_dict['samples']
for idx, sample in enumerate(samples):
    sample.save(f'maopifang_sample_{idx}.png')
controls = output_dict['controls']
for idx, control in enumerate(controls):
    control.save(f'maopifang_control_{idx}.png')