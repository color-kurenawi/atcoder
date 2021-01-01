#!/bin/sh

# atcoder-cliの設定をするためのshell

# 入出力のディレクトリの設定をonline-judge-toolsと合わせる
acc config default-test-dirname-format test

# デフォルトですべての問題をダウンロードする．
acc config default-task-choice all

# pythonのテンプレートファイルを設定する．
acc_config_dir=$(acc config-dir)
ln -s /atcoder/templates/python $acc_config_dir/python

# デフォルトのテンプレートをpythonに設定する．
acc config default-template python

# pypyの提出用にaliasを設定する
echo 'alias acc-s-pypy="acc s main.py -- --guess-python-interpreter pypy"' >> ~/.bash_aliases