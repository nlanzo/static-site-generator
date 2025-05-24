import os
import shutil


def copy_from_static_to_public(dir_from, dir_to):
    if not os.path.exists(dir_to):
        os.mkdir(dir_to)

    files = os.listdir(dir_from)

    for file in files:
        from_path = os.path.join(dir_from, file)
        to_path = os.path.join(dir_to, file)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_from_static_to_public(from_path, to_path)