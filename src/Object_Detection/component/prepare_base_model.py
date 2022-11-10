from Object_Detection import logger
from Object_Detection.entity.config_entity import Prepare_Base_Model_Config
from Object_Detection.entity.config_artifact import Prepare_Base_Model_Artifact
from Object_Detection.util.utility import read_yaml_file,write_yaml_file,read_file
from git.repo.base import Repo
from pathlib import Path
import os

class Prepare_Base_Model:
    def __init__(self,prepare_base_model_config:Prepare_Base_Model_Config):
        try:
            logger.info(f"{'>>'*20}prepare base model log started.{'<<'*20} ")
            self.prepare_base_model_config=prepare_base_model_config
        except Exception as e:
            raise e
    
    def clone_the_yolo(self,github_url:str,base_model_path):
        try:
            Repo.clone_from(url=github_url,to_path=base_model_path)
            logger.info("Successfully clone the YoloV5 github")
            base_model_path=os.path.join(base_model_path,"models","yolov5s.yaml")
            return Path(base_model_path)
        except Exception as e:
            raise e
    
    def update_yolo_model(self,base_model_path,update_model_path):
        try:
            content=read_file(file_path=base_model_path)
            logger.info("Successfully read the base yolo5s model")
            content["nc"]=6
            write_yaml_file(file_path=update_model_path,data=content)  # type: ignore
            logger.info(f"Successfully change the number of classes as 6 and content is {content}")
        except Exception as e:
            raise e
    
    def initiate_prepare_base_model(self)->Prepare_Base_Model_Artifact:
        try:
            github_url=self.prepare_base_model_config.Yolov5_github_url
            base_model_dir=self.prepare_base_model_config.base_model_dir
            base_model_path=self.clone_the_yolo(github_url=github_url,base_model_path=base_model_dir)  # type: ignore
            updated_model_name=self.prepare_base_model_config.updated_model_file_name
            updated_model_path=Path(os.path.join(os.path.dirname(base_model_path),updated_model_name))
            self.update_yolo_model(base_model_path=base_model_path,update_model_path=updated_model_path)
            prepare_base_model_artifact=Prepare_Base_Model_Artifact(base_model_path=base_model_path,
                                        updated_model_path=updated_model_path)
            return prepare_base_model_artifact
        except Exception as e:
            raise e
