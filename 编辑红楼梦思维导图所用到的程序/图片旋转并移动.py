import os
import time
from PIL import Image

# 原始图片所在目录
src_dir = 'input'
# 旋转后图片存放目录
dst_dir = 'output'

# 全局计数器
count = 46
while True:
    for filename in os.listdir(src_dir):
        # 检查文件是否为图片（可根据需要更改）
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # 打开图片并旋转90度
            with Image.open(os.path.join(src_dir, filename)) as im:
                im = im.rotate(90, expand=True)
                # 生成新文件名
                new_filename = f'{count}.jpg'
                # 保存旋转后的图片到目标目录中，并按顺序命名
                im.save(os.path.join(dst_dir, new_filename))
                print('saved,' , count)
                count += 1
            # 删除原始文件
            os.remove(os.path.join(src_dir, filename))
    # 暂停后再次执行循环
    time.sleep(1)