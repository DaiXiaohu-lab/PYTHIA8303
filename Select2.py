#!/usr/bin/env python

file1 = open('Select2.txt','w+')
num_of_complete_event= 0
num_of_D_bar0 = 0
num_of_D_star_bar0 = 0
num_of_D_same_time = 0


f= open("mymainout-X_3872.csv","r")
msms = f.readlines()
for k in msms:
    if "PYTHIA Event Listing  (complete event)" in k:
        num_of_complete_event +=1
for i in msms:
    if "Dbar0" in i:
        num_of_D_bar0 += 1
        for j in msms:
            if "D*bar0" in j:
                num_of_D_star_bar0 +=1
                print(i)
                print(j)
                file1.write(i+ '\n')
                file1.write(j+ '\n')
                print('--' * 67)
num_of_D_star_bar0 = num_of_D_star_bar0/num_of_D_bar0
num_of_D_same_time = min(num_of_D_bar0,num_of_D_star_bar0)
print('number of Dbar0:',num_of_D_bar0)
print('number of Dstarbar0:',num_of_D_star_bar0)
print('number of same time:', num_of_D_same_time)
print('number of complete envent:',num_of_complete_event)
f.close()
file1.close()