import kagglehub
import os
import shutil

# 1) Download dataset via KaggleHub
path = kagglehub.dataset_download("vivek468/superstore-dataset-final")
print("Downloaded to cache:", path)

# 2) Ensure project/data exists
DATA_DIR = os.path.join("project", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 3) Copy all files from cache into project/data
for file in os.listdir(path):
    src = os.path.join(path, file)
    dst = os.path.join(DATA_DIR, file)
    shutil.copy(src, dst)

print("Files copied into:", DATA_DIR)


