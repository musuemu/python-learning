#Find all duplicate items in a list.

#method 1:

import sys
while True:
    try:
        list1 = sys.stdin.readline().strip().split(",")
        list2 = []
        for i in list1:
            if list1.count(i) > 1:
                list2.append(i)
        print(set(list2))
    except:
        break

#result 1:
#1,2,3,4,5,6,3,4,5,6
#{'3', '6', '5', '4'}


#method 2:
import sys
from collections import Counter
while True:
    try:
        list1 = sys.stdin.readline().strip().split(",")
        dict1 = dict(Counter(list1))
        print([key for key, value in dict1.items() if value > 1])
    except:
        break
        
#result2:
#1,2,3
#[]
#11,22,33,44,22,44
#['22', '44']
