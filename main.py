from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
         trainingPipelineConfig=TrainingPipelineConfig()
         dataingestionconfig=DataIngestionConfig(trainingPipelineConfig)
         data_ingestion=DataIngestion(dataingestionconfig)
         logging.info("initiate the data ingestion")
         dataingestionartifact=data_ingestion.initiate_data_ingestion()
         print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)