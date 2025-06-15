from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import subprocess
import datetime
import os

app = Flask(__name__)

recording_process = None
SAVE_DIR = os.path.expanduser("~/timelapse_output")
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route("/")
def index():
    global recording_process

    status = "idle"
    if recording_process and recording_process.poll() is None:
        status = "recording"

    try:
        files = sorted(os.listdir(SAVE_DIR), reverse=True)
    except OSError:
        files = []

    return render_template("index.html", status=status, files=files)

@app.route("/start", methods=["POST"])
def start_recording():
    global recording_process

    if recording_process and recording_process.poll() is None:
        return redirect(url_for('index'))

    try:
        duration_hours = int(request.form.get("duration_hr", 0))
        duration_minutes = int(request.form.get("duration_min", 0))
        duration_sec = (duration_hours * 3600) + (duration_minutes * 60)

        if duration_sec <= 0:
            return redirect(url_for('index'))

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"timelapse_{timestamp}.mp4"
        filepath = os.path.join(SAVE_DIR, filename)

        stream_url = "http://192.168.0.43:8080/?action=stream"
