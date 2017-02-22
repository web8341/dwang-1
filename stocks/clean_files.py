import glob
import os
import shutil

source_path = 'D:/hotma/AlgorTrading/algo/files/'
remove_path = 'D:/hotma/AlgorTrading/algo/file/remove/'

os.chdir(source_path)
list_files = glob.glob('*.csv')
for name in list_files:
  with open(name, 'r') as file:
    ltr1 = file.read()[0]
    if ltr1=='<':
      print(name.split('.')[0]) 
