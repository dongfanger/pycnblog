import os
import re

from config_loader import conf
from mime import mime_mapping
from server_proxy import server


def find_md_img(md):
    """查找markdown中的图片，排除网络图片(不用上传)"""
    # 获取图片非空链接。使用非贪婪匹配，不然(.+?)会匹配之后的全部
    images = re.findall(r"!\[.*?\]\((.+?)\)", md)  # 避免出现括号嵌套，否则无法识别
    images += re.findall(r'<img\s+[^>]*\bsrc\s*=\s*[\"\'](.+?)[\"\'][^>]*>', md)
    images = [i for i in images if not re.match("((https?)|(ftp))://.*", i)]
    print('{} images found'.format(len(images)))
    #  *：解包操作符，将images列表元素分别通过print打印，并用换行符隔开，功能类似于遍历列表打印元素
    print(*images, sep='\n')
    return images


async def upload_img(path):
    """上传图片"""
    name = os.path.basename(path)
    # 图像的后缀
    _, suffix = os.path.splitext(name)
    print("Uploading {}".format(name))
    with open(path, 'rb') as f:
        file = {
            "bits": f.read(),
            "name": name,
            "type": mime_mapping[suffix]
        }
        url = server.metaWeblog.newMediaObject(conf["blog_id"], conf["username"], conf["password"], file)
        return url


def replace_md_img(path, img_mapping):
    """替换markdown中的图片链接"""
    # 这里不使用异常处理，因为在upload_markdown.py中一开始就使用了，如果读取文件出现异常，那么在这里肯定也会异常
    with open(path, 'r', encoding='utf-8') as fr:
        md = fr.read()
        for local, net in img_mapping.items():  # 替换图片链接
            md = md.replace(local, net)
        if conf["img_format"]:
            md_links = re.findall("!\\[.*?\\]\\(.*?\\)", md)
            md_links += re.findall('<img src=.*/>', md)
            for ml in md_links:
                img_url = re.findall("!\\[.*?\\]\\((.*?)\\)", ml)
                img_url += re.findall('<img src="(.*?)"', ml)
                img_url = img_url[0]

                if conf["img_format"] == "typora":
                    zoom = re.findall(r'style="zoom:(.*)%;"', ml)
                    if zoom:
                        replacement = f'<center><img src="{img_url}"  style="width:{zoom[0]}%;" /></center>'
                        md.replace(ml, replacement)
                else:
                    replacement = conf["img_format"].format(img_url)
                    md.replace(ml, replacement)

        if conf["gen_network_file"]:
            path_net = os.path.join(os.path.dirname(path),
                                    '_network'.join(os.path.splitext(os.path.basename(path))))
            with open(path_net, 'w', encoding='utf-8') as fw:
                fw.write(md)
                print('Images replacement success.')
        return md
