# pycnblog

博客园上传markdown文件 https://www.cnblogs.com/df888/p/11826480.html

# 功能

- 一键拖拽上传
- 默认“未发布”，可选择直接发布
- 重复上传，提示是否更新博客

# 环境

python3

`git clone git@github.com:dongfanger/pycnblog.git`

`pip install pyyaml`

# 配置

在config.yaml中，填写博客配置信息。

```python
blog_url: https: // rpc.cnblogs.com / metaweblog / testblog
blog_id: "testblog"
username: "zhangsan"
password: "123456"
```

## blog_url

blog_url在博客后台>设置，页面最下方的MetaWeblog访问地址。
https://rpc.cnblogs.com/metaweblog/testblog

## blog_id

blog_id就是访问地址的尾巴， testblog。

## username

username是登录用户名，跟blog_id不一定是同一个。

## password

password是密码。

# 运行

windows cmd:<br/>
打开`cnblog_markdown.cmd`（windows里面双击此文件即可），提示`Please input file path:`<br/>
把文件往里一拖，回车就完事了。

mac:<br/>
配置PATH，`cd ~/`， `vim .bash_profile`，输入`i`编辑，添加`export PATH=/tool_local_path/:$PATH`，按下 “ESC” 按钮，输入`:wq!`
，回车保存。立即生效，`source ~/.bash_profile`。`cd tool_local_path`，修改可执行文件权限，`chmod 777 cnblogmd`。修改`cnblogmd`
文件，`/tool_local_path/upload.py`。 <br/>

以后直接打开终端，输入cnblogmd，就可以了。

可以直接使用python3 upload.py xxx.md命令

这个文章写得比较详细 https://www.cnblogs.com/gered/p/14736136.html

