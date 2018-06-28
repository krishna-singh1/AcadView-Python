from heapq import heappush, heappop
def heapsort(item):
    h=[]
    for i in item:
        heappush(h, i)
    return [heappop(h) for i in range(len(h))]
print(heapsort([4,2,3]))
