from Object_Detection.constants import *
import streamlit as st
from streamlit_tensorboard import st_tensorboard
import numpy as np
from PIL import Image
import torch

"""                       SIGN LANGUAGE OBJECT DETECTION     

"""
#model=torch.hub.load(r"C:/Users/arun7/Desktop/projects/Computer_Vision/Object_Detection/src/Object_Detection/artifact_dir/prepare_base_model/base_model","custom",r"C:/Users/arun7/Desktop/projects/Computer_Vision/Object_Detection/src/Object_Detection/artifact_dir/prepare_base_model/base_model/runs/train/yolov5s_results/weights/best.pt",source="local")
model=torch.hub.load(MODEL_PATH,"custom",MODEL_WEIGHTS_PATH,source="local")
upload_image=st.file_uploader("Choose a File")
st_tensorboard(logdir=TENSORBOARD_LOG_DIR,port=6006,width=950)
if upload_image is not None:
    image=Image.open(upload_image)
    img=image.resize((416,640))
    img_array=np.array(img)
    #img_array=np.expand_dims(img_array,axis=0)
    result=model(img_array)
    result.show()

    if dict(result.pandas().xyxy[0])["class"][0]==0 and dict(result.pandas().xyxy[0])["name"][0]=="Hello":
        st.image(image,caption="Actual:Hello")
        st.image(img_array,caption="Predicted:Hello")

    elif dict(result.pandas().xyxy[0])["class"][0]==1 and dict(result.pandas().xyxy[0])["name"][0]=="IloveYou":
        st.image(image,caption="Actual:I LOVE YOU")
        st.image(img_array,caption="Predicted:I LOVE YOU")
    
    elif dict(result.pandas().xyxy[0])["class"][0]==2 and dict(result.pandas().xyxy[0])["name"][0]=="No":
        st.image(image,caption="Actual:NO")
        st.image(img_array,caption="Predicted:NO")
    
    elif dict(result.pandas().xyxy[0])["class"][0]==3 and dict(result.pandas().xyxy[0])["name"][0]=="Please":
        st.image(image,caption="Actual:PLEASE")
        st.image(img_array,caption="Predicted:PLEASE")
    
    elif dict(result.pandas().xyxy[0])["class"][0]==4 and dict(result.pandas().xyxy[0])["name"][0]=="Thanks":
        st.image(image,caption="Actual:THANKS")
        st.image(img_array,caption="Predicted:THANKS")
    
    elif dict(result.pandas().xyxy[0])["class"][0]==5 and dict(result.pandas().xyxy[0])["name"][0]=="Yes":
        st.image(image,caption="Actual:YES")
        st.image(img_array,caption="Predicted:YES")
