import os
import json
import numpy as np
import codecs


def ansi2utf8(data_dir):
    file_names = []

    all_file = os.listdir(data_dir)

    if not os.path.exists(os.path.join(data_dir,"utf8")):
        os.mkdir(os.path.join(data_dir,"utf8"))

    for file_name in all_file:
        if file_name == "utf8":
            continue
        if file_name.endswith(".json"):
            file_names.append(file_name)
            f = codecs.open(os.path.join(data_dir, file_name), 'r', 'ansi')
            ff = f.read()
            file_object = codecs.open(os.path.join(data_dir, "utf8", file_name), 'w', 'utf-8')
            file_object.write(ff)

    json_file = file_names[0]


with open(os.path.join(data_dir,"utf8",json_file), "r",encoding='utf-8') as f:
    info = json.load(f)

if __name__ == "__main__":
    # this action will transfer all the ansi encoded json file which under data_dir folder into utf-8 format
    # all the transfered files will saved in folder uft8 under data_dir
    data_dir = ""
    ansi2utf8(data_dir)