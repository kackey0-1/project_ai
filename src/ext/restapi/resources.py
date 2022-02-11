import os

import werkzeug
from flask import jsonify
from flask_restful import Resource, reqparse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from werkzeug.utils import secure_filename

classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
image_size = 28
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
# TODO temporarily comment out
# model = load_model("./src/ml_models/model.h5")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


class ImageAiResource(Resource):
    def post(self):
        """
        Creates a new product.

        # curl -XPOST localhost:5000/api/v1/product/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        parse = reqparse.RequestParser()
        parse.add_argument(
            "file", type=werkzeug.datastructures.FileStorage, location="files"
        )
        args = parse.parse_args()
        file = args["file"]
        if file.filename == "":
            raise InvalidAPIUsage("file not found")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            filepath = filename
            img = image.load_img(
                filepath, color_mode="grayscale", target_size=(image_size, image_size)
            )

            img = image.img_to_array(img)
            data = np.array([img])
            # 変換したデータをモデルに渡して予測
            # result = model.predict(data)[0]
            # predicted = result.argmax()
            # predict_answer = classes[predicted]
            predict_answer = 1
            os.remove(filename)
            return jsonify({"answer": predict_answer})


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
