# 博客上传脚本——博客园

## 致谢

本项目基于[pycnblog](https://github.com/dongfanger/pycnblog)，由[dongfanger](https://github.com/dongfanger)等贡献者完成开发。在此特别感谢原作者的杰出工作。同时，感谢所有为开源社区做出贡献的开发者们！

## 功能

目前，仅支持上传至博客园的随笔。

- 默认“未发布”，可选择直接发布
- 重复上传，则更新博客
- 提供类别提示
- 选择上传的类别。若选择的类别不存在，则会创建新类别

## 环境配置

1. 克隆仓库

`git clone git@github.com:Shane-shy/pycnblog.git`

2. 环境配置：需要`python`，`pip`以及库函数`pyyaml`，库函数可以自动安装。三种情况命令行都会进行相应提示。

3. 修改配置文件`config.yaml`

   - blog_url：在博客后台>设置，页面最下方的MetaWeblog访问地址
   - blog_id：blog_url的结尾部分
   - username：登录用户名，跟blog_id不一定是同一个，最好去用户设置内查看
   - password：在博客后台>设置，页面最下方的MetaWeblog访问令牌

4. 相关补充文件

   - `config.yaml`

   ```yaml
   # 注意引号
   blog_url: xxx
   blog_id: 'xxx'
   username: 'xxx'
   # MetaWeblog访问令牌
   password: 'xxx'
   
   # 是否生成图片替换后本地文件,默认False关闭
   gen_network_file: False
   
   # 上传后是否发布，默认未发布，设置True为发布
   publish: False
   
   # 图片自定义显示格式，默认不设置
   
   # 设置居中和宽度
   # img_format: "<center><img src="" style="width:100%;" /></center>"
   
   # 还原typora图片样式，居中，设置zoom，上传后无需再手动调整图片大小
   img_format: typora
   
   # 不设置
   #img_format: ""
   ```

   - `linux_upload_markdown.sh`

   ```shell
   #!/bin/bash
   
   # 设置getCategories.py的绝对路径
   PYTHON_CATEGORIES_PATH=""
   # 设置upload_markdown.py的绝对路径
   PYTHON_UPLOAD_PATH=""
   
   # &> /dev/null：重定向并丢弃，避免将检测结果输出在终端，
   # 检查是否安装了 Python
   if  ! command -v python3 &> /dev/null;then
       echo "Python3 未安装，请安装 Python3。"
       exit 1
   fi
   
   # 检查是否安装了 pip
   if  ! command -v pip3 &> /dev/null;then
       echo "pip3 未安装，请安装 pip3。"
       exit 1
   fi
   
   # 检查是否安装了所需的 Python 包
   REQUIRED_PKG="pyyaml"
   for PKG in $REQUIRED_PKG; do
       if ! pip3 show $PKG &> /dev/null; then
           echo "$PKG 未安装，正在安装..."
           pip3 install $PKG
       fi
   done
   
   # 检测是否配置了Python脚本路径
   if [ -z $PYTHON_UPLOAD_PATH ];then
     echo "未配置upload_markdown.py脚本路径"
     exit 0
   fi
   
   if [ -z $PYTHON_CATEGORIES_PATH ];then
     echo "未配置getCategories.py脚本路径"
     exit 0
   fi
   
   
   
   while true; do
     # read：按行读取，可以一次性读取多个值；参数p：读入字符串之前，打印的提示字符串；
       read -p  "Please input file path: " filePath
       python "$PYTHON_CATEGORIES_PATH"
       read -p  "Please input categories (separated by space): " category
       python "$PYTHON_UPLOAD_PATH" "$filePath" "$category"
       status=$?
       if [ $status -eq 0 ];then
         echo "Uploading success"
         break
       else
         echo "Uploading fail"
       fi
   done
   ```
   
   - `mac_upload_markdown`：应该与`linux_upload_markdown.sh`相同
   

## 使用方法

- Linux：`bash linux_upload_markdown.sh`，根据提示执行之后操作。`Please input file path:`时，可以直接将文件拖入命令行，就能生成绝对路径。**通过测试。**
- Macos：与Linux相同，**通过测试。**
- Windows：本项目实际运行是python脚本，因此不存在操作系统限制。笔者能力有限，若希望实现Windows终端执行本脚本，请自行编写终端脚本文件。

### 常见问题

1. 上传失败，留意终端报错信息。
2. 图片无法上传、图片文件路径正确但程序无法找到。
   - 检查是否存在“空图像”，如**`![]()`或`\<img src = "" />`**。若存在，请删除。
   - 检查图片路径是否存在括号嵌套问题，如**`![](())`**。使用正则表达式筛选括号嵌套问题难度大，笔者能力有限，没能实现，所以请修改图片名称或图片路径为非括号嵌套形式。



