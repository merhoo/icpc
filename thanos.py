n = int(input())
l = [int(x) for x in input().split()]
print(thanos(l, 0, len(l) - 1))
def thanos(A, p, q):
    if p == q:
        return 1
    if isSorted(A):
        return
    return max(thanos(A,p, (p+q)/2)


def isSorted(A):
    for i in A:
        if 
