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

    while True:
        ran1 = random.randint(1, 4)
        ran1 = ran1 - 1
        if heap[ran1] != 0:
            ran2 = random.randint(1, heap[ran1])
            heap[ran1] = heap[ran1] - ran2
            print("Computer's turn is over now is your turn ")
            print(heap)
            break
        else:
            pass
    if heap == [0] * 4:
        print("computer wins!!")