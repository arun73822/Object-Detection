from Object_Detection import logger
from Object_Detection.config.configuration import Configuration
from Object_Detection.entity.config_artifact import Data_Ingestion_Artifact
from Object_Detection.component.data_ingestion import Data_Ingestion

STAGE_NAME="Data_Ingestion"

def main():
    config=Configuration()
    data_ingestion_config=config.get_data_ingestion_config()
    data_ingestion=Data_Ingestion(data_ingestion_config=data_ingestion_config)
    data_ingestion.initiate_data_ingestion()

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e