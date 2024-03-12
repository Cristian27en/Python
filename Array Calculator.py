
from array import array
mylist = array('i',[1,2,3,4,5])

def sum(mylist):
    return mylist[0] + mylist[1] + mylist[2] + mylist[3] + mylist[4]

result = sum(mylist)

print(result)


#using for loop

from array import array
mylist = array('i',[1,2,3,4,5])

def sum_loop(mylist):
    result=0
    for number in mylist:
        result = result + number
    return result

result = sum_loop(mylist)

print(result)

