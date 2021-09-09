
#### 必要環境

python 3.8以降がインストールされていること

#### 手順

`VelCensored-pc/game`フォルダで`powershell`を開きます。  
（アドレスバーに`powershell`と入力し、エンター。）

```shell
# 翻訳ファイルDL
wget -OutFile 'translated.txt' 'https://docs.google.com/spreadsheets/d/15t2DiwvPYab69b48i5Qit5dNEmMnGGoUxEgCUglJVlo/export?format=tsv&gid=1293283491'
# 翻訳適用スクリプトDL
wget -OutFile 'main.py' 'https://github.com/Gniang/grimvel_trans_jp/raw/master/main.py'
# 日本語フォントDL
wget -OutFile 'SourceHanSansLite.ttf' 'https://github.com/Gniang/grimvel_trans_jp/raw/master/SourceHanSansLite.ttf'

python main.py
```

