# noesis_utils/router.py
from pathlib import Path





STORAGE_DIR_NAME = ".noesis"





def get_storage_path() -> Path:
    storage_path = Path.home() / STORAGE_DIR_NAME

    if not storage_path.exists():
        print(f"[noesis_utils] directory '{storage_path}' does not exist, creating it...")
        storage_path.mkdir(exist_ok=True)
        print("[noesis_utils] directory created successfully.")
    else:
        print(f"[noesis_utils] directory '{storage_path}' already exists.")

    return storage_path