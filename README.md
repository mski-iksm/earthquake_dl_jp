# earthquake dl jp

## 概要

* 気象庁のWEBページでダウンロード可能な地震震源データを一括ダウンロードするコードです。
* データソース： https://www.data.jma.go.jp/svd/eqev/data/bulletin/hypo.html

実行方法

```bash
python earthquake_dl_jp.py
```

* 実行に時間がかかるかもしれませんが、完了すると`eq_data_df.csv`という名前のcsvファイルが出力されます
* 各列の説明： https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/format/hypfmt_j.html

