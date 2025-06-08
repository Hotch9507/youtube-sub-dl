# core/subscriptions.py
import os
import tomli
from yt_dlp import YoutubeDL

def load_config():
    """读取项目根目录下的 config.toml"""
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    cfg_path = os.path.join(base, "config.toml")
    with open(cfg_path, "rb") as f:
        return tomli.load(f)

def get_subscriptions_status():
    cfg = load_config()
    cookies = cfg["general"]["cookies_file"]
    proxy = cfg["general"].get("proxy")

    ydl_opts = {
        "quiet": True,
        "ignoreerrors": True,
        "flat_playlists": True,
        "dump_single_json": True,
        "cookiefile": cookies,
    }

    if proxy:
        ydl_opts["proxy"] = proxy

    url = "https://www.youtube.com/feed/channels"

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    # info["entries"] 是一个列表，每项含: title, url, id
    channels = []
    for entry in info.get("entries", []):
        if not entry:
            continue
        channels.append({
            "name": entry.get("title"),
            "url": f"https://www.youtube.com/channel/{entry.get('id')}",
            # total/downloaded/status 暂时留空，后续再填
            "total": "--",
            "downloaded": "--",
            "status": "待查询",
        })
    # Debug
    print(f">>> fetched {len(channels)} subscriptions")
    return channels
