import asyncio
import html
import sys
import xmlrpc.client

from img_transfer import *

if len(sys.argv) == 1:
    print('请输入markdown文件路径,带双引号哦')
    exit(-1)

md_path = sys.argv[1:][0]  # markdown路径
dir_name = os.path.dirname(md_path)

title, _ = os.path.splitext(os.path.basename(md_path))  # 文件名作为博客标题

net_images = []  # 图片上传后url
image_count = 1  # 图片计数


def get_image_url(t):
    """回调，获取url"""
    global image_count
    url = t.result()['url']
    print(f'第{image_count}张图片上传成功,url:{url}')
    net_images.append(url)
    image_count += 1


with open(md_path, encoding='utf-8') as f:
    md = f.read()
    print(f'markdown读取成功:{md_path}')
    local_images = find_md_img(md)

    if local_images:  # 有本地图片，异步上传
        tasks = []
        for li in local_images:
            image_full_path = os.path.join(dir_name, li)
            task = asyncio.ensure_future(upload_img(image_full_path))
            task.add_done_callback(get_image_url)
            tasks.append(task)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

        image_mapping = dict(zip(local_images, net_images))

        md = replace_md_img(md_path, image_mapping)
    else:
        print('无需上传图片')

    post = dict(description=md, title=title, categories=['[Markdown]'])
    recent_posts = server.metaWeblog.getRecentPosts(conf["blog_id"], conf["username"], conf["password"], 999999)
    # 获取所有标题，需要处理HTML转义字符
    recent_posts_titles = [html.unescape(recent_post['title']) for recent_post in recent_posts]
    if title not in recent_posts_titles:
        server.metaWeblog.newPost(conf["blog_id"], conf["username"], conf["password"], post, conf["publish"])
        print(f"markdown上传成功, 博客标题为'{title}', 状态为'未发布', 请到博客园后台查看")
    elif input('博客已存在, 是否更新?(y/n)') == 'y':
        for recent_post in recent_posts:
            if title == recent_post['title']:
                update_post = recent_post
                update_post['description'] = md
                try:
                    server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"], update_post,
                                               False)
                except xmlrpc.client.Fault as fault:
                    if 'published post can not be saved as draft' in str(fault):
                        server.metaWeblog.editPost(update_post['postid'], conf["username"], conf["password"],
                                                   update_post, True)
                    else:
                        raise fault
                print(f"博客'{title}'更新成功")
    else:
        print('上传已取消')
