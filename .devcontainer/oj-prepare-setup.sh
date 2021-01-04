#!/usr/bin/env bash

# 注意:oj-prepareの設定ファイルは~/以下なので，事前にコンテナ内で作業するユーザに切り替えておく必要がある．

# oj-prepareの設定ファイル用のディレクトリを作る
mkdir ~/.config/online-judge-tools/

# シンボリックリンクを張る
ln -s /atcoder/.devcontainer/prepare.config.toml ~/.config/online-judge-tools/