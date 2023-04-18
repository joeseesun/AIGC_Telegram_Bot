# -*- coding: utf-8 -*-
import time
import feedparser
import requests
from telegram import Bot
from datetime import datetime
from bs4 import BeautifulSoup
from translate import Translator
from dotenv import load_dotenv
import os
import asyncio

# Set the source and target languages
source_language = "en"
target_language = "zh"
translator = Translator(from_lang=source_language, to_lang=target_language)

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv("TOKEN")
target_chat_id = os.getenv("target_chat_id")
TELEGRAM_API_BASE_URL=os.getenv("TELEGRAM_API_BASE_URL", "https://api.telegram.org/bot")

bot = Bot(
    token=TOKEN,
    base_url=TELEGRAM_API_BASE_URL,
    )

rss_list = []
# 读取文本文件
with open("twitter_list.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 遍历文本里的每一行
for line in lines:
    info = line.strip().split(',')

    # 获取 Twitter ID 和昵称
    twitter_id = info[0].strip()
    nickname = info[1].strip() if len(info) > 1 else twitter_id

    # 构造 URL
    url = f"http://rss.qiaomu.pro/twitter/user/{twitter_id}"

    # 添加到 rss_list
    rss_list.append({
        "name": nickname,
        "url": url
    })

    # print(f"rss list is {rss_list}")

def get_latest_twitter_updates(rss_url, last_item_link):
    response = requests.get(rss_url)
    rss_content = response.content
    feed = feedparser.parse(rss_content)
    
    latest_items = []
    for entry in feed["entries"]:
        if entry["link"] == last_item_link:
            break
        latest_items.append(entry)


    # print(f"content list is {latest_items}")
        
    return latest_items

async def send_update_to_telegram(items):

    # print(f"in async send, item length is {len(items)}")

    for item in items:
        author = item["author"]
        title = item["title"]

        # print(f"author is {author}, title is {title}")

        description_html = item["description"]
        soup = BeautifulSoup(description_html, 'html.parser')

        # Convert div with class rsshub-quote
        rsshub_quotes = soup.find_all('div', class_='rsshub-quote')
        for rsshub_quote in rsshub_quotes:
            rsshub_quote.string = f"\n&gt; {rsshub_quote.get_text(separator=' ', strip=True)}\n\n"
        
        for br in soup.find_all('br'):
            br.replace_with('\n')
        
        description = "\n".join(soup.stripped_strings)
        description_zh = translator.translate(description)


        # Get and send images from the text
        images = soup.find_all('img', src=True)
        # 处理图片，单独发送
        for img in images:
            await asyncio.to_thread(bot.send_photo, chat_id=target_chat_id, photo=img['src'])
        # 处理视频，单独发送
        videos = soup.find_all('video', src=True)
        for video in videos:
            video_url = video.get("src")
            await asyncio.to_thread(bot.send_video, chat_id=target_chat_id, video=video_url)

        pub_date_parsed = datetime.strptime(item["published"], "%a, %d %b %Y %H:%M:%S %Z")
        pub_date = pub_date_parsed.strftime("%Y-%m-%d %H:%M:%S")
        link = item["link"]

        message = (
            f"From {author}:\n\n"
            f"发布时间: {pub_date}\n\n"
            f"{description}\n\n"  
            f"{description_zh}\n\n" 
            f"链接: {link}"
        )

        # print(f"message to be sent is {message}")

        await asyncio.to_thread(
            bot.send_message, 
            chat_id=target_chat_id, 
            text=message,
            timeout=100,
            )  # Do not use parse_mode="HTML"

last_links = [None] * len(rss_list)
interval = 600  # 以秒为单位，根据需要调整RSS检查的频率

async def main():
    while True:
        for index, rss_source in enumerate(rss_list):
            latest_items = get_latest_twitter_updates(rss_source["url"], last_links[index])

            # print(f"latest_items length is {len(latest_items)}")


            if latest_items:
                last_links[index] = latest_items[0]["link"]
                await send_update_to_telegram(latest_items[::-1]) # Send tweets from oldest to newest
            
            await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.run(main())



