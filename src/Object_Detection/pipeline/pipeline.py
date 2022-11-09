from Object_Detection import logger
from Object_Detection.config.configuration import Configuration
from Object_Detection.entity.config_artifact import Data_Ingestion_Artifact
from Object_Detection.component.data_ingestion import Data_Ingestion

class pipeline:
    def __init__(self,config:Configuration) -> None:
        self.config=config
    
    def start_data_ingestion(self):
        try:
            data_ingestion=Data_Ingestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise e
    
    def run_pipeline(self):
        try:
            self.start_data_ingestion()
        except Exception as e:
            raise e