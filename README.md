# earthquake dl jp

## 概要

* 気象庁のWEBページでダウンロード可能な地震震源データを一括ダウンロードするコードです。
* データソース： https://www.data.jma.go.jp/svd/eqev/data/bulletin/hypo.html

実行方法

```bash
python earthquake_dl_jp.py
```

* 実行に時間がかかりますが、完了すると`csv`ディレクトリ内にcsvファイルが出力されます

## 出力カラム名

|      カラム名      |     項目名     | 特筆項目  |
|:--------------:|:-----------:|:-----:|
|      type      |  レコード種別ヘッダ  |       |
|      year      |     西暦      |       |
|     month      |      月      |       |
|      date      |      日      |       |
|      hour      |      時      |       |
|      min       |      分      |       |
|      sec       |      秒      | float |
|    sec_err     | 時間　標準誤差（秒）  | float |
|      lat       |    緯度（度）    |       |
|    lat_min     |    緯度（分）    | float |
|  lat_min_err   | 緯度　標準誤差（分）  | float |
|      lon       |    経度（度）    |       |
|    lon_min     |    経度（分）    | float |
|  lon_min_err   | 経度　標準誤差（分）  | float |
|     depth      |   深さ（km）    | float |
|   depth_err    | 深さ　標準誤差（km） | float |
|    mag1_val    |  マグニチュード1   | float |
|   mag1_type    | マグニチュード1種別  |       |
|    mag2_val    |  マグニチュード2   | float |
|   mag2_type    | マグニチュード2種別  |       |
|  t_time_table  |    使用走時表    |       |
| epicenter_eval |    震源評価     |       |
| epicenter_type |   震源補助情報    |       |
| max_intensity  |    最大震度     |       |
|     damage     |    被害規模     |       |
|    tsunami     |    津波規模     |       |
|    l_region    |   大地域区分番号   |       |
|    s_region    |   小地域区分番号   |       |
|   epicenter    |    震央地名     |       |
|    obs_nums    |    観測点数     |       |
|      flag      |   震源決定フラグ   |       |

* 特筆項目に`float`となっているカラムは、データを元データの表記から、float表記に変換してあります。
* 各列の説明は気象庁のレコードフォーマットページを参照してください。
	* https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/format/hypfmt_j.html

