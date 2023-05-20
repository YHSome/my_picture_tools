import os
from PIL import Image

# 指定要旋转的文件夹路径(路径要用两个反斜杠)
folder_path = 'file'

# 遍历文件夹内所有文件
for file_name in os.listdir(folder_path):
    # 判断是否为图片文件
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        # 打开图片文件
        img_path = os.path.join(folder_path, file_name)
        with Image.open(img_path) as img:
            # 逆时针旋转90度
            rotated_img = img.rotate(90, expand=True)
            # 保存旋转后的图片
            rotated_img.save(img_path)