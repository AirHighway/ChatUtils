import os
import numpy as np
from PIL import Image


# 获取文件夹下所有文件的文件名
def get_file_names_in_directory(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(file)
    return file_names


# 拼接文件夹路径和文件名到新的列表中
def join_folder_and_file_names(folder_path, file_names):
    # 初始化一个空列表来存放拼接后的完整路径
    full_paths = []

    # 使用os.path.join()拼接文件夹路径和文件名
    for file_name in file_names:
        full_path = os.path.join(folder_path, file_name)
        full_paths.append(full_path)

    return full_paths


# 调用函数读取PNG图像并转换为float32的NumPy数组
def read_png_image(filepath):
    try:
        # 读取PNG图像
        image = Image.open(filepath)

        # 将图像转换为float32类型的NumPy数组
        image_array = np.array(image).astype(np.float32) / 1.0

        return image_array
    except Exception as e:
        print("Error:", str(e))
        return None


# 示例用法
if __name__ == "__main__":
    # image文件夹路径
    image_path = r"D:\Trnasformer\T02_STUnet\data\Satellite dataset Ⅰ (global cities)\image"
    # label文件夹路径
    label_path = r"D:\Trnasformer\T02_STUnet\data\Satellite dataset Ⅰ (global cities)\label"
    # 保存npz文件的文件夹路径
    npz_save_path = r"D:\Trnasformer\T02_STUnet\data\Satellite dataset Ⅰ (global cities)\npz_save_path"

    # 读取所有文件的名字
    file_names = get_file_names_in_directory(image_path)
    # 计算列表的长度
    list_length = len(file_names)
    # 拼接image和label以及输出文件的完整路径
    image_full_paths = join_folder_and_file_names(image_path, file_names)
    label_full_paths = join_folder_and_file_names(label_path, file_names)
    npz_save_paths = join_folder_and_file_names(npz_save_path, file_names)
    for i in range(list_length):
        # 读取图片中的数组
        image_array = read_png_image(image_full_paths[i])
        label_array = read_png_image(label_full_paths[i])
        npz_file_name = npz_save_paths[i]
        np.savez(npz_file_name, image=image_array, label=label_array)
        if i > 0 and i % 50 == 0:
            print(f"已经完成了 {i} 组图像的处理。")
    print(f"已经完成了 {i} 组图像的处理。")
