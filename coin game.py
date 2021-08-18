def heap1(arg):
    for v in arg:
        print(v * "$", end=" ")
    print()

import random

heap = []
for i in range(4):
    n = random.randint(1,8)
    heap.append(n)

user = int(input("Press  1 for computer \n"
        
         "Press 2 for PvP \n"
         ))
op = 1

while True:
    if user == 2:#uman vs human
        while op < 2:
            name1 = input("Name of player 1 = ")
            name2 = input("Name of player 2 = ")
            print(heap)
            op = op + 1
        a = int(input(name1 + " tell heap choice = "))
        b = int(input(name1 + " tell no. of coins = "))
        heap[a-1] = heap[a-1] - b
        print(heap)
        if heap == [0] * 4:
            print(name1 + " WINS!!! ")
            break

        c = int(input(name2 + " tell the heap choice = "))
        d = int(input(name2  + " tell no. of coins = "))
        heap[c-1] = heap[c-1] - d
        print(heap)

        if heap == [0] * 4:
            print(name2 + " WINS!!!")
            break
    elif user == 4:  #Computer vs human
        while op < 2:
            name1 = input("Name of player = ")
            print(heap)
            op = op + 1
            break

        a = int(input(name1 + " tell heap choice = "))
        b = int(input(name1 + " tell no. of coins = "))
        heap[a - 1] = heap[a - 1] - b
        print(heap)
        if heap == [0] * 4:
            print(name1 + " WINS!!! ")
            break


        ran1 = random.randint(1, 4)
        ran1 = ran1 - 1
        if heap[ran1] != 0:
            ran2 = random.randint(1, heap[ran1])
            heap[ran1] = heap[ran1] - ran2
            print("Computer's turn is over now is your turn ")
            print(heap)

        else:
            while heap[ran1 ] != 0:
                ran1 = random.randint(1, 4)
                ran1 = ran1 - 1

                ran2 = random.randint(1, heap[ran1])
                heap[ran1] = heap[ran1] - ran2
            else:
                print("Computer's turn is over now is your turn ")
                print(heap)

        if heap == [0] * 4:
            print("Computer won " + name1 + " lost!!")
            break
        if heap == [0] * 3:
            max1 = int(max(heap))
            max2 = int(heap.index(max1))
            heap[max2] = heap[max2] - max1
            print(heap)
            print("Computer WON!!!")
            break

    else:
        while op < 2:
            name1 = input("Name of player = ")
            print(heap)

            op = op + 1
            break
        A = heap[0]
        B = heap[1]
        C = heap[2]
        D = heap[3]

        nim = (A ^ B ^ C ^ D)
        if nim != 0:

            d = 0
            while nim != 0:
                for i in range(len(heap)):
                    ran2 = heap[i] + 1
                    for ran1 in range(1, ran2):
                        heap[i] = heap[i] - ran1
                        nim = heap[0] ^ heap[1] ^ heap[2] ^ heap[3]
                        if nim == 0:
                            d = 1

                            print("Computer's turn is over now is your turn " + name1)
                            print(heap)
                            break
                        else:
                            heap[i] = heap[i] + ran1
                            continue
                    if d == 1:
                        break
            if heap == [0] * 4:
                print("Computer won " + name1 + " lost!!")
                break

        else:

            a = int(input(name1 + " tell heap choice = "))
            b = int(input(name1 + " tell no. of coins = "))
            heap[a - 1] = heap[a - 1] - b
            print(heap)

            if heap == [0] * 4:
                print(name1 + " WINS!!! ")
                break











