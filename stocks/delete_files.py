import glob
import os
import shutil

source_path = 'D:/hotma/AlgorTrading/algo/files/'
map_file = 'D:/hotma/AlgorTrading/algo/nasdaq_files_error.txt'

os.chdir(source_path)
list_files = glob.glob('*.csv')

with open(map_file,'r') as remove_file_list:
    remove_list = remove_file_list.read()
    rl = remove_list.split('\n')
for name in list_files:
  if name.split('.')[0] in rl:
      os.remove(name)
