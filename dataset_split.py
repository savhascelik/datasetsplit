import random
import os
import subprocess
import sys

def split_data_set(image_dir,train_txt,val_txt,test_txt,val_ratio,test_ratio):

    f_test = open(test_txt, 'w')
    f_train = open(train_txt, 'w')
    f_val = open(val_txt, 'w')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(test_ratio * data_size)
    data_eval_size = int(val_ratio * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    eval_array = random.sample(range(data_size), k=data_eval_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "jpg"):
            ind += 1
            
            if ind in test_array:
                f_test.write(image_dir+'/'+f+'\n')
            elif ind in eval_array:
                f_val.write(image_dir+'/'+f+'\n')
            else:
                f_train.write(image_dir+'/'+f+'\n')


split_data_set(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])