import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig


#Use decorator: only need to define variables. 
#Use init constructor: define, other functions in class.

@dataclass  
#saves dataingestion o/p in artifacts folder.
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") 
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #all paths in DIConfig are saved here.
    
    def initiate_data_ingestion(self): #easiest way to read dataset from source.
        logging.info("Entered data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe.")

            #create artifact folders: train, test, data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #save in raw_data_path
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e,sys)

#Saving the necessary returned values from all components.        
if __name__ =="__main__":
    obj= DataIngestion()
    train_data, test_data= obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
