from yt_dlp import YoutubeDL
from config import get_config  # 我们之前写的读取toml配置的函数

def download_video(url, channel_name):
    config = get_config()
    proxy = config.get("general", {}).get("proxy", None)
    download_path = config.get("general", {}).get("download_path", "downloads")

    ydl_opts = {
        "proxy": proxy,
        "outtmpl": f"{download_path}/{channel_name}/%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "cookies": config["general"]["cookies_file"],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
