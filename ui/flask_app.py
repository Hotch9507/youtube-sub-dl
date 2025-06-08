from flask import Flask, render_template, request, redirect, url_for, session
from core.subscriptions import get_subscriptions
from core.downloader    import start_downloads

from cookie import save_cookie, load_config

app = Flask(__name__)
app.secret_key = "replace-with-secure-key"

@app.context_processor
def inject_user():
    return dict(user=session.get("user"), config=load_config())

@app.route("/login")
def login():
    # 渲染一个上传 Cookie 的简单页面，或跳转 OAuth
    return render_template("config.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/subscriptions")
def subscriptions():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    channels = get_subscriptions(user.cookie_path)
    return render_template("subscriptions.html", channels=channels)

@app.route("/download/<channel_id>")
def download_channel(channel_id):
    user = session.get("user")
    start_downloads(channel_id, user.cookie_path)
    return redirect(url_for("downloads"))

@app.route("/downloads")
def downloads():
    # 假设有 get_active_jobs() 获取当前任务列表
    from core import get_active_jobs
    jobs = get_active_jobs()
    return render_template("downloads.html", jobs=jobs)

@app.route("/config/upload_cookie", methods=["POST"])
def upload_cookie():
    f = request.files["cookie_file"]
    save_cookie(f)
    session["user"] = {"name": "YouTubeUser", "cookie_path": save_cookie(f)}
    return redirect(url_for("subscriptions"))

@app.route("/config/set_proxy", methods=["POST"])
def set_proxy():
    proxy = request.form["proxy"]
    from cookie import save_proxy
    save_proxy(proxy)
    return redirect(url_for("config"))

@app.route("/config")
def config():
    return render_template("config.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
