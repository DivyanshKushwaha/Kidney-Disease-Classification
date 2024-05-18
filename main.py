from src.CnnClassifier import logger
from src.CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CnnClassifier.pipeline.stage_03_training_model import ModelTraininigPipeline
from src.CnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os
os.environ['PYTHONIOENCODING'] = 'UTF-8'



STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj1 = DataIngestionTrainingPipeline()
    obj1.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj2 = PrepareBaseModelTrainingPipeline()
    obj2.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj3 = ModelTraininigPipeline()
    obj3.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj4 = EvaluationPipeline()
    obj4.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e