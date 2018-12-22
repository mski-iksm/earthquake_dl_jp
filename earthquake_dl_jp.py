import requests
from bs4 import BeautifulSoup
import os
import pathlib
import pandas as pd

pd.options.display.max_columns = 10000
pd.options.display.max_rows = 10000


def download_zips():
    # download zip files
    base_url = "https://www.data.jma.go.jp/svd/eqev/data/bulletin/"
    r = requests.get("{}hypo.html".format(base_url))
    soup = BeautifulSoup(r.content, 'html5lib')

    for aa in soup.find_all("a"):
        link = aa.get("href")
        name = aa.get_text()
        if link[:5] == "data/":

            url = "{}{}".format(base_url, link)

            os.system("wget {} -P data --no-clobber".format(url))


def unzip_files(unzip=True):
    # unzip zip files
    path_obj = pathlib.Path('data')
    path_list = [str(item) for item in path_obj.glob('*.zip')]
    path_name_list = [item.name.split(".")[0] for item in path_obj.glob('*.zip')]

    if unzip:
        for path in path_list:
            os.system("unzip -d data -o {}".format(path))

    return path_name_list


def make_csv(path_name_list):
    for filename in path_name_list:
        convert_text(filename)


def convert_text(fname):
    print(fname)
    # convert into csv data
    colspecs = [(0, 1), (1, 5), (5, 7), (7, 9), (9, 11), (11, 13), (13, 15), (15, 17),
                (17, 19), (19, 21),
                (21, 24), (24, 26), (26, 28), (28, 30), (30, 32),
                (32, 36), (36, 38), (38, 40), (40, 42), (42, 44),
                (44, 46), (46, 49), (49, 50), (50, 52), (52, 54), (54, 55), (55, 57), (57, 58),
                (58, 59), (59, 60), (60, 61), (61, 62), (62, 63), (63, 64), (64, 65),
                (65, 68), (68, 92), (92, 95), (95, 96)]
    names = ["type", "year", "month", "date", "hour", "min", "sec_int", "sec_dec",
             "sec_err_int", "sec_err_dec",
             "lat", "lat_min_int", "lat_min_dec", "lat_min_err_int", "lat_min_err_dec",
             "lon", "lon_min_int", "lon_min_dec", "lon_min_err_int", "lon_min_err_dec",
             "depth_int", "depth_dec", "depth_err_int", "depth_err_dec",
             "mag1", "mag1_type", "mag2", "mag2_type",
             "t_time_table", "epicenter_eval", "epicenter_type", "max_intensity", "damage",
             "tsunami",
             "l_region", "s_region", "epicenter", "obs_nums", "flag"]
    eq_data_df = pd.read_fwf("data/{}".format(fname), colspecs=colspecs, names=names)
    eq_data_df["type"] = eq_data_df["type"].astype(str)
    eq_data_df["year"] = eq_data_df["year"].fillna("-9999").astype(float).astype(int)
    eq_data_df["month"] = eq_data_df["month"].fillna("-9999").astype(int)
    eq_data_df["date"] = eq_data_df["date"].fillna("-9999").astype(int)
    eq_data_df["hour"] = eq_data_df["hour"].fillna("-9999").astype(int)
    eq_data_df["min"] = eq_data_df["min"].fillna("-9999").astype(int)

    eq_data_df["sec_int"] = eq_data_df["sec_int"].fillna("0").astype(str)
    eq_data_df["sec_int"] = eq_data_df["sec_int"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["sec_dec"] = eq_data_df["sec_dec"].fillna("0").astype(str)
    eq_data_df["sec_dec"] = eq_data_df["sec_dec"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["sec"] = eq_data_df["sec_int"] + eq_data_df["sec_dec"] / 100.
    eq_data_df["sec_err_int"] = eq_data_df["sec_err_int"].fillna("0").astype(str)
    eq_data_df["sec_err_int"] = eq_data_df[
        "sec_err_int"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["sec_err_dec"] = eq_data_df["sec_err_dec"].fillna("0").astype(str)
    eq_data_df["sec_err_dec"] = eq_data_df[
        "sec_err_dec"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["sec_err"] = eq_data_df["sec_err_int"] + eq_data_df["sec_err_dec"] / 100.

    eq_data_df["lat"] = eq_data_df["lat"].fillna("-9999").astype(str)
    eq_data_df["lat"] = eq_data_df["lat"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lat_min_int"] = eq_data_df["lat_min_int"].fillna("0").astype(str)
    eq_data_df["lat_min_int"] = eq_data_df[
        "lat_min_int"].replace(" ", "").astype(float).astype(int)
    eq_data_df["lat_min_dec"] = eq_data_df["lat_min_dec"].fillna("0").astype(str)
    eq_data_df["lat_min_dec"] = eq_data_df[
        "lat_min_dec"].replace(" ", "").astype(float).astype(int)
    eq_data_df["lat_min"] = eq_data_df["lat_min_int"] + eq_data_df["lat_min_dec"] / 100.

    eq_data_df["lat_min_err_int"] = eq_data_df["lat_min_err_int"].fillna("0").astype(str)
    eq_data_df["lat_min_err_int"] = eq_data_df[
        "lat_min_err_int"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lat_min_err_dec"] = eq_data_df["lat_min_err_dec"].fillna("0").astype(str)
    eq_data_df["lat_min_err_dec"] = eq_data_df[
        "lat_min_err_dec"].str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lat_min_err"] = eq_data_df[
        "lat_min_err_int"] + eq_data_df["lat_min_err_dec"] / 100.
    eq_data_df["lon"] = eq_data_df["lon"].fillna(
        "-9999").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lon_min_int"] = eq_data_df["lon_min_int"].fillna(
        "0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lon_min_dec"] = eq_data_df["lon_min_dec"].fillna(
        "0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lon_min"] = eq_data_df["lon_min_int"] + eq_data_df["lon_min_dec"] / 100.
    eq_data_df["lon_min_err_int"] = eq_data_df[
        "lon_min_err_int"].fillna("0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lon_min_err_dec"] = eq_data_df[
        "lon_min_err_dec"].fillna("0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["lon_min_err"] = eq_data_df[
        "lon_min_err_int"] + eq_data_df["lon_min_err_dec"] / 100.
    eq_data_df["depth_int"] = eq_data_df["depth_int"].fillna(
        "0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["depth_dec"] = eq_data_df["depth_dec"].fillna(
        "0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["depth"] = eq_data_df["depth_int"] + eq_data_df["depth_dec"] / 100.
    eq_data_df["depth_err_int"] = eq_data_df[
        "depth_err_int"].fillna("0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["depth_err_dec"] = eq_data_df[
        "depth_err_dec"].fillna("0").astype(str).str.replace(" ", "").astype(float).astype(int)
    eq_data_df["depth_err"] = eq_data_df["depth_err_int"] + eq_data_df["depth_err_dec"] / 100.

    eq_data_df["mag1"] = eq_data_df["mag1"].fillna("00").astype(str)
    eq_data_df["mag1_flag"] = (eq_data_df["mag1"].str[0] == "A") | \
        (eq_data_df["mag1"].str[0] == "B") | \
        (eq_data_df["mag1"].str[0] == "C") | \
        (eq_data_df["mag1"].str[0] == "-")
    eq_data_df["mag1_val"] = (eq_data_df["mag1"].str[0] == "A") * (-1) + \
        (eq_data_df["mag1"].str[0] == "B") * (-2) + \
        (eq_data_df["mag1"].str[0] == "C") * (-3)
    eq_data_df.loc[eq_data_df["mag1_flag"], "mag1_val"] = \
        eq_data_df.loc[eq_data_df["mag1_flag"], "mag1_val"] \
        - eq_data_df.loc[eq_data_df["mag1_flag"], "mag1"].str[1].astype(float).astype(int) / 10.
    eq_data_df.loc[~ eq_data_df["mag1_flag"], "mag1_val"] = \
        eq_data_df.loc[~ eq_data_df["mag1_flag"], "mag1"].fillna(0).astype(float).astype(int) / 10.

    eq_data_df["mag2"] = eq_data_df["mag2"].fillna("00").astype(str)
    eq_data_df["mag2_flag"] = (eq_data_df["mag2"].str[0] == "A") | \
        (eq_data_df["mag2"].str[0] == "B") | \
        (eq_data_df["mag2"].str[0] == "C") | \
        (eq_data_df["mag2"].str[0] == "-")
    eq_data_df["mag2_val"] = (eq_data_df["mag2"].str[0] == "A") * (-1) + \
        (eq_data_df["mag2"].str[0] == "B") * (-2) + \
        (eq_data_df["mag2"].str[0] == "C") * (-3)
    eq_data_df.loc[eq_data_df["mag2_flag"], "mag2_val"] = \
        eq_data_df.loc[eq_data_df["mag2_flag"], "mag2_val"] \
        - eq_data_df.loc[eq_data_df["mag2_flag"], "mag2"].str[1].astype(float).astype(int) / 10.
    eq_data_df.loc[~ eq_data_df["mag2_flag"], "mag2_val"] = \
        eq_data_df.loc[~ eq_data_df["mag2_flag"], "mag2"].fillna(0).astype(float).astype(int) / 10.

    columns = ["type", "year", "month", "date", "hour", "min", "sec", "sec_err",
               "lat", "lat_min", "lat_min_err",
               "lon", "lon_min", "lon_min_err",
               "depth", "depth_err",
               "mag1_val", "mag1_type", "mag2_val", "mag2_type",
               "t_time_table", "epicenter_eval", "epicenter_type", "max_intensity", "damage",
               "tsunami",
               "l_region", "s_region", "epicenter", "obs_nums", "flag"]
    eq_data_df = eq_data_df[columns]
    eq_data_df.to_csv("csv/{}.csv".format(fname), index=False)


if __name__ == '__main__':
    download_zips()
    path_name_list = unzip_files(unzip=False)
    make_csv(path_name_list)
