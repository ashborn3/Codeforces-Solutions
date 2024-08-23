import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
# Take int input
def inp():
    return(int(input()))
# Take list input
def inlt():
    return(list(map(int,input().split())))
# Take string input as a array of chars
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
# For taking space seperated integer variable inputs.
def invr():
    return(map(int,input().split()))


def min_operations_to_equal_elements(arr):
    from collections import Counter
    n = len(arr)
    frequency = Counter(arr)
    max_freq = max(frequency.values())
    min_operations = n - max_freq
    return min_operations

t = inp()
for i in range(t):
    n = inp()
    a = inlt()
    print(min_operations_to_equal_elements(a))