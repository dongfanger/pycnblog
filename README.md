# pycnblog
博客园上传markdown文件 https://www.cnblogs.com/df888/p/11826480.html

# 功能

- 一键拖拽上传
- 默认“未发布”，支持直接发布
- 重复上传，更新博客
- 支持上传后图片转为\<img src="" width=100% /\>，方便调整宽度
- 支持上传后生成替换后本地文件

# 环境

python3

# 配置

在config.py中，填写博客配置信息。

```python
blog_url = 'https://rpc.cnblogs.com/metaweblog/testblog'
blog_id = 'testblog'
username = 'zhangsan'
password = '123456'
```

## blog_url

blog_url在博客后台>设置，页面最下方的MetaWeblog访问地址。
https://rpc.cnblogs.com/metaweblog/testblog

## blog_id

blog_id就是访问地址的尾巴。
testblog

## username

username是登录用户名，跟blog_id不一定是同一个。

## password

password是密码。

# 运行

windows cmd:<br/>
打开`cnblog_markdown.cmd`（windows里面双击此文件即可），提示`Please input file path:`<br/>
把文件往里一拖，回车就完事了
