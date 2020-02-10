n = int(input())

arr = map(int, input().split())

print(arr)

ar = []
for i in arr:
    print(i)
    ar.append(i)

print(list(dict.fromkeys(ar)))
b = list(dict.fromkeys(ar))
b.sort()
print(b[-2])