import os
import re

from config_loader import conf
from mime import mime_mapping
from server_proxy import server


def find_md_img(md):
    """ markdown中的代码内容不需要参与以下的正则匹配 """
    pattern = r"```.*?```"
    md = re.sub(pattern, "", md, flags=re.DOTALL)

    """查找markdown中的图片，排除网络图片(不用上传)"""
    images = re.findall("\\!\\[.*?\\]\\((.*?)\\)", md)
    images += re.findall('<img src="(.*?)"', md)
    images = [i for i in images if not re.match("((http(s?))|(ftp))://.*", i)]
    print(f'共找到{len(images)}张本地图片')
    print(*images, sep='\n')
    return images


async def upload_img(path):
    """上传图片"""
    name = os.path.basename(path)
    _, suffix = os.path.splitext(name)
    print(f"正在上传{name}")
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
                        md = md.replace(ml, f'<center><img src="{img_url}"  style="width:{zoom[0]}%;" /></center>')
                else:
                    md = md.replace(ml, conf["img_format"].format(img_url))
        if conf["gen_network_file"]:
            path_net = os.path.join(os.path.dirname(path), '_network'.join(os.path.splitext(os.path.basename(path))))
            with open(path_net, 'w', encoding='utf-8') as fw:
                fw.write(md)
                print(f'图片链接替换完成，生成新markdown:{path_net}')
        return md
