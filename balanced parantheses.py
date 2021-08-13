def balCheck(s):
    if len(s)%2!=0: #odd lenght will have no pair
        return False
    o=set('({[') #to see the starting elements
    m=set([ ('[',']'), ('(',')'), ('{','}') ]) #compare the elements
    stack = [] #adding the starting elements and then compairig with last elements
    for i in s: #taking every elements of string
        if i in o: #seeing is string starting with opening parantheses
            stack.append(i) #if yes, then storing in stack
        else:
            if len(stack)==0: #if no element found with opening parantheses and found a closing parantheses
                return False
            last = stack.pop() #taking the closing parantheses and storing in last
            if (last,i) not in m: #compairing the pairs
                return False
    return len(stack)==0 # if lenght = 0

print(balCheck('(){([)}'))

