import random
heap = []
for i in range(4):
    n = random.randint(1,8)
    heap.append(n)

op = 1
n = 3
while True:
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
    A = heap[0]
    B = heap[1]
    C = heap[2]
    D = heap[3]

    while True:
        if A + B + C + D > 0:
            ran1 = random.randint(1, 4)

            if A and B and C and D > 0:
                we = str(ran1 - 1)
                ran2 = random.randint(1,heap[ran1 - 1])
                print(ran2)
                heap[ran1 -1] = heap[ran1 - 1] - ran2
                print(heap)
                print("w" + we)
                break
            else:
                ran1 = ran1 + 1
                if ran1 > 4:

                    ran1 = ran1 - 2
                    ran2 = random.randint(1,heap[ran1])
                    print(ran2)
                    heap[ran1] = heap[ran1] - ran2
                    print(heap)
                    we = str(ran1)
                    print("w" + we)
                    break
                else:
                    if heap[ran1] > 0:

                        ran1 = random.randint(1,4)
                        ran2 = random.randint(1,heap[ran1 - 1])
                        heap[ran1 -1] = heap[ran1 - 1] - ran2
                        print(ran2)
                        print(heap)
                        we = str(ran1)
                        print("w" + we)
                        break
                    else:
                        ran1 = ran1 - 1
                        ran2 = random.randint(1,heap[ran1])
                        print(ran2)
                        heap[ran1] = heap[ran1] - ran2
                        print(heap)
                        we = str(ran1)
                        print("w" + we)
                    break

        else:
            print("computer won")







