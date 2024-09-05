import numpy as np

# 假设你的.npz文件名为data.npz
file_name = r'D:\WorkSpace\002 - 20240620 - paper&code-Read\Codes\Swin-Unet-main\data\Synapse\17.png.npz'

# 使用numpy的load函数读取.npz文件
data = np.load(file_name)

# 打印出文件中包含的所有数组和它们的详细信息
for key, value in data.items():
    print(f"数组名称: {key}")
    print(f"形状: {value.shape}")
    print(f"数据类型: {value.dtype}")
    print(f"数组内容（部分）:")
    print(value[:5])  # 打印数组的前5个元素
    print("---")  # 分隔线


# 后发现
# 在保存image和label为.npz文件的时候
# np.savez(npz_filename, image=image, label=label) 
# 指定了image和label
# 所以读取的时候，指导保存的数据哪里是图像、哪里是标签
