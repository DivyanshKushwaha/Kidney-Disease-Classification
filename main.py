from src.CnnClassifier import logger
from src.CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CnnClassifier.pipeline.stage_03_training_model import ModelTraininigPipeline


STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = ModelTraininigPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e