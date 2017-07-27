# O (n log n)
# input = (1, 3, 5, 9)

# possible
# (1,3),(5,9)
# (1,5),(3,9)
# (1,9),(3,9)
# (4,14) -> 14
# (6,12) -> 12
# (10,8) -> 10

# output -> 10


# O(n log n) (similar to mergeSort)
# input will not be sorted 

# Traversing the input ( pairing input[0] with each input from input[1:]) - O(log n)
# Splitting the input into pairs - O(n) 
# Finding largest sum of the pairs 
# min of list of largest 
def lrg_Sm_sm(lst):
    """
        >>>lst = [3, 1, 5, 9]
        >>>lrg_Sm_Sm(lst)
        >>>10
    """
    srtlst = sorted(lst)

    while srtlst > 0: 
        bigpair = (srtlst.pop(0), srtlst.pop())
        return bigpair

lst = [3, 1, 5, 9]
print lrg_Sm_sm(lst)