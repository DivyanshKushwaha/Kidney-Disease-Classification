from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.training_model import Training
from src.CnnClassifier import logger
import os


STAGE_NAME = "Training"


class ModelTraininigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__=='__main__':
    try:
        logger.info(f"******************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelTraininigPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e