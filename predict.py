N, M = map(int, input().split())

list_Nn = [i for i in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())
    temp = list_Nn[i-1:j]
    temp.reverse()
    list_Nn[i-1:j] = temp

print(*list_Nn)