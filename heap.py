def klar(arr, k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i], end=" ")
arr = [1, 23, 12, 9, 30, 2, 50,343,23]
k = 4
#klar(arr, k)
print(max(arr));arr.pop(max(arr));print(max(arr))
arr.pop(max(arr))
print(max(arr))

