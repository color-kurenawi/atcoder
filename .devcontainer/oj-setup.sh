#!/usr/bin/env bash

# 注意:oj-prepareの設定ファイルは~/以下なので，事前にコンテナ内で作業するユーザに切り替えておく必要がある．

# oj-submitのシンボリックリンクを張る．
sudo ln -s /atcoder/scripts/oj-submit /usr/local/bin/

# oj-prepareの設定ファイル用のディレクトリを作る
mkdir -p ~/.config/online-judge-tools/

# 設定ファイルのシンボリックリンクを張る
ln -s /atcoder/.devcontainer/prepare.config.toml ~/.config/online-judge-tools/

# /usr/local/bin/にラッパーのシンボリックリンクを張る．
sudo ln -s /atcoder/scripts/oj-new /usr/local/bin/

# alias集を~/.bash_aliasesに追加する．
cat /tmp/oj_aliases >> ~/.bash_aliases