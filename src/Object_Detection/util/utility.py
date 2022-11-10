from Object_Detection import logger
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
import os
import yaml

@ensure_annotations
def read_yaml_file(file_path:Path)->ConfigBox:

    """ 
    reads yaml file and returns
    Args:
          file_path(str): path like input
    Raises:
          Value Error: if yaml file is empty
          e: empty file
    Returns:
          ConfigBox: ConfigBox type """
    try:
        with open(file_path,"r") as yaml_file:
            data=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{file_path} is loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def write_yaml_file(file_path,data):
    try:
        with open(file_path,"w") as file:
            yaml.dump(data,file)
    except Exception as e:
        raise e
