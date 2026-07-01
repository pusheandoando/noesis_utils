# noesis_utils/router.py
from pathlib import Path





STORAGE_DIR_NAME = ".noesis"





def get_storage_path() -> Path:
    storage_path = Path.home() / STORAGE_DIR_NAME
    storage_path.mkdir(exist_ok=True)
    return storage_path