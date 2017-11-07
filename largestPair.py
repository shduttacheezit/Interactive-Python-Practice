# 11/6/17 NextSpace Berkeley WWC East Bay Meetup 

# Big O--
# n = size of input 
# -> time
# -> space 

# EXAMPLE: Dinner Party at Your House
# clean your home - constant 
# *you clean your house the same way 

# passing food around the table - linear 
# *everyone will touch the food once 

# greeting everyone - exponential 
# *you greet X person, X person greets everyone else 
# *^drop the coefficients

# STEPS - ALGORITHM SOLVING--
# 1. clarify the question 
# 2. inputs and outputs 
# 3. test cases
# 4. brainstorming 
# 5. runtime 
# 6. coding 
# 7. debugging 


# 1. Largest Pair (CoderByte)
#  Challenge
#  Using the JavaScript language, have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest double digit number. The input will always contain at least two positive digits. 
#  Sample Test Cases
#  Input:453857
#  Output:85
#  Input:363223311
#  Output:63
# --> def LargestPair(num):
#     """
#     >>>LargestPair(453857)
#     85
#     >>>LargestPair(363223311)
#     63
#     """
#     # iterating and then slicing 
#     lst = str(num)
#     currentMax = lst[0]
#     for i in range(0,(len(lst)-1)):
#         # if int(currentMax) < int(i):
#         if currentMax < lst[i:i+2]:
#             currentMax = lst[i:i+2]
#     return currentMax 


# print LargestPair(453857)
# print LargestPair(363223311)


# 2. Given a list/array, return the most repeated element 


def LargestPair(num):
    """
    >>>LargestPair(453857)
    85
    >>>LargestPair(363223311)
    63
    """
    # iterating and then slicing 
    lst = str(num)
    currentMax = lst[0]
    for i in range(0,(len(lst)-1)):
        # if int(currentMax) < int(i):
        if currentMax < lst[i:i+2]:
            currentMax = lst[i:i+2]
    return currentMax 


print LargestPair(453857)
print LargestPair(363223311)


def modeInitial(strlst):
    """
    >>>modeInitial(['A', 'HL', 'CC', 'CC', 'K'])
    'CC'
    >>>modeInitial([])
    None 
    >>>modeInitial('A', 'HL','HL', 'CC', 'CC', 'K')
    'HL', 'CC'
    """
    dict = {}
    currentMax = strlst[0]
    for i in strlst:
      if i in dict:
        dict[i] += 1
        if dict[i] > dict[currentMax]:
          currentMax = i
      else:
        dict[i] = 1
    return currentMax, dict
    
lst = ['A', 'HL', 'CC', 'CC', 'K']
print modeInitial(lst)
