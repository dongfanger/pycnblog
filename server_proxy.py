import xmlrpc.client

from config import blog_url


server = xmlrpc.client.ServerProxy(blog_url)
