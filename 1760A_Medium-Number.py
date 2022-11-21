for _ in range(int(input())):
    array = [int(i) for i in input().split()]

    x = array[0]
    y = array[1]
    z = array[2]

    if (x > y and x < z) or (x > z and x < y):
        print(x)
    elif (y > z and y < x) or (y > x and y < z):
        print(y)
    else:
        print(z)