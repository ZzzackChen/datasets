import pandas as pd
import shutil
import os
path = r'D:\dataset\celeba\\'
male_dir = path + 'male'
female_dir = path + 'female'
if not os.path.exists(male_dir):
    os.mkdir(male_dir)
if not os.path.exists(female_dir):
    os.mkdir(female_dir)
with open(path+'list_attr_celeba.csv') as f:
    reader = pd.read_csv(f)
    male_list = []
    female_list = []
    male_idx = reader['Male']==1
    female_idx = reader['Male']==-1
    male_list = reader[male_idx]['image_id']
    female_list = reader[female_idx]['image_id']
    for img_name in male_list:
        shutil.copy(path+img_name, male_dir+img_name)