name = input()
    
def banjo_function(name):

    if name.startswith ('R') or name.startswith ('r'):
        print ("Congratulations " + name + " you play banjo!")

    else: 
        print (name + " you don't play Banjo!") 

banjo_function(name)

