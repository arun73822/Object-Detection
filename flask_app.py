from Object_Detection.constants import *
from flask import Flask,flash,redirect,request,render_template,url_for,send_from_directory
from werkzeug.utils import secure_filename
#from Daily_runs import func,func_2
from PIL import Image
import numpy as np
import torch
import cv2
import os
import matplotlib.pyplot as plt

UPLOAD_FOLDER="static/images"
OUTPUT_FOLDER="static/output"
ALLOWED_EXTENCTIONS={"jpg","png","jpeg"}

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route("/",methods=["POST","GET"])
def upload_file():
    if request.method=="POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file=request.files["file"]
        if file.filename=="":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            image = [i for i in os.listdir(UPLOAD_FOLDER) if i.endswith('.jpg' or '.png' or '.jpeg')][-1]
            return render_template('image.html', user_image = image)
            #return redirect(url_for('upload_file', name=filename))
    return render_template("upload.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/predict', methods=['POST','GET'])
def predict():
   image_file_name = [i for i in os.listdir(UPLOAD_FOLDER) if i.endswith('.jpg' or '.png' or '.jpeg')][-1]
   image=os.path.join(UPLOAD_FOLDER,image_file_name)
   image=Image.open(image)
   img=image.resize((416,640))
   img_array=np.array(img)
   result=model(img_array)
   result.save(save_dir="static/output",exist_ok=True)
   result.show()
   image = [i for i in os.listdir(OUTPUT_FOLDER) if i.endswith('.jpg' or '.png' or '.jpeg')][-1]
   return render_template("output.html", user_image = image)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENCTIONS

if __name__=="__main__":
    model=torch.hub.load(MODEL_PATH,"custom",MODEL_WEIGHTS_PATH,source="local")
    app.run()
