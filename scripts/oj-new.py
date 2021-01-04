#!/usr/bin/env python3

import argparse
import subprocess
import os

ATCODER_ROOT = "https://atcoder.jp/contests/"

def get_args():
    parser = argparse.ArgumentParser(description="oj-prepare wrapper for atcoder")
    parser.add_argument("contest_id", type=str, help="set atcoder contest_id")
    args = parser.parse_args()
    return args

def get_args_info():
    args = get_args()
    args_info = args.__dict__
    return args_info
    
def get_url_from_contest_id(contest_id):
    url = os.path.join(ATCODER_ROOT, contest_id)
    return url
    
def make_command():
    args_info = get_args_info()
    
    contest_id = args_info["contest_id"]
    contest_url = get_url_from_contest_id(contest_id)
        
    command_elements = ["oj-prepare", contest_url]
    
    command = " ".join(command_elements)
    
    return command

def oj_new():
    command = make_command()
    subprocess.run(command, shell=True)

def main():
    oj_new()
    
if __name__ == "__main__":
    main()