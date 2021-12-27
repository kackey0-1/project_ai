import os
from flask import Flask, request, redirect, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
image_size = 28
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
# 学習済みモデルをロード
model = load_model("./models/model.h5")
# app = Flask(__name__, static_folder="../ui/dist/static", template_folder="../ui/dist")
app = Flask(__name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルがありません")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("ファイルがありません")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            # 受け取った画像を読み込み、np形式に変換
            img = image.load_img(
                filepath, color_mode="grayscale", target_size=(image_size, image_size)
            )
            img = image.img_to_array(img)
            data = np.array([img])
            # 変換したデータをモデルに渡して予測
            result = model.predict(data)[0]
            predicted = result.argmax()
            predict_answer = "これは " + classes[predicted] + " です"
            return render_template("index.html", answer=predict_answer)

    return render_template("index.html", answer="")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        raise InvalidAPIUsage("file not found")
    file = request.files["file"]
    if file.filename == "":
        raise InvalidAPIUsage("file not found")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        img = image.load_img(
            filepath, color_mode="grayscale", target_size=(image_size, image_size)
        )
        img = image.img_to_array(img)
        data = np.array([img])
        # 変換したデータをモデルに渡して予測
        result = model.predict(data)[0]
        predicted = result.argmax()
        predict_answer = "これは " + classes[predicted] + " です"
        print(predict_answer)
        return jsonify({"answer": predict_answer})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
