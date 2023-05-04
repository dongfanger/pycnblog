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


def _check_categories(categories):
    new = []
    if categories:
        for one in categories.split(','):
            if str(one).strip() != "":
                new.append(one)
    else:
        new = []
    return new


def check_categories(categories):
    try:
        categories = _check_categories(categories)
        print(f"要添加到的分类为:{categories}")
        return categories
    except:
        print("类别错误, 设置类别为空")
        return []


conf["categories"] = check_categories(conf["categories"])
