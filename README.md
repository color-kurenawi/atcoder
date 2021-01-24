# atcoder

## これは何

AtCoderのPython3環境構築用リポジトリです．

VSCode with VSCode Remote Containersでの利用を想定していますが，Dockerのみでも利用可能です．`Dockerfile`及び`docker-compose.yml`は `.devcontainer/`以下に置いています．

## できること

- AtCoderにおけるPython3環境の再現
- AtCoderとほぼ同等*なPyPy3環境
- **online-judge-tools**，**online-judge-template-generator** を用いた自動テスト，自動提出

*AtCoderではPyPy3.6-3.7.0ですが，ビルド済のソースが見つからなかったため，このリポジトリではPyPy3.6-3.7.3を用いています．

## 使い方

### 環境構築

このレポジトリをclone

```bash
git clone https://github.com/color-kurenawi/atcoder.git
```

VSCodeで開く

```bash
code atcoder/
```

VSCode上でコマンドパレットを開き(Ctrl+Shift+P)，`Remote-Containers: Reopen in Container`を選択する．

### 自動テスト，自動提出

コンテスト中は，`contests/`以下で作業します．ここでは，AtCoder Beginner Contest 187(以下，ABC187)において自動テスト，自動提出を行う例を示します．

#### online-judge-toolsでAtCoderにログイン

```bash
oj-l
```

#### コンテスト用ディレクトリに移動

```bash
cd contests/
```

#### 自動テスト用入出力のダウンロード，テンプレートの作成

atcodee-cliのコマンドを利用し，問題ごとにディレクトリを作成，テンプレートとしてmain.pyを作成します．また，new以下の**abc187**はコンテストIDを指します．コンテストIDは，コンテストtopページ(https://<span>atcoder<span>.jp/contests/**abc187**)の最後の部分です．

```bash
oj-new abc187
```

#### 問題の解答

ABC187のA問題を解くとします．テンプレートが`contests/abc187/abc187_a/main.py`
に作成されているので`contests/abc187/abc187_a`に移動して，問題を解いていきます．

#### 解答の自動テスト，自動提出

ABC187のA問題の自動テストをするには，`contests/abc187/abc187_a`において

```bash
oj-test
```

また，自動提出は同ディレクトリにおいて

```bash
oj-submit
```

で行うことができます．

## 利用可能な言語

- Python 3.8.2
  - numpy==1.18.2
  - scipy==1.4.1
  - scikit-learn==0.22.2.post1
  - numba==0.48.0
  - networkx==2.4

- PyPy 3.6-3.7.3
