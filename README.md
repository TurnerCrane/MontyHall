# 概要
このリポジトリは、Rayの強化学習ライブラリであるRLlibと、PythonとC++の間でシームレスなインタフェースを提供するPybind11を統合しています。Rayの強化学習機能を活用しつつ、C++との効率的な連携をするためのサンプルプログラムです。

# 特徴
Ray RLlibとPybind11を使用したシームレスなPythonとC++の統合
リポジトリ内には、サンプルコードや使用例が含まれています

# インストール
このプロジェクトを動作させるために必要な手順や依存関係について説明します。

``` bash
# インストール手順
pip3 install ray gymnasium lz4

# ビルド手順
git clone https://github.com/TurnerCrane/MontyHall.git
cd MontyHall
git submodule init
git submodule update
mkdir build
cd build
cmake ..
make

# 実行方法
python3 train.py
```
