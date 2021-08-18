#order = 2,3,4,4,3,2,
import random

rabbit = [1,1,1,1,1]
day = 0
print(rabbit)
while rabbit != [0] * 5:
    turn = int(input("Enter Hole no.  "))
    rabbit[turn - 1] = 0
    print(rabbit)
    temp = [0, 0, 0, 0, 0]
    for i in range(5):

        if rabbit[i] == 1:

            if i == 0:
                temp[i + 1] = 1


            elif i == 4:
                temp[i - 1] = 1

            else:
                temp[i + 1] = 1
                temp[i - 1] = 1

    for k in range(5):
        rabbit[k] = temp[k]
    day = day + 1
    print("Day " + str(day))
    print(rabbit)
    continue

else:
    print("Yeah you killed rabbit in " + str(day) + " days")


