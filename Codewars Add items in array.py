#Codewars adding array function

#import numpy as np

array = [1,2,3,4,5]

length = len(array)

def array_addition(length):
    
    if length == 0:
        print('0')
    
    else:
        print(sum(array))

array_addition(array)
