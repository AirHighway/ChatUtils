from PIL import Image
import os

def load_image_pixels(image_path):
    """加载图片并返回像素值列表"""
    with Image.open(image_path) as img:
                    # 获取图片的像素数据
                    pixels = img.load()
                    # 初始化像素值之和
                    pixel_sum = 0
                    # 遍历图片的每个像素
                    for y in range(img.size[1]):
                        for x in range(img.size[0]):
                            pixel_sum += pixels[x, y]
    return pixel_sum


def check_zero_pixels(pixel_sums):
    """检查像素和列表中是否包含0"""
    return 0 in pixel_sums

def main():
    txt_file_path = r'D:\WorkSpace\002 - 20240620 - paper&code-Read\Datasets\WD_Dataset_WaterFormer\dataset_png\dataset_png_label_01_512_含有水体像素的所有图片.txt'  # txt文件路径
    root_path = r'D:\WorkSpace\002 - 20240620 - paper&code-Read\Datasets\WD_Dataset_WaterFormer\dataset_png\dataset_png_label_01_512'  # 根路径
    
    pixel_sums = []
    with open(txt_file_path, 'r') as file:
        for line in file:
            img_path = os.path.join(root_path, line.strip())  # 去除空白字符并添加根路径
            pixels = load_image_pixels(img_path)
            # print(pixels)
            pixel_sums.append(pixels)  # 计算像素和
            # print(pixel_sums)
    
    
    
    # pixel_sums = process_txt_file(txt_file_path, root_path)
    
    pixel_sums.sort()
    print("排序后的像素和列表:", pixel_sums)
    print("是否包含0:", check_zero_pixels(pixel_sums))

if __name__ == '__main__':
    main()
