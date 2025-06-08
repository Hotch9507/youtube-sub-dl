import threading
from flask import Flask, render_template, redirect, url_for
from core.subscription import get_subscriptions_status, download_all_subscriptions

app = Flask(__name__)

@app.route("/")
def index():
    print(">>> hit index route <<<")
    subscriptions = get_subscriptions_status()
    return render_template("index.html", subscriptions=subscriptions)

@app.route("/download_all")
def trigger_download():
    threading.Thread(target=download_all_subscriptions).start()
    return redirect(url_for('index'))


@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/logs")
def logs():
    return render_template("logs.html")
