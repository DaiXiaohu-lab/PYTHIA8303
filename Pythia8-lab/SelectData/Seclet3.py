#Select the pair of D0 and Dstarbar0, find the number of D0 and Dstarbar0 pair.

num_of_D0_and_Dstarbar0 = 0

file1 = open('e1.txt', 'w+')

f =  open("mymainout-X_3872.csv","r")

for line1 in f:
    if line1.find("D0") != -1:

        for line2 in f:
            if line2.find('D*bar0') !=-1:
                num_of_D0_and_Dstarbar0  +=1

                print(line1)
                print(line2)
                print('--'*67)
                file1.write(line1 +'\n')
                file1.write(line2 +'\n')


print('num_of_D0_and_Dstarbar0:',num_of_D0_and_Dstarbar0)
f.close()
file1.close()


