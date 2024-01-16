import os
from pathlib import Path
import sys
import shutil
from datetime import datetime


FOLDER_NAMES = []


def current_time():
    return datetime.utcnow()



def parse_file_name(name: str):
    """takes in file name and extract folder name"""
    parsed = name.strip()[:11]
    print(parsed)
    FOLDER_NAMES.append(parsed)


# split the file name that has the part number
def create_folders():
    for x in FOLDER_NAMES:
        os.mkdir(x)


def create_backup():
    home = Path.home()
    backup_loc = f"{home}/Documents/projsort_{current_time()}_backup"
    os.mkdir(backup_loc)
    for file in os.listdir():
        shutil.copyfile(file, f"{backup_loc}/{file}")


def main(parent_folder: str):
    """run all other funcs"""

    for files in os.listdir():
        print(files)
        parse_file_name(files)

    for folder in FOLDER_NAMES: 
        print(folder)
        os.mkdir(f"{parent_folder}/{folder}")

    for x in os.listdir():
        Path(x).rename(f"{parent_folder}/{x.strip()[:11]}/{x}")



    for x in os.listdir():
        Path(x).rename(f"{x.strip()[:11]}/{x}")



if __name__ == "__main__":
    # Always create a backup

    try:
        create_backup()
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        p = Path(f'{sys.argv[1]}')
        if p.exists:
            main(sys.argv[1])
        else:
            print("invalid path")
            sys.exit(1)


