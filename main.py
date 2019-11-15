from flask import Flask, request
import base64
import re
import numpy as np
import tensorflow as tf

import cv2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decode_image", methods=['POST'])
def getimage():

    model = tf.keras.models.load_model("numeric_classification_model.h5")

    base64Image = request.form.get("base64")
    imgstr = re.search(r'base64,(.*)', base64Image).group(1)
    imgdata = base64.b64decode(imgstr)

    with open("image.png", "wb") as img:
        img.write(imgdata)

    image = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
    img_resize = cv2.resize(image, (28, 28))

    y = img_resize.reshape(-1, 784)
    y = y.astype(float)

    predict = model.predict(y)
    print(np.argmax(predict))
    print((predict))

    return "None"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
