import xmlrpc.client

from config import blog_url

blog_url = blog_url.strip()
server = xmlrpc.client.ServerProxy(blog_url)
