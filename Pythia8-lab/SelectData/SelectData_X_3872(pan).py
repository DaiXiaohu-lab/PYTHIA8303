#!/usr/bin/env python
#Select the events when D0 and Dstarbar0 appear at the same time.

with open("mymainout-X_3872.csv","r") as f:
    msms = f.readlines()
    f.close()

file1 = open('SelectDate1.txt','w+')

num_of_complete_event= 0

num_of_sametime = 0
event = []
for i in msms:
    if "PYTHIA Event Listing  (complete event) " in i:
        num_of_complete_event += 1
        for j in event:
            if "Dbar0" in j:

                for k in event:
                    if "D*bar0"in k:

                        num_of_sametime += 1
                        print(j)
                        print(k)
                        print ("--"*67)
                        event = []
                        file1.write(j+'\n')
                        file1.write(k+'\n')

    event.append(i)
file1.close()


print("num_of_complete_event:", num_of_complete_event)

print("num_of_same_time:", num_of_sametime)
