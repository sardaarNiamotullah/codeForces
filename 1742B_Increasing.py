testCases = int(input())

for i in range(testCases):
    arrayLen = int(input())
    array = [int(i) for i in input().strip().split()]

    if arrayLen == 1:
        print('YES')
        continue
    if arrayLen == 0:
        print('YES')
        continue

    i = 0
    doable = True

    while i < len(array):
        j = i + 1
        while j < len(array):
            if array[i] == array[j]:
                doable = False
            j += 1
        i += 1

    if doable:
        print('YES')
    else:
        print('NO')