#
# Copyright (C) 2024 by Moonshining1@Github, < https://github.com/Moonshining1 >.
#
# This file is part of < https://github.com/Moonshining1/ANNIE-MUSIC > project,
# and is released under the "MIT License".
# Please see < https://github.com/Moonshining1/ANNIE-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#
import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get it from my.telegram.org

API_ID = int(getenv("API_ID", "24880308"))

API_HASH = getenv("API_HASH", "fce3dc86e231613c5e0e164cdf8f1ca9")


## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7597057529:AAG4TvzqXvlT3hSxddwXatGGvdmkyBcdlm0")

BOT_USERNAME = getenv("BOT_USERNAME", "snowy_x_musicbot")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "18000")
)  # Remember to give value in Seconds


# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "3000")
)  # Remember to give value in Minutes


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "True",
)

# Fill True if you want to load extra plugins


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/itzarjuna1/Snowyxannie-MUSIC", 
)
# iss link ko mt remove krna harmai ye management wlaa hai isme hi sub code hai management ke liye..
# Fill here the external plugins repo where plugins that you want to load


EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

# Your folder name in your extra plugins repo where all plugins stored


# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000")
)  # Remember to give value in Minutes


# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002643544937"))


# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "7926944005").split())
)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Moonshining1/ANNIE-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    "",
)

# Token allow for access youtube songs. [ True = use token data, False = use cookies ]
TOKEN_ALLOW = os.getenv("TOKEN_ALLOW", "False")

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting.
AUTO_GCAST = os.getenv("AUTO_GCAST", "on")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support"
)  # Example:- https://t.me/VIP_CREATORS
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/dark_knight_support"
)  # Example:- https://t.me/TG_FRIENDSS

SUPPORT_CHAT = getenv(
    "SUPPORT_GROUP", "https://t.me/dark_knight_support"
)  # Example:- https://t.me/Grandxmasti
# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 1800)
)  # Remember to give value in Seconds


# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorize command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))


# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/itzarjuna1/snowyxanniemusic-music")


# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", "False")


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @VIPStringBot
STRING1 = getenv("STRING_SESSION", "AQF7pLQAojetQZtb9UXJs4lyP3JPmWAk-kFniZR4cciu1Lh5svG19MFQ0uZjSxH0HwLQczOgfc-CZn_TAdjEQTOUp7wumUntlr7GdPFTyL5IT7oI0pExGSgu8cXb9UJ6lozm12nW3jjQ7kfP4IZJPLtzbZ5fp0Qc8Z72k09EavrM_nmddtYjXsETOxBez2j3IC6kiFHQ2jQB3RvhTFvi6cVSXytwU_pXEk2rb8WqwttXEJUp5ar4ZOSgplWfI7AY1xpM-FLTUTgjAO3ddPCF8ii9OSBfmz4Dr-pX26x8bQt_7CMqcyUZnnD7o6-xXRy2AJoM2pUAOLlVgpryPSsdVhQ5hMkMIQAAAAHoG-_JAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

                                          
### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "ANNIElogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/443htj.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/91533956c91d0fd7c9f20.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://telegra.ph/file/de1db74efac1770b1e8e9.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://telegra.ph/file/8234d704952738ebcda7f.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://telegra.ph/file/8d02ff3bde400e465219a.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://telegra.ph/file/7645d1e04021323c21db9.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://telegra.ph/file/b7758d4e1bc32aa9fb6ec.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://telegra.ph/file/60ed85638e00df10985db.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )


if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )


if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "https://telegra.ph/file/91533956c91d0fd7c9f20.jpg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://telegra.ph/file/de1db74efac1770b1e8e9.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://telegra.ph/file/8234d704952738ebcda7f.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://telegra.ph/file/7645d1e04021323c21db9.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://telegra.ph/file/8d02ff3bde400e465219a.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
