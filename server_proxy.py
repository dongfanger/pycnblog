import sys
import xmlrpc.client

from config_loader import conf

blog_url = conf["blog_url"].strip()
try:
    server = xmlrpc.client.ServerProxy(blog_url)
except Exception as e:
    e = str(e)
    if 'unsupported XML-RPC protocol' in e:
        print('Check blog_url in config.yaml')
    sys.exit(1)
