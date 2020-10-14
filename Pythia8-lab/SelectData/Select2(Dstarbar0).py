#!/usr/bin/env python
# Select  Dstarbar0, find the number of  Dstarbar0

num_of_D_star_bar0 = 0

with open("mymainout-X_3872(1).csv","r") as f:
    with open('Select2.txt','w+') as file1:
        for line2 in f:
            if line2.find("(D*bar0)") != -1:
                num_of_D_star_bar0 += 1
                print(line2)
                file1.write(line2+ '\n')
f.close()

print('number of Dstarbar0:',num_of_D_star_bar0)




