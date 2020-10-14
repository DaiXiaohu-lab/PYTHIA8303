#Select the pair of D0 and Dstarbar0, find the number of D0 and Dstarbar0 pair.

num_of_D0_and_Dstarbar0 = 0

with open("mymainout-X_3872(2).csv","r") as f:
    with open('Seclet3.txt', 'w+') as file1:
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

f.close()
file1.close()
print('num_of_D0_and_Dstarbar0:',num_of_D0_and_Dstarbar0)






