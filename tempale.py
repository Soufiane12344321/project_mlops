import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/utils.py',
    'src/logger/logging.py',
    'src/exception/exception.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'tox.ini',
    'pyproject.toml',
    'experiment/experiments.ipynb',
]

for file in list_of_files:
    # Create the directory if it doesn't exist
    dir_path = os.path.dirname(file)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")
    
    # Create the file
    with open(file, 'w') as f:
        pass  # Just create an empty file