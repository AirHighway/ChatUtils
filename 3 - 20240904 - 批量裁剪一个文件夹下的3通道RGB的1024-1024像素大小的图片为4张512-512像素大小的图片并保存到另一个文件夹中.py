from PIL import Image
import os

def crop_image(image, crop_size, start_x, start_y):
    # 裁剪图像
    return image.crop((start_x, start_y, start_x + crop_size[0], start_y + crop_size[1]))

def crop_and_save_images(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # 构建完整的文件路径
            file_path = os.path.join(input_folder, filename)
            # 打开图像
            with Image.open(file_path) as img:
                # 检查图像尺寸是否正确
                if img.size == (1024, 1024) and img.mode == 'RGB':
                    # 裁剪图像为4个512x512的图像
                    crop_size = (512, 512)
                    # 确定每个裁剪区域的起始坐标
                    start_x = 0
                    start_y = 0
                    cropped_images = [
                        crop_image(img, crop_size, start_x, start_y),
                        crop_image(img, crop_size, start_x, start_y + crop_size[1]),
                        crop_image(img, crop_size, start_x + crop_size[0], start_y),
                        crop_image(img, crop_size, start_x + crop_size[0], start_y + crop_size[1])
                    ]
                    # 保存裁剪后的图像
                    for i, cropped_img in enumerate(cropped_images):
                        # 构建输出文件名
                        output_filename = f"{filename.rsplit('.', 1)[0]}_{i+1}.png"
                        # 构建输出文件路径
                        output_path = os.path.join(output_folder, output_filename)
                        # 保存裁剪后的图像
                        cropped_img.save(output_path)
                else:
                    print(f"图像 {filename} 的尺寸不是1024x1024或不是3通道，无法裁剪。")
                    
                    
# 调用函数，传入输入和输出文件夹路径
input_folder_path = r'path1'  # 替换为实际的输入文件夹路径
output_folder_path = r'path2'  # 替换为实际的输出文件夹路径
crop_and_save_images(input_folder_path, output_folder_path)
