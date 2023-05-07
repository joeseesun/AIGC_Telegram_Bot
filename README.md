
指定twitter ID 列表，定时抓取推特内容更新发送给自己的Telegram Bot。

Use jupyter-lab to send Twitter updates from a list of users to your Telegram bot. 


## Fork说明

- 项目fork自[@joeseesun](https://github.com/joeseesun/AIGC_Telegram_Bot)，感谢原作者带来的推动力和诸多启发！
- 对这个项目感兴趣是因为我认为在不久的将来，用户可获取所有线上公开内容，每人将拥有自己的算法，在全网范围过滤信息和整理信息。付费信息也可以通过便利的市场完成交易。
- 信息的流动将会变得异常高效，而各种互联网平台，只是处理某一类信息的算法公司，用户将不必需要这些平台提供信息的推荐服务。
- 未来，一个视频可以发布在一个图床，然后声明允许各大视频网站抓取，并且提供对应的用户名，就可以实现全网发布。一篇文章，一段声音，也可以用同样的方式全网发布。
- 全网发布，则意味着全网的用户都可以消费，并且使用自己最希望的方式去消费，比如，查看一个视频的总结和关键帧之后再看视频，查询与一篇文章相似的其他文章的合集，为文章添加AI配图之后再去阅读，文字|声音|视频|问答交互|等多模态之间可以自由切换。信息的消费方式将会实现高度的个性化。

## 更新要点
- 改为放在jupyter-lab中运行，可以快速实验一些想法
- 添加了一个文件，用于保存时间戳，来判断需要更新的内容，首次运行，会获取一小时内的内容
- 添加了异步函数，同时请求多个rss源，减少等待时间
- 添加了设置telegram api代理地址的功能，可参考[这里](https://blog.orii.xyz/202301/%E4%BD%BF%E7%94%A8cloudflare-Worker%E4%BB%A3%E7%90%86telegram-bot-api/)


## Todo
- rsshub中，可能有跟时间相关的请求格式，带上时间去请求，可以减少数据传输
- 鉴于rsshub有大量信息可订阅，需要一个分类订阅信息的功能，最好能有一个基于本地web端的数据看板和订阅源管理模块
- 订阅的内容，发送到telegram是多种消费方式的一种，不妨喂进去AI模型，先提炼总结下

## 如果显示连接timeout
- 首先`ping api.telegram.org`,看下是否可以连上
- 如果ping不通，可以试下全局翻，并且打开clash的增强模式
- 或者可以使用telegram api代理地址


## 使用方法

1. 创建Telegram机器人，获取Token
- 打开 https://t.me/botfather 输入 /start
- 按引导流程，先输入机器人名字，然后输入想要ID（必须以bot结尾），比如telegram_rss_bot
- 创建后会给Token，类似这种结构：5987500169:AAEBqLx7OWmK6ne9pIfHhrgMktDmq_VcsSQ

2. 获取自己的Telegram ID
打开 https://t.me/userinfobot 输入 \/start，拿到自己的ID，类似结构：1293676963


3. 设置Token和Telegram ID

- 把Token和Telegram ID 填入env.txt文件，然后把env.txt改名为".env"
- 需要添加telegram api代理地址的，也可以设置在TELEGRAM_API_BASE_URL，防止网络无法连上
- 如果有自己的rss的服务器，比如自建的rsshub服务器地址，也可以设置在RSS_BASE_URL

4. 把 cutoff_time2.txt 改名为 cutoff_time.txt，用于保存时间戳

5. 添加venv，安装依赖程序
```
python3 -m venv .venv_bot
source .venv_bot/bin/activate
pip install -r requirements.txt
```

6. 运行程序
```
jupyter-lab
```
之后打开rss.ipynb

7. 如果需要停止程序，在最后出现的输入框中按回车即可


## 想自定义关注人？
修改 twitter_list.txt ，一个一个 twitter ID，逗号分割后面是名字，可自定义（非必须）







