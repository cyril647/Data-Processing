#!/user/bin/env python3


import pandas as pd
import os
import argparse
import numpy as np

# help and info: python filename -h
# e.g. python select_rows.py --file_path=/home/sicheng/Task_change2target --file_name=Original_Format_obj.csv --true_id 543 812

def select_row(file_name, file_dir, true_id):
    data_all = pd.DataFrame()
    file_path_name = os.path.join(file_dir, file_name)
    df = pd.read_csv(file_path_name)
    for id in true_id:
        data = df.loc[df['object.id'] == id]
        # print(data)
        data_all = data_all.append(data)
    output_name = file_name[:-4] + '_Kissme.csv'
    data_all.to_csv(os.path.join(file_dir, output_name), sep=",", index=False)

def get_parser():
    parser = argparse.ArgumentParser(description='Please enter the filename and the path to the input file')
    parser.add_argument('--file_path', type=str, default='/home/sicheng/Task_change2target/', help='输入原始文件的路径')
    parser.add_argument('--file_name', type=str, default='Target_Format_obj.csv',  help='输入原始文件的名字')
    parser.add_argument('--true_id', nargs= '+', type=int, default=[623, 543], help='输入需要的id列表如：623, 543')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parser()
    select_row(args.file_name, args.file_path, args.true_id)
    print('done!')