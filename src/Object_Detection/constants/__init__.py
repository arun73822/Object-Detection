from pathlib import Path
import os 


ROOT_DIR=os.getcwd()
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
NUMBER_OF_CLASSES=6
MODEL_PATH=r"C:/Users/arun7/Desktop/projects/Computer_Vision/Object_Detection/src/Object_Detection/artifact_dir/prepare_base_model/base_model"
MODEL_WEIGHTS_PATH=os.path.join(MODEL_PATH,"runs","train","yolov5s_results","weights","best.pt")
TENSORBOARD_LOG_DIR="src/Object_Detection/artifact_dir/prepare_base_model/base_model/runs/train/yolov5s_results"