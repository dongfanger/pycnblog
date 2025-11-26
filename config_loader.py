"""
@Time    : 2024/5/23 
@Author  : 顾子郤
@Function: 读取config.yaml
"""

import yaml
import os

# 获取当前脚本的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前脚本所在目录的路径
current_directory = os.path.dirname(current_file_path)

# 读取config.yaml
config_path = current_directory + '/' + 'config.yaml'
with open(config_path, "r", encoding="utf-8") as f:
    conf = yaml.load(f.read(), Loader=yaml.FullLoader)
