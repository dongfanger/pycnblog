#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  Don
@Date    :  9/16/2020 1:40 PM
@Desc    :  
"""
import os

import yaml

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")

with open(config_path, "r", encoding="utf-8") as f:
    conf = yaml.load(f.read(), Loader=yaml.FullLoader)
