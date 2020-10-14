#!/usr/bin/env python
# Select the single D0 and Dstarbar0, find the number of D0 and Dstarbar0

file1 = open('Select1.txt','w+')
num_of_complete_evet= 0
num_of_D_bar0 = 0
num_of_D_star_bar0 = 0
num_of_D_same_time = 0

f= open("mymainout-X_3872.csv","r")
msms = f.readlines()
for k in msms:
    if "PYTHIA Event Listing  (complete event)" in k:
        num_of_complete_evet +=1
for i in msms:
    if "D0" in i:
        num_of_D_bar0 += 1
        print(i)
        file1.write(i + '\n')
print('--'*67)
for j in msms:
    if "D*bar0" in j:
        num_of_D_star_bar0 += 1

        print(j)

        file1.write(j+ '\n')

print('number of Dbar0:',num_of_D_bar0)
print('number of Dstarbar0:',num_of_D_star_bar0)
print('number of complete envent:',num_of_complete_evet)
f.close()
file1.close()


