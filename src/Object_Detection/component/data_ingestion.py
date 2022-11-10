from zipfile import ZipFile
from Object_Detection.entity.config_entity import Data_Ingestion_Config
from Object_Detection.entity.config_artifact import Data_Ingestion_Artifact
from Object_Detection import logger
from six.moves import urllib
from zipfile import ZipFile
import shutil
import os
from pathlib import Path

class Data_Ingestion:

    def __init__(self,data_ingestion_config:Data_Ingestion_Config ):
        try:
            logger.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise e

    def download_housing_data(self,) -> Path:
        try:
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            os.makedirs(raw_data_dir,exist_ok=True)

            housing_file_name = os.path.basename(download_url)

            raw_data_path = os.path.join(raw_data_dir, housing_file_name)

            logger.info(f"Downloading file from :[{download_url}] into :[{raw_data_path}]")
            urllib.request.urlretrieve(download_url, raw_data_path)  # type: ignore
            logger.info(f"File :[{raw_data_path}] has been downloaded successfully.")
            return Path(raw_data_path)

        except Exception as e:
            raise e

    def extract_zip_file(self,raw_data_path:Path):
        try:
            extracted_data_dir = self.data_ingestion_config.extracted_data_dir

            #if os.path.exists(extracted_data_dir):
                #os.remove(extracted_data_dir)

            os.makedirs(extracted_data_dir,exist_ok=True)

            logger.info(f"Extracting zip file: [{raw_data_path}] into dir: [{extracted_data_dir}]")
            with ZipFile(raw_data_path) as file:
                file.extractall(extracted_data_dir)
            logger.info(f"Extraction completed")
            return extracted_data_dir
        except Exception as e:
            raise e
    
    def get_training_and_testing_data(self,extracted_path,train_data_path,test_data_path):
        try:
            train_path=Path(os.path.join(extracted_path,"train"))
            test_path=Path(os.path.join(extracted_path,"test"))
            shutil.copytree(train_path,train_data_path)
            shutil.copytree(test_path,test_data_path)
            return train_path,test_path
        except Exception as e:
            raise e
    
    def initiate_data_ingestion(self)->Data_Ingestion_Artifact:
        try:
            raw_data_path= self.download_housing_data()
            extracted_data_path=self.extract_zip_file(raw_data_path=raw_data_path)
            train_data_path,test_data_path=self.get_training_and_testing_data(
                                        extracted_path=extracted_data_path,
                                        train_data_path=self.data_ingestion_config.ingested_train_dir,
                                        test_data_path=self.data_ingestion_config.ingested_test_dir)

            data_ingestion_artifact=Data_Ingestion_Artifact(train_file_path=train_data_path,
                                                            test_file_path=test_data_path)
            return data_ingestion_artifact
        except Exception as e:
            raise e