#Codewars character recognition and change 

tuple_1 = ("51NGAP0RE")

array_1 = list(tuple_1)

for i in range(len(array_1)):
    if array_1[i] == '5':
        array_1[i] = 'S'
    elif array_1[i] == '1':
        array_1[i] = 'I'
    elif array_1[i] == '0':
        array_1[i] = 'O'

array_2 = ''.join(array_1)

print(array_2)


        


#def character_change(array_1):
    #array_2 = list(map(lambda st: str.replace(st, "5", "S"), array_1))
    #str.replace(st, "1", "I"),str.replace(st, "0", "O")
    #print(array_2)



#character_change(array_1)

# import the regex module
#import re

#string = "51NGAP0RE"
#print("Original string: ", string)


#newString = re.sub("5", "S", string)

#print("The new string: ", newString)


