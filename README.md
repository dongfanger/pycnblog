# PyCnblog
博客园上传markdown文件 https://www.cnblogs.com/df888/p/11826480.html

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

username是登录用户名，跟blog_id不是同一个。

## password

password是密码。

# 运行

方式1 执行命令：

```shell
python upload.py ${filePath}  # 文件路径不包括空格
```

```python
python upload.py "${filePath}"  # 若文件路径包含空格，需要加双引号
```

方式2 Windows系统 cmd：

双击打开`cnblog_markdown.cmd`，提示`Please input file path:`，把文件往cmd窗口拖就能带出来文件路径，如果文件名包含空格，还会自动加双引号。为方便可右键发送到桌面快捷方式。
