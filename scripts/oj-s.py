#!/usr/bin/env python3
import argparse
import subprocess
import json
import os

DEFAULT_LANGUAGE = "cpython"
PYTHON_TEMPLATE_NAME = "main.py"
JSON_NAME = "contest.acc.json"
JSON_ROOT = "../"

def get_args():
    parser = argparse.ArgumentParser(description="oj t command in online-judge-tools wrapper")
    parser.add_argument('-l', "--language", type=str, default=DEFAULT_LANGUAGE, help="select submit language")
    
    args = parser.parse_args()
    return args

def get_json_path():
    json_path = os.path.join(JSON_ROOT, JSON_NAME)
    return json_path

def get_submit_url():
    json_path = get_json_path()
    return json_path

def get_target_parent_dir():
    cwd = os.getcwd()
    parent_dir = cwd.split("/")[-1]
    return parent_dir    

def get_json_info():
    json_path = get_json_path()
        
    with open(json_path, "r") as f:
        json_dict = json.load(f)

    parent_dir = get_target_parent_dir()
    
    task_dicts = json_dict["tasks"]
    json_info = {}
    
    for task_dict in task_dicts:
        if task_dict["directory"]["path"] == parent_dir:
            json_info = task_dict
    
    return json_info
    
def get_submit_info():
    submit_info = get_args().__dict__
    
    json_info = get_json_info()
    submit_info["url"] = json_info["url"]
    
    return submit_info
    
def make_command():
    submit_info = get_submit_info()
    language = submit_info["language"]
    submit_url = submit_info["url"]
        
    command_elements = ["oj", "s", submit_url]
    
    if language in ["cpython", "pypy"]:
        python_elements = [PYTHON_TEMPLATE_NAME, "--guess-python-interpreter", language]
        command_elements.extend(python_elements)
        
    command_elements.append("--wait 0")
    
    command = " ".join(command_elements)
    return command

def submit():
    command = make_command()
    subprocess.call(command, shell=True)

def main():
    submit()
    
if __name__ == "__main__":
    main()