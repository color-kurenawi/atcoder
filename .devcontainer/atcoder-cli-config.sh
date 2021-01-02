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

# oj-toolsでatcoderにログインするためのaliasを設定する．
echo 'alias oj-l="oj login https://atcoder.jp/"' >> ~/.bash_aliases

# atcoder-cliとoj-toolsの両方でatcoderにログインするためのaliasを設定する．
echo 'alias ac-login="acc login && oj-l"' >> ~/.bash_aliases

# テストを簡単化するためのaliasを設定する
echo "alias oj-t='oj t -c \"python3.8 main.py ONLINE_JUDGE\"'" >> ~/.bash_aliases
echo "alias oj-t-pypy='oj t -c \"pypy3 main.py\"'" >> ~/.bash_aliases

# pypyの提出用にaliasを設定する
echo 'alias acc-s-pypy="acc s main.py -- --guess-python-interpreter pypy"' >> ~/.bash_aliases