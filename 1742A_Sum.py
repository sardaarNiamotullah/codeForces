testCases = int(input())

for i in range(testCases):
    array = [int(i) for i in input().strip().split()]

    if (array[0] + array[1] == array[2]) or (array[0] + array[2] == array[1]) or (array[1] + array[2] == array[0]):
        print("YES")
    else:
        print("NO")