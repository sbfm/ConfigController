# PythonConfigController
====
Pythonのconfigparserをラップしたクラス

## Overview
Vimのフォント設定をコマンドから手軽に行えます。

## Description
設定ファイルが存在しないとき、自動で設定ファイルを作成します。
設定値がないとき、自動でdefault値を設定します。
これはソースコードの配布や設定ファイルを安全にするのに役に立ちます。

## Sample Code
import ConfigController as cc

cini = cc.ConfigController('config.ini')
cini.setSection("Application")
value = cini.getProperties("setting","defaultValue")

## Licence
MIT Licence

## Author

[sbfm](https://github.com/sbfm)
 
