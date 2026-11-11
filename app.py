from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(BASE_DIR), static_folder=None)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/juman")
def profile_image():
    # ضع الصورة بجانب app.py وسمّها juman.jpg
    image = BASE_DIR / "juman.jpg"
    if not image.exists():
        abort(404, description="ضع صورة juman.jpg بجانب app.py")
    return send_from_directory(BASE_DIR, "juman.jpg")

@app.get("/song")
def song():
    # ضع ملف الأغنية بجانب app.py وسمّه song.mp3
    audio = BASE_DIR / "song.mp3"
    if not audio.exists():
        abort(404, description="ملف الأغنية song.mp3 غير موجود")
    return send_from_directory(BASE_DIR, "song.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)), debug=False)
