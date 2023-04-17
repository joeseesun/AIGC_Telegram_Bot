# AIGC_Telegram_Bot
编程新手用GPT4辅助开发的一个Telegram机器人，指定twitter ID，自动抓取推特消息并翻译成中文发给自己的Telegram账号。

# 使用方法

① 创建Telegram机器人，获取Token
打开 https://t.me/botfather 输入 /start
按引导流程，先输入机器人名字，然后输入想要ID（必须以bot结尾），比如telegram_rss_bot
创建后会给Token，类似这种结构：5987500169:AAEBqLx7OWmK6ne9pIfHhrgMktDmq_VcsSQ

② 获取自己的Telegram ID
打开 https://t.me/userinfobot 输入 \/start，拿到自己的ID，类似结构：1293676963


③ 设置Token和Telegram ID

把Token和Telegram ID 填入env.txt文件，然后把env.txt改名为".env"

④ 安装依赖程序
```
pip install -r requirements.txt
```

⑤ 运行程序
python main.py

# 想自定义关注人？
修改 twitter_list.txt ，一个一个 twitter ID，逗号分割后面是名字，可自定义（非必须）

# 求帮优化改进
自己是产品经理，不怎么会代码。
以上都是GPT4帮写的，希望程序员大佬帮优化改进。

# 如果显示连接timeout
首先`ping api.telegram.org`,看下是否可以连上
如果ping不通，可以试下全局翻，并且打开增强模式






