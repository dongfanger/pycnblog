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

```python
python upload.py "文件路径"  # 注意要用双引号哦
```

方式2 Windows系统 cmd：

双击打开`cnblog_markdown.cmd`，`Please input file path:`，把.md文件往cmd中一拖，`Please input file path:"E:\Test Case.md"`，再回车一敲。因为windows把文件拖到cmd会自动把路径以双引号形式，显示出来。为了方便可右键`cnblog_markdown.cmd`创建桌面快捷方式。
