for _ in range(int(input())):
    slen = int(input())
    sen = input().lower()
    sen = list(sen)
    sen = [ord(_)-96 for _ in sen]
    sen.sort()
    print(sen[slen-1])