from flask import Flask , render_template , request
from PIL import Image
import base64
import io
import re
import numpy as np
import json
import array
import tensorflow as tf
from keras.preprocessing.image import  array_to_img, img_to_array, load_img

app = Flask(__name__)

label = [0,1,2,3,4,5,6,7,9]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decode_image",methods=['POST'])
def getimage():

    model =  tf.keras.models.load_model("sequential_model-1.h5")
    #imgstr = re.search(r'base64,(.*)', request.get_data().decode('utf-8')).group(1)
    # image_bytes = io.BytesIO(base64.b64decode(imgstr))
    # im = Image.open(image_bytes)

    # arr = np.array(im)
    # arr = arr.reshape(28,28)
    # print(arr.shape)
    #print(request.args)
    nnInput = [];
    data = request.get_data()
    image = request.form.get("image")
    image = str(image)
    image = image.split(",")

    #Data URL
    # base64Image = request.form.get("base64")
    # imgstr      = re.search(r'base64,(.*)', base64Image).group(1)
    # #imgdata     = base64.b64decode(imgstr)
    # image       = np.fromstring(imgstr)
    # print(image)

    # height = int(request.form.get("height"))
    # width  = int(request.form.get("width"))


    


    for i in range(len(image)):
        nnInput.append(int(image[i]))
    nnInput = np.array(nnInput)
    image = nnInput.reshape(280,280,-1)
    image = image[:,:,0:1]
    #print(nnInput.reshape((28,28,1)).shape)
    #nnInput = np.resize(nnInput , (280,280,-1))
    #print(nnInput.shape)
    image = tf.keras.preprocessing.image.array_to_img(image)
    image.thumbnail((28,28))
    image = np.array(image)
    image = image.reshape(-1,784)
    x = (image - 128.0) / 128.0
    # image = img_to_array(image)  
    # x = (image - 128.0) / 128.0
    # x = x[:,:,0:1]
    # x = x.reshape(-1,784)
    

    # image = np.fromfile("./3.png")
    # print(image.shape)
    # image = np.resize(image,(28,28))
    # image = image.reshape(-1,784)
    #print(image.shape)

     
    # nnInput = array.array('f',[784])

    
    #image = imageDataToGrayscale(image,height,width)

    np.save("image.png",nnInput.reshape(280,280,-1))


    

    # for y in range(28):
    #     for x in range(28):   
    #         mean = 0
    #         for v in range(10):
    #             for h in range(10):
    #                 mean = mean + image[y*10 + v][x*10 + h]
    #         mean = (1 - mean / 100); # average and invert
    #         nnInput[x*28+y] = (mean - .5) / .5
    # print(nnInput)

    

        
    #print(image.shape)
    predict = model.predict(x)
    print(np.argmax(predict))
    print(predict)

    return "None"
  

def imageDataToGrayscale(imgData, height , width):
    grayscaleImg = [];
    for y in range(height):
        grayscaleImg[y];
        for x in range(width):
            offset = y * 4 * width + 4 * x;
            alpha = imgData[offset+3];
            #weird: when painting with stroke, alpha == 0 means white;
            #alpha > 0 is a grayscale value; in that case I simply take the R value
            if alpha == 0 : 
                imgData[offset] = 255;
                imgData[offset+1] = 255;
                imgData[offset+2] = 255;
        imgData[offset+3] = 255;
        #simply take red channel value. Not correct, but works for
        #black or white images.
        grayscaleImg[y][x] = imgData[y*4*width + x*4 + 0] / 255;
    return grayscaleImg;
      
    """
    if (request.data != None):
        image = np.array(request.data)
        print(image.shape)
    """
    return "Image comming" 
if __name__ == "__main__":
    app.run(port=8890 , debug=True) 




 #import base64 
 #image = open('deer.gif', 'rb') 
 #open binary file in read mode image_read = image.read() 
 # image_64_encode = base64.encodestring(image_read) 
