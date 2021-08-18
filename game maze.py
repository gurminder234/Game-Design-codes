import numpy as np
import random
maze = []



for i in range(10):
    a = []
    for i in range(10):
        if random.randint(0,1) == 0:
            a.append(" ")
        else:
            a.append("x")

    maze.append(a)


start = random.randint(1,8)
start1 = random.randint(1,8)

end = random.randint(1,8)
end1 = random.randint(1,8)

maze[start][start1] = "@"
maze[end][end1] = "E"

for t in range(10):
    maze[0][t] = "-"
    maze[9][t] = "-"
    maze[t - 1][0] = "|"
    maze[t - 1][9] = "|"

for q in maze:

    for v in q:

        print(v, end =  " ")
    print()

while( True):
    input1 = input("= ").lower()

    while input1 != "x":
        if input1 == "w":
            start = start - 1
            if maze[start][start1] != "-" and  maze[start][start1] !="|":

                if maze[start][start1] != "x":
                    maze[start + 1][start1] = " "
                    maze[start][start1] = "@"
                else:
                    start = start + 1
            else:
                start = start + 1
                pass
            for q in maze:
                for v in q:
                    print(v, end=" ")
                print()
            break

        if input1 == "s":
            start = start + 1

            if maze[start][start1] != "-" and  maze[start][start1] !="|":
                if maze[start][start1] != "x":
                    maze[start - 1][start1] = " "
                    maze[start ][start1] = "@"
                else:
                    start = start -  1
            else:
                start = start - 1
                pass
            for q in maze:
                for v in q:
                    print(v, end=" ")
                print()

            break
        if input1 == "a":
            start1 = start1 - 1
            if maze[start][start1] != "-" and  maze[start][start1] !="|":
                if maze[start][start1] != "x":
                    maze[start][start1 + 1] = " "
                    maze[start][start1 ] = "@"
                else:
                    start1 = start1 + 1
            else:
                start1 = start1 + 1
                pass
            for q in maze:
                for v in q:
                    print(v, end=" ")
                print()

            break
        if input1 == "d":
            start1 = start1 + 1

            if maze[start][start1] != "-" and  maze[start][start1] !="|":
                if maze[start][start1] != "x":
                    maze[start][start1 - 1] = " "
                    maze[start][start1] = "@"
                else:
                    start1 = start1 - 1
            else:
                start1 = start1 - 1
                pass
            for q in maze:
                for v in q:
                    print(v, end=" ")
                print()

            break
        if input1 != "w" or "s" or "a" or "d" or "x":
            print("invalid input!!")
            break
    else:
        break
    if start1 == end1 and start == end:
        print("Yeah finished!!!")
        break









