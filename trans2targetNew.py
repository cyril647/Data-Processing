#!/user/bin/env python3

import pandas as pd
import os
import argparse
import numpy as np

# help and info: python filename -h
# e.g. python change2target.py --file_path=/home/sicheng/Task_change2target --file_name=Original_Format_obj.csv


#Required parameters
from setuptools.command.py36compat import sdist_add_defaults

obj_usecols = ['header timestamp',	'object.id', 'class_label_pred', 'pose.position.x',	'pose.position.y', 'pose.position.z',
'pose.orientation.w', 'pose.orientation.x', 'pose.orientation.y', 'pose.orientation.z',	'velocity.linear.x', 'velocity.angular.z',
'yaw', 'dimension_x', 'dimension_y', 'dimension_z']
ego_usecols = ['header timestamp', 'position x', 'position y', 'oritentation yaw', 'velocity']


def change2target(file_name, file_path, output_name, usecols):
    file_path_name = os.path.join(file_path, file_name)
    data = pd.read_csv(file_path_name, usecols = usecols)
    data.to_csv(os.path.join(file_path, output_name), sep=",", columns=usecols, index=False)

def get_parser():
    parser = argparse.ArgumentParser(description='Please enter the filename and the path to the input file')
    parser.add_argument('--file_path', type=str, default='/home/sicheng/Task_change2target/', help='输入原始文件的路径')
    parser.add_argument('--file_name', type=str, default='Original_Format_ego.csv',  help='输入原始文件的名字')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = get_parser()
    output_name = args.file_name[:-4] + '_Kissme.csv'
    if args.file_name[-7:] == 'obj.csv':
        change2target(args.file_name, args.file_path, output_name, obj_usecols)
        print('obj.csv done')
    elif args.file_name[-7:] == 'ego.csv':
        change2target(args.file_name, args.file_path, output_name, ego_usecols)
        print('ego.csv done')
    else:
        print('No obj and ego type csv')




