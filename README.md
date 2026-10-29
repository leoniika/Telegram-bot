# Telegram bot with python

[English](#Induction) | [فارسی](#پیشگفتار)

## Induction

A simple Telegram bot that allows users to send anonymous messages to the bot owner. Users can send text messages, pictures, and files without their Telegram identity being shared directly with the owner.

## Features

- **Anonymous Messaging:** Users can send messages to the bot owner anonymously.
- **Reply System:** The owner of the bot can reply directly to received messages, and the bot sends the response to the original sender. (By copying the messages, not forwarding.)
- **Message Tracking:** The bot uses SQLite to store the connection between received messages and their senders, allowing replies to reach the correct user.
- **Data Storage:** Message tracking information is saved in a local database. (SQLite in this project.)

## How It Works

1. User starts the bot using `/start`.
2. User sends a text message, picture, or file.
3. Bot copies and send the message to the owner and saves its ID and the sender's chat ID in the database.
4. Owner replies to the received message directly in Telegram.
5. Bot uses the saved information to deliver the reply to the original sender.

## Libraries Used

- **python-telegram-bot** — Handles Telegram messages and bot conversations.
- **SQLite** — Stores message and sender information.
- **python-dotenv** — Loads configuration from environment variables.

## Configuration

The bot requires the following environment variables:

- `BOT_TOKEN` — The Telegram bot token.
- `OWNER_ID` — The Telegram user ID of the bot owner.
- `DATA_AIR` — Optional directory for storing the database. If not specified, the project directory is used.

Keep your bot token private and never commit your `.env` file to GitHub.

## Running the Bot

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Configure the environment variables, then run:

```bash
python Bot.py
```

The bot will start listening for Telegram messages.

## My Goal by doing this project

This project was an exercise for me to work with Python, SQLite and Git, acting as an initial stepping stone for the start of my workflow. 👩🏻‍💻🎀

---

# بات تلگرام با پایتون

## پیشگفتار

یک ربات ساده که به کاربرها اجازه میده که به سازنده ی ربات به شکل ناشناس پیام ارسال کنن. کابرها میتونن متن، عکس و فایل به ربات ارسال کنن بدون اینکه اسم فرستنده مستقیما برای سازنده ی ربات نمایش داده بشه.

## ویژگی ها

- **مکالمه ی ناشناس:** کاربرها میتونن به شکل ناشناس به سازنده ی ربات پیام ارسال کنن.
- **قابلیت پاسخ دادن به پیام:** سازنده ی ربات مستقیما میتونه به پیام فرستنده پاسخ بده، ربات هم پیام پاسخ رو به فرسنده ی درست ارسال میکنه. (به شکل کپی و ارسال پیام. ربات امکان فوروارد کردن پیام رو نداره.)
- **پیگیری پیام:** ربات با استفاده از SQLite ارتباط بین پیام ها و فرستنده هاشون رو نگه میداره و اجازه میده که پیام های پاسخ از سمت سازنده به فرستنده ی درست اون پیام برسن.
- **ذخیره داده ها:** داده های ردیابی پیام به شکل یک پایگاه داده ی محلی ذخیره میشن. (توی این پروژه پایگاه داده SQLite هستش.)

## کارکرد ربات

1. کاربر با پیام `/start` ربات رو شروع میکنه.
2. کاربر پیامی در قالب متن، عکس و یا فایل ارسال میکنه.
3. ربات پیام ارسال شده رو کپی کرده و به سازنده ارسال میکنه. در همین حین ربات آیدی پیام و آیدی فرستنده رو در پایگاه دادش ذخیره میکنه.
4. سازنده ی ربات به پیام ارسال شده مستقیم جواب میده.
5. ربات با استفاده از داده های داخل پایگاه داده فرستنده ی پیام رو پیگیری میکنه و پاسخ سازنده رو بهش ارسال میکنه.

## کتابخانه های استفاده شده

- **python-telegram-bot** — برای مدیریت پیام های تلگرام و مکالمه های ربات.
- **SQLite** — برای ذخیره ی داده ی پیام و فرستنده.
- **python-dotenv** — برای بالا آوردن تنظیمات پیکربندی از متغیر های محلی.

## پیکربندی

ربات به این متغیر های محلی نیاز داره:

- `BOT_TOKEN` — توکن ربات تلگرامی.
- `OWNER_ID` — آیدی تلگرام سازنده ی ربات.
- `DATA_AIR` — مکان انتخابی برای نگهداری پایگاه داده. اگه مشخص نشه پایگاه داده داخل فولدری که پروژه داخلش قرار داره، ساخته میشه.

توکن ها داده های مهمی هستن و باید به شکل خصوصی ذخیره بشن و فایل `.env` نباید همراه پروژه جایی منتشر بشه.

## اجرای ربات

برای اجرای ربات باید وابستگی های مورد نیاز رو نصب کنید:

```bash
pip install -r requirements.txt
```

پیکربندی متغیر های محلی انجام میشه, بعد اجرا کنین:

```bash
python Bot.py
```

ربات الان فعال میشه و به پیام های تلگرام گوش میده.

## هدفم از انجام این پروژه

این پروژه تمرینی بود برای من که از گیت، پایتون و SQLite استفاده کنم برای شروعی برای روند کد زدنم. 👩🏻‍💻🎀
