import xmlrpc.client

from config_loader import conf

blog_url = conf["blog_url"].strip()
server = xmlrpc.client.ServerProxy(blog_url)
