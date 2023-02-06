#find nearest square number Codewars - finds out if number is square using modulus 




#for i in range(0,16):
    #print(i)



def nearest_sq(n):
    import math
    
    root_n = math.sqrt(n) 

    if n == 1:
        print('1')
    
    elif n != (0):
        print(n)
        
    else:
        root_n%1 == 0

        #print(n)
        
    if int(root_n):

        base = int(root_n)

        square = (base * base)
        
    print (square)

 
nearest_sq(2)

#nearest_sq(int(input(1)))

