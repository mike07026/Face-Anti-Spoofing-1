import os,shutil,glob
import sys
from random import shuffle

def create_Partition(filepath, labels):
    data = dict()
    x = os.listdir(filepath)
    num = len(x)
    print(num)
    num_test = (int)(num*(0.05))
    num_train = num-num_test
    num_train_val = (int)(num_train*(0.05))
    num_train_tr = num_train - num_train_val
    shuffle(x)
    data["training"] = x[:num_train_tr]
    data["validate"] = x[num_train_tr:num_train_tr+num_train_val]
    data["testing"] = x[num_train_tr+num_train_val:] 
    return data



filepath = "E:\\CV\\MSU_8_Class\\MSU_8_Class\\Dataset"
labels = ["f_aa","f_ao","f_ap","f_la","f_lo","f_lp","r_ap","r_lp"]
batch_size = 16

data = create_Partition(filepath, labels)

train_path='E:\\CV\\MSU_8_Class\\MSU_8_Class\\train_cases.txt'
fh=open(train_path,"w")
count=0
files=os.walk('E:\\CV\\MSU_8_Class\\MSU_8_Class\\Dataset')
print(files)
test_path =  'E:\\CV\\MSU_8_Class\\MSU_8_Class\\test_cases.txt'
fh=open(test_path,"w")
count=0
for f in data["testing"]:
    fh.write(f)
    count=count+1
    fh.write("\n")
print(count)
for k in data["validate"]:
    fh.write(k)
    count=count+1
    fh.write('\n')
fh.close()
source = 'E:\\CV\\MSU_8_Class\\MSU_8_Class\\Dataset\\'
dest = 'E:\\CV\\MSU_8_Class\\MSU_8_Class\\Test\\'

F = open("E:\\CV\\MSU_8_Class\\MSU_8_Class\\test_cases.txt", "r")
l = F.read().split('\n')
#print l
for i in range(0,len(l)-1):
        shutil.move(source+l[i], dest)

print(count)


#print(count)