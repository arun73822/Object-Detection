from Object_Detection.pipeline.data_ingestion import pipeline
from Object_Detection.config.configuration import Configuration

pipe=pipeline(config=Configuration())

if __name__=='__main__':
    pipe.run_pipeline()