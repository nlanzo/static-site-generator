import os
import shutil


def copy_from_static_to_public(dir_from, dir_to):
    if not os.path.exists(dir_to):
        os.mkdir(dir_to)

    files = os.listdir(dir_from)
    for file in files:
        file_path = os.path.join(dir_from, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(dir_to, file))
        else:
            copy_from_static_to_public(file_path, os.path.join(dir_to, file))