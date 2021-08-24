import os
from simpledbf import Dbf5

path = './dbc_files'

for file in os.listdir(path):
    if file.endswith('.dbf'):
        dbf = Dbf5(f'{path}/{file}', codec='latin')
        dbf.to_csv(f'{path}/csv/{os.path.splitext(file)[0]}.csv')
        print(f'{path}/{file} converted to csv')
