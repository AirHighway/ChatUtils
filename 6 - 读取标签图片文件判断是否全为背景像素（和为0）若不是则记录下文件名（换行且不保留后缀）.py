import os
from PIL import Image

def read_images_in_folder(folder_path, output_file):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是图片
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 构建完整的文件路径
            file_path = os.path.join(folder_path, filename)
            # 打开图片
            with Image.open(file_path) as img:
                # 获取图片的像素数据
                pixels = img.load()
                # 初始化像素值之和
                pixel_sum = 0
                # 遍历图片的每个像素
                for y in range(img.size[1]):
                    for x in range(img.size[0]):
                        pixel_sum += pixels[x, y]
                # 如果像素值之和不为0，则记录文件名
                if pixel_sum != 0:
                    # 直接使用完整的文件名，不去除后缀
                    # 写入到输出文件中
                    with open(output_file, 'a') as f:
                        f.write(filename)
                        f.write("\n")

# 使用示例
folder_path = r'D:\WorkSpace\002 - 20240620 - paper&code-Read\Datasets\WD_Dataset_WaterFormer\dataset_png\dataset_png_label_01_512'  # 替换为你的图片文件夹路径
output_file = r'D:\WorkSpace\002 - 20240620 - paper&code-Read\Datasets\WD_Dataset_WaterFormer\dataset_png\dataset_png_label_01_512_含有水体像素的所有图片.txt'  # 输出文件的名称
read_images_in_folder(folder_path, output_file)
