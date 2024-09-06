import os
from pathlib import Path  ## Automatically handles paths correctly for different OS
import logging

# Creating a list of files
list_of_files = [
    
    ".github/workflows/.gitkeep", # indise this .github we will write all the workflows
    "src/__init__.py", # we are creating src files it represents the source code
    "src/components/__init__.py", # indise this src we are creating another file know as components it represents all components stages of the pipeline
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit__init__.py", # Here we are performing unit testing it is only performed for an individual component
    "tests/integration/__init__.py", # Here we are using integration test it will perform for all unites and all the components
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated