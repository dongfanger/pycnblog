import asyncio
import html
import os
import ssl
import sys
import xmlrpc.client

from config_loader import conf
from img_transfer import find_md_img, upload_img, replace_md_img
from server_proxy import server

if len(sys.argv) != 3:
    print('Input error')
    # 异常，返回状态码到命令行
    sys.exit(1)

# markdown路径
md_path = sys.argv[1]
md_path = md_path.strip("\"' ")  # 统一mac和linux的路径差异，处理首位的引号和空格
# 如果输入的类别为空，则categories_ls为空列表
categories_ls = sys.argv[2].split(' ') if len(sys.argv[2]) != 0 else []
dir_path = os.path.dirname(md_path)
title = None
net_images = []  # 图片上传后url
image_count = 0  # 图片计数


# 回调，获取url
def get_image_url(t):
    # 修改全局变量，加global
    global image_count
    url = t.result()['url']
    image_count += 1
    print('Image {} uploading success, url {}'.format(image_count, url))
    net_images.append(url)


# 取消全局ssl认证，安全性换性能提升
def cancel_ssh_authentication():
    ssl._create_default_https_context = ssl._create_unverified_context


async def upload_tasks(local_images_):
    tasks = []
    for li in local_images_:
        image_full_path = os.path.join(dir_path, li)
        task = asyncio.create_task(upload_img(image_full_path))
        task.add_done_callback(get_image_url)
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    cancel_ssh_authentication()
    try:
        with open(md_path, encoding='utf-8') as f:
            md = f.read()
            print('Reading markdown success: {}'.format(md_path))
            local_images = find_md_img(md)
            if local_images:  # 有本地图片，异步上传
                asyncio.run(upload_tasks(local_images))
                image_mapping = dict(zip(local_images, net_images))
                md = replace_md_img(md_path, image_mapping)
            else:
                print('No images to upload')

            # 删除第一行大标题
            if md and md[0].startswith("#"):
                # 按行分割内容
                md = md.splitlines()
                title = md[0].lstrip("# ").rstrip()  # 第一行大标题作为博客标题。去掉开头的#和空格
                # 删除第一行（大标题）
                md = md[1:]
                # 将剩余的行重新拼接为字符串
                md = "\n".join(md)

            if title is None:
                print('No title')
                sys.exit(1)

            post = dict(description=md, title=title, categories=['[Markdown]'] + categories_ls)  # + 合并列表
            # 博客园的博文最大可获取数量为100
            recent_posts = server.metaWeblog.getRecentPosts(conf["blog_id"], conf["username"], conf["password"], 99)
            # 获取所有标题，需要处理HTML转义字符
            recent_posts_titles = [html.unescape(recent_post['title']) for recent_post in recent_posts]

            if title not in recent_posts_titles:  # 新文章
                server.metaWeblog.newPost(conf["blog_id"], conf["username"], conf["password"], post, conf["publish"])
                status = 'Published' if conf['publish'] else 'Unpublished'
                print('Upload success. Title: {}, Status: {}, Category: {}'.format(title, status, categories_ls))
                sys.exit(0)
            else:
                for recent_post in recent_posts:
                    if title == html.unescape(recent_post['title']):
                        print('update')
                        update_post = recent_post
                        update_post['description'] = md
                        # 博客更新时保留摘要、标签
                        posted_article = server.metaWeblog.getPost(update_post['postid'], conf["username"],
                                                                   conf["password"])
                        try:
                            update_post["mt_keywords"] = posted_article["mt_keywords"]
                            update_post["mt_excerpt"] = posted_article["mt_excerpt"]
                        except KeyError as ke:
                            print('When updating cnblog, {}'.format(ke))
                            sys.exit(1)
                        try:
                            server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"],
                                                       update_post,
                                                       conf["publish"])
                        except xmlrpc.client.Fault as fault:
                            if 'published post can not be saved as draft' in str(fault):
                                server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"],
                                                           update_post, True)
                            else:
                                raise fault
                            sys.exit(1)
                        print('Cnblog {} update success.'.format(title))
                        sys.exit(0)

    except FileNotFoundError:
        print('The file {} does not exist'.format(md_path))
        sys.exit(1)
    except PermissionError:
        print('Permission denied for file {}'.format(md_path))
        sys.exit(1)
    except  IsADirectoryError:
        print('File {} is a directory, not a file'.format(md_path))
        sys.exit(1)
    except IOError as e:
        print('Error: {}'.format(e))
        sys.exit(1)
