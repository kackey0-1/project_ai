import os
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
image_size = 28
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
# 学習済みモデルをロード
model = load_model("./models/model.h5")
# app = Flask(__name__, static_folder="../ui/dist/static", template_folder="../ui/dist")
app = Flask(__name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
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
                filepath, grayscale=True, target_size=(image_size, image_size)
            )
            img = image.img_to_array(img)
            data = np.array([img])
            # 変換したデータをモデルに渡して予測する
            result = model.predict(data)[0]
            predicted = result.argmax()
            predict_answer = "これは " + classes[predicted] + " です"
            return render_template("index.html", answer=predict_answer)

    return render_template("index.html", answer="")


if __name__ == "__main__":
    app.run()
