import json
import os
from opencc import OpenCC

def convert_simplified_to_traditional(obj):
    if isinstance(obj, dict):
        return {key: convert_simplified_to_traditional(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_simplified_to_traditional(element) for element in obj]
    elif isinstance(obj, str):
        return converter.convert(obj)
    else:
        return obj

# 初始化转换器
converter = OpenCC('s2twp')

# 使用绝对路径确保准确性
input_path = r'C:\Users\HsxMa\Documents\GitHub\SJMCL\src\locales\zh-Hans.json'
output_path = r'C:\Users\HsxMa\Documents\GitHub\SJMCL\src\locales\zh-Hant.json'

# 检查文件是否存在
if not os.path.exists(input_path):
    print(f"错误：文件 {input_path} 不存在！")
    exit(1)

# 读取并转换
with open(input_path, 'r', encoding='utf-8') as f:
    simplified_data = json.load(f)

traditional_data = convert_simplified_to_traditional(simplified_data)

# 保存结果
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(traditional_data, f, ensure_ascii=False, indent=2)

print("转换完成！")