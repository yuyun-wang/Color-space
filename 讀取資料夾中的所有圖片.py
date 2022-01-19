import cv2
import os
import random
import numpy as np

#讀取資料夾中所有照片
def get_filepaths(directory):
    file_paths = []
    for root, subdir, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.endswith(".jpg"):
                file_paths.append(filepath)
    return file_paths

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(".\\color\\")
