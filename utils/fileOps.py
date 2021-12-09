import os

def is_file_empty(file_path):
    return not os.path.getsize(file_path) > 0