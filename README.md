# Kidney-Disease-Classification

## Workflows 

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update pipeline
7. Update the main.py
8. Update the dvc.yaml
9. app.py

# How to run?

### Steps:

### Step 1 - Create a conda enviroment after opening the repository

```bash
conda create -n CnnClassifier python==3.10.4 -y
```

```bash
conda activate CnnClassifier
```

### Step 2 - install the requirements
```bash
pip install -r requirements.txt
```
### MLFlow

### cmd
- mlflow ui

### dagshub

[dagshub] (https://dagshub.com/)
MLFLOW_TRACKING_URI=https://dagshub.com/DivyanshKushwaha/Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=DivyanshKushwaha \
MLFLOW_TRACKING_PASSWORD=918ce4fd5758d0e748f225fb5c24cacbbec65e84 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI = https://dagshub.com/DivyanshKushwaha/Kidney-Disease-Classification.mlflow
export MLFLOW_TRACKING_USERNAME = DivyanshKushwaha
export MLFLOW_TRACKING_PASSWORD = ":***ce4fd5758d0e***f***fb5c24cacbbec**e**"

```