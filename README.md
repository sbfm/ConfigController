# ConfigController
====
Pythonのconfigparserをラップしたクラスです。

## Description
設定ファイルが存在しないとき、自動で設定ファイルを作成します。  
設定値がないとき、自動でdefault値を設定します。  
また、getPropertiesCを利用すれば、プロパティ値の説明を加えることができます。  
これはソースコードの配布や設定ファイルを安全にするのに役に立ちます。  

## Sample Code
[sample code]  
import ConfigController as cc  
cini = cc.Call('config.ini')  
value = cini.getProperties("Application","setting","defaultValue")  
  
[sample code2]  
import ConfigController as cc  
cini = cc.Call('config.ini')  
cini.setSection("Application")  
value = cini.getProperties("setting","defaultValue")  
  
[sample code3]  
import ConfigController as cc  
cini = cc.Call('config.ini')  
cini.setSection("Application")  
value = cini.getPropertiesC("setting","defaultValue","settingInfoText")  

## Licence
MIT Licence  

## Author

[sbfm](https://github.com/sbfm)
 
