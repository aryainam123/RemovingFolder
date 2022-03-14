import os
import shutil
import time
deletedFoldersCount = 0
deletedFilesCount = 0
path = input("Please enter the path")
days = 30
seconds = time.time() - (days * 24 * 60 * 60)
if os.path.exists(path):