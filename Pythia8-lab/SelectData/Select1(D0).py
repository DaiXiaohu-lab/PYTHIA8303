#!/usr/bin/env python
# Select the  Dstarbar0, find the number of  Dstarbar0

num_of_D_bar0 = 0

with open("mymainout-X_3872(1).csv","r") as f:
    with open('Select1.txt','w+') as file1:
        for line1 in f:
            if line1.find("(D0)") != -1:
                num_of_D_bar0 += 1
                print(line1)
                file1.write(line1 + '\n')

f.close()

print('number of Dbar0:',num_of_D_bar0)




