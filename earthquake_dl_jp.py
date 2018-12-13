import requests
from bs4 import BeautifulSoup
import os
import pathlib
import pandas as pd


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

# unzip zip files
path_obj = pathlib.Path('data')
path_list = [str(item) for item in path_obj.glob('*.zip')]
path_name_list = [item.name.split(".")[0] for item in path_obj.glob('*.zip')]

for path in path_list:
    os.system("unzip {} -d data -o".format(path))

# connect files
f = open('all_eq_data.txt', 'w')
for filename in path_name_list:
    read_f = open("data/{}".format(filename))
    text_data = read_f.read()
    read_f.close()
    f.write(text_data)
    f.write("\n")
f.close()

# convert into csv data
colspecs = [(0, 1), (1, 5), (5, 7), (7, 9), (9, 11), (11, 13), (13, 17), (17, 21),
            (21, 24), (24, 28), (28, 32), (32, 36), (36, 40), (40, 44),
            (44, 49), (49, 52), (52, 54), (54, 55), (55, 57), (57, 58),
            (58, 59), (59, 60), (60, 61), (61, 62), (62, 63), (63, 64), (64, 65),
            (65, 68), (68, 92), (92, 95), (95, 96)]
names = ["type", "year", "month", "date", "hour", "min", "sec", "sec_err",
         "lat", "lat_min", "lat_min_err", "lon", "lon_min", "lon_min_err",
         "depth", "depth_err", "mag1", "mag1_type", "mag2", "mag2_type",
         "t_time_table", "epicenter_eval", "epicenter_type", "max_intensity", "damage", "tsunami",
         "l_region", "s_region", "epicenter", "obs_nums", "flag"]
eq_data_df = pd.read_fwf("all_eq_data.txt", colspecs=colspecs, names=names)
eq_data_df.to_csv("eq_data_df.csv", index=False)
