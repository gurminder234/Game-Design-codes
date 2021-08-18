import random

op = 1
#heap = [2,3,4,6]
heap = []
for i in range(4):
    n = random.randint(1,6)
    heap.append(n)

while True:
    while op < 2:
        name1 = input("Name of player = ")

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
                for ran1 in range(1 , ran2):
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
        if heap == [0]*4:
            print("Computer won " + name1 + " lost, hell yeah!!")
            break

    else:
        print(heap)
        a = int(input(name1 + " tell heap choice = "))
        b = int(input(name1 + " tell no. of coins = "))
        heap[a - 1] = heap[a - 1] - b
        print(heap)

        if heap == [0] * 4:
            print(name1 + " WINS!!! ")
            break










