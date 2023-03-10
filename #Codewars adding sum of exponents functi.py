#Codewars adding sum of exponents function

""""

a = []

b = 2

c = input()

d = int(c)

def sum_exp_func(d):
    
    for i in (range(0,d)):
        
        e = (i**b)

        a.append(e)

        print(e)


sum_exp_func(d)

new_list = a

x = sum(new_list)

print(new_list)

print(x)

"""


b = 2
c = input()
d = int(c)

new_list = [i**b for i in range(d)]

x = sum(new_list)

print(new_list)
print(x)



