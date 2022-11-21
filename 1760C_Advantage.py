for _ in range(int(input())):
    aLen = int(input())
    array = [int(_) for _ in input().split()]
    mArray = array.copy()
    array.sort()
    strongest = array[aLen - 1]
    output = []

    for _ in mArray:
        if _ == strongest:
            output.append(_ - array[aLen - 2])
        else:
            output.append(_ - strongest)

    i = 0
    while i < len(output):
        if i == len(output) - 1:
            print(output[i])
        else:
            print(output[i], end=" ")
        i += 1