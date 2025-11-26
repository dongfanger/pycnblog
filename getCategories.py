"""
@Time    : 2024/8/12
@Author  : 顾子郤
@Function: 获取博客园的标签
"""
from server_proxy import server
from config_loader import conf

if __name__ == '__main__':
    current_categories = server.metaWeblog.getCategories(conf["blog_id"], conf["username"], conf["password"])
    ls_categories = []
    for category in current_categories:
        if "随笔分类" in category['title']:
            ls_categories.append(category['title'][6:])  # 避开开头的[随笔分类]文字
    print("Current categories: {}".format("\t".join(ls_categories)))
