import os
import shutil
import sys

def remove_dir(path):
    shutil.rmtree(path)
    if not check_dir(path):
        return True 
    return False

def check_dir(path:str)->bool:
    return os.path.isdir(path)

def check_file(path:str)->bool:
    return os.path.isfile(path)

def map_dirs(ignore:list)->dict:

    list_of_templates={}
    current_dir = os.getcwd()
    items = os.scandir(current_dir)
    for item in items:
        if item.name not in ignore:
            list_of_templates.update({item.name:item.path})
    return list_of_templates


