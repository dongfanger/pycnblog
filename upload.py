import asyncio
import html
import ssl
import sys
import tkinter as tk
import xmlrpc.client
import windnd

from img_transfer import *
from tkinter import *


# if len(sys.argv) == 1:
#     print('请输入markdown文件路径,带双引号哦')
#     exit(-1)
def dragged_files(files):
    for file in files:
        print(file.decode('utf-8'))


window = tk.Tk()
window.title("First Window")
window.geometry("1100x680")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

windnd.hook_dropfiles(window, func=dragged_files)
window.mainloop()

# md_path = "D:\documents\博客\博客园上传markdown文件.md"  # markdown路径
# dir_name = os.path.dirname(md_path)
#
# title, _ = os.path.splitext(os.path.basename(md_path))  # 文件名作为博客标题
#
# net_images = []  # 图片上传后url
# image_count = 1  # 图片计数
#
#
# def get_image_url(t):
#     """回调，获取url"""
#     global image_count
#     url = t.result()['url']
#     print(f'第{image_count}张图片上传成功,url:{url}')
#     net_images.append(url)
#     image_count += 1
#
#
# def cancel_ssh_authentication():  # 取消全局ssl认证
#     ssl._create_default_https_context = ssl._create_unverified_context
#
#
# async def upload_tasks(local_images_):
#     tasks = []
#     for li in local_images_:
#         image_full_path = os.path.join(dir_name, li)
#         task = asyncio.create_task(upload_img(image_full_path))
#         task.add_done_callback(get_image_url)
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
#
# if __name__ == '__main__':
#     cancel_ssh_authentication()
#     with open(md_path, encoding='utf-8') as f:
#         md = f.read()
#         print(f'markdown读取成功:{md_path}')
#         local_images = find_md_img(md)
#
#         if local_images:  # 有本地图片，异步上传
#             asyncio.run(upload_tasks(local_images))
#             image_mapping = dict(zip(local_images, net_images))
#             md = replace_md_img(md_path, image_mapping)
#         else:
#             print('无需上传图片')
#
#         post = dict(description=md, title=title, categories=['[Markdown]']+conf["categories"])
#         recent_posts = server.metaWeblog.getRecentPosts(conf["blog_id"], conf["username"], conf["password"], 99)
#         # 获取所有标题，需要处理HTML转义字符
#         recent_posts_titles = [html.unescape(recent_post['title']) for recent_post in recent_posts]
#         if title not in recent_posts_titles:
#             server.metaWeblog.newPost(conf["blog_id"], conf["username"], conf["password"], post, conf["publish"])
#             print(f"markdown上传成功, 博客标题为'{title}', 状态为'{'已发布' if conf['publish'] else '未发布'}', "
#                   f"分类为:{conf['categories']} 请到博客园后台查看")
#         else:
#             for recent_post in recent_posts:
#                 if title == html.unescape(recent_post['title']):
#                     update_post = recent_post
#                     update_post['description'] = md
#                     # 博客更新时保留摘要、标签
#                     posted_article = server.metaWeblog.getPost(update_post['postid'], conf["username"],
#                                                                conf["password"])
#                     try:
#                         update_post["mt_keywords"] = posted_article["mt_keywords"]
#                         update_post["mt_excerpt"] = posted_article["mt_excerpt"]
#                     except KeyError:
#                         pass
#                     try:
#                         server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"],
#                                                    update_post,
#                                                    conf["publish"])
#                     except xmlrpc.client.Fault as fault:
#                         if 'published post can not be saved as draft' in str(fault):
#                             server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"],
#                                                        update_post, True)
#                         else:
#                             raise fault
#                     print(f"博客'{title}'更新成功")
