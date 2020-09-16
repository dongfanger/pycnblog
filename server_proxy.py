import xmlrpc.client

from init import conf

blog_url = conf["blog_url"].strip()
server = xmlrpc.client.ServerProxy(blog_url)
