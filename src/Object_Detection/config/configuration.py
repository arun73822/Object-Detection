from Object_Detection import logger
from Object_Detection.entity.config_entity import Training_Pipeline_Config,Data_Ingestion_Config,Prepare_Base_Model_Config
from Object_Detection.util.utility import read_yaml_file
from Object_Detection.constants import *
from pathlib import Path

class Configuration:
    
    def __init__(self,config_file_path=CONFIG_FILE_PATH):
        try:
            self.config_info=read_yaml_file(file_path=Path(config_file_path))
            self.training_pipeline_config=self.get_training_pipeline_config()
        except Exception as e:
            raise e

    def get_training_pipeline_config(self)->Training_Pipeline_Config:
        try:
            training_pipeline_config_info=self.config_info.training_pipeline_config
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_config_info.pipeline_name,
                training_pipeline_config_info.artifact_dir)

            training_pipeline_config = Training_Pipeline_Config(artifact_dir=Path(artifact_dir))

            logger.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise e

    def get_data_ingestion_config(self) -> Data_Ingestion_Config:
        try:
            data_ingestion_config_info = self.config_info.data_ingestion_config 
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir, data_ingestion_config_info.data_ingestion_dir
            )
            dataset_download_url = data_ingestion_config_info.dataset_download_url
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir, data_ingestion_config_info.raw_data_dir
            )
            extracted_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config_info.extracted_data_dir,
            )
            traning_data_dir = os.path.join(data_ingestion_artifact_dir,
                                            data_ingestion_config_info.ingested_train_data_dir)

            testing_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config_info.ingested_test_data_dir
            )

            data_ingestion_config = Data_Ingestion_Config(
                data_ingestion_dir=Path(data_ingestion_artifact_dir),
                dataset_download_url=dataset_download_url,
                raw_data_dir=Path(raw_data_dir),
                extracted_data_dir=Path(extracted_data_dir),
                ingested_train_dir=Path(traning_data_dir),
                ingested_test_dir=Path(testing_data_dir)
            )
            logger.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise e
    
    def get_prepare_base_model_config(self)->Prepare_Base_Model_Config:
        try:
            artifact_dir=self.training_pipeline_config.artifact_dir
            prepare_base_model_config_info=self.config_info.prepare_base_model_config  # type: ignore
            prepare_base_model_config_dir=os.path.join(artifact_dir,
                                            prepare_base_model_config_info.prepare_base_model_dir)
            base_model_dir=os.path.join(prepare_base_model_config_dir,
                                        prepare_base_model_config_info.base_model_dir)
            base_model_file_name=prepare_base_model_config_info.base_model_file_name
            updated_model_dir=os.path.join(prepare_base_model_config_dir,
                                           prepare_base_model_config_info.updated_model_dir)
            updated_model_file_name=prepare_base_model_config_info.updated_model_file_name
            updated_model_file_path=os.path.join(updated_model_dir,updated_model_file_name)
            params_number_of_classes=NUMBER_OF_CLASSES
            github_url=prepare_base_model_config_info.Yolov5_github_url
            prepare_base_model_config=Prepare_Base_Model_Config(
                                                prepare_base_model_dir=Path(prepare_base_model_config_dir),
                                                base_model_dir=Path(base_model_dir),
                                                base_model_file_name=base_model_file_name,
                                                updated_model_dir=Path(updated_model_dir),
                                                updated_model_file_name=updated_model_file_name,
                                                updated_model_file_path=Path(updated_model_file_path),
                                                params_number_of_classes=params_number_of_classes,
                                                Yolov5_github_url=github_url)
            logger.info(f"Prepare Model Config: {prepare_base_model_config}")
            return prepare_base_model_config
        except Exception as e:
            raise e