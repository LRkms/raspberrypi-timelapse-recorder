# 🎥 Timelapse Flask Recorder

A lightweight Flask-based web interface for scheduling and recording MJPG-streamer webcam streams as timelapse `.mp4` files on a Raspberry Pi.

## 💡 Features

- 📷 Start/stop video recording from webcam stream
- ⏱️ Schedule recordings by duration (hours + minutes)
- 💾 Saves videos to local disk
- 🌐 Web UI accessible via browser
- 🔁 Systemd support for persistent background running
- 📥 Download recorded videos directly from UI

## 📦 Requirements

- Raspberry Pi (tested on Pi 4)
- Python 3.7+
- `ffmpeg`
- `mjpg-streamer` running at `http://<IP>:8080/?action=stream`

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/timelapse-flask-app.git
cd timelapse-flask-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
