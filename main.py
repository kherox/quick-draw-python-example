from flask import Flask, render_template, request
from PIL import Image
import base64
import io
import re
import numpy as np
import json
import array
import tensorflow as tf
from keras.preprocessing.image import array_to_img, img_to_array, load_img

import cv2

app = Flask(__name__)

label = [0, 1, 2, 3, 4, 5, 6, 7, 9]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/decode_image", methods=['POST'])
def getimage():

    model = tf.keras.models.load_model("numeric_classification_model.h5")

    base64Image = request.form.get("base64")
    imgstr = re.search(r'base64,(.*)', base64Image).group(1)
    imgdata = base64.b64decode(imgstr)
   # image = np.fromstring(imgstr)

    with open("image.png", "wb") as img:
        img.write(imgdata)

    image = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
    img_resize = cv2.resize(image, (28, 28))
    # x = (img_resize - 128) / 128
    # #y = x.reshape(784)

    y = img_resize.reshape(-1, 784)
    y = y.astype(float)

    predict = model.predict(y)
    print(np.argmax(predict))
    print((predict))

    return "None"


def imageDataToGrayscale(imgData, height, width):
    grayscaleImg = []
    for y in range(height):
        grayscaleImg[y]
        for x in range(width):
            offset = y * 4 * width + 4 * x
            alpha = imgData[offset+3]
            # weird: when painting with stroke, alpha == 0 means white;
            # alpha > 0 is a grayscale value; in that case I simply take the R value
            if alpha == 0:
                imgData[offset] = 255
                imgData[offset+1] = 255
                imgData[offset+2] = 255
        imgData[offset+3] = 255
        # simply take red channel value. Not correct, but works for
        # black or white images.
        grayscaleImg[y][x] = imgData[y*4*width + x*4 + 0] / 255
    return grayscaleImg

    """
    if (request.data != None):
        image = np.array(request.data)
        print(image.shape)
    """
    return "Image comming"


if __name__ == "__main__":
    app.run(port=8080, debug=True)

 #import base64
 #image = open('deer.gif', 'rb')
 # open binary file in read mode image_read = image.read()
 # image_64_encode = base64.encodestring(image_read)
