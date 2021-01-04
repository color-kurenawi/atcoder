#!/usr/bin/env python3

import argparse
import subprocess
import os

DEFAULT_LANGUAGE = "cpython"
DEFAULT_SUBMIT_TARGET = "main.py"
DEFAULT_WAIT_TIME = "0"

def get_args():
    parser = argparse.ArgumentParser(description="oj command wrapper for submit to AtCoder")
    parser.add_argument('-l', "--language", type=str, default=DEFAULT_LANGUAGE, help="submit language")
    parser.add_argument('-t', "--target", type=str, default=DEFAULT_SUBMIT_TARGET, help="target file for submit")
    parser.add_argument('-w', "--wait", type=str, default=DEFAULT_WAIT_TIME, help="wait time before submit")
    
    args = parser.parse_args()
    return args

def get_args_info():
    args = get_args()
    args_info = args.__dict__
    return args_info
    
def make_command():
    args_info = get_args_info()
    language = args_info["language"]
    submit_target = args_info["target"]
    
    command_elements = ["oj", "s", submit_target]
    
    if language in ["cpython", "pypy"]:
        python_elements = ["--guess-python-interpreter", language]
        command_elements.extend(python_elements)
        
    wait_time = args_info["wait"]
    command_elements.extend(["--wait", wait_time])
    
    command = " ".join(command_elements)
    return command

def submit():
    command = make_command()
    subprocess.run(command, shell=True)

def main():
    submit()
    
if __name__ == "__main__":
    main()