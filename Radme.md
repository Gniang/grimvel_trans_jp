
必要環境

python 3.8以降がインストールされていること

```shell
# 翻訳ファイルDL
wget -OutFile 'translated.txt' 'https://docs.google.com/spreadsheets/d/15t2DiwvPYab69b48i5Qit5dNEmMnGGoUxEgCUglJVlo/export?format=tsv&gid=1293283491'
# 翻訳適用スクリプトDL
wget -OutFile 'main.py' ''
# 日本語フォントDL
wget -OutFile 'SourceHanSansLite.ttf' ''

python main.py
```

