import xmlrpc.client

from config_loader import conf

blog_url = conf["blog_url"].strip()
try:
    server = xmlrpc.client.ServerProxy(blog_url)
except Exception as e:
    e = str(e)
    if 'unsupported XML-RPC protocol' in e:
        print('请查看config.yaml文件中的blog_url,应该是这个URL地址没设置对')
