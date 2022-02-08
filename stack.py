l = []
while True :
    c = int(input(''' 
              1. Push Element
              2. Pop Element
              3. Peek Element
              4. Stack list
              5. Exit
        Which action do you want to perform >?
    
    '''))
    

    if c == 1:
        print("You choose Option 1 , add any value in list")
        n = input("Enter The Value :- ")
        l.append(n)
        print(l, "added")

    elif c == 2:
        print("You choose Option 2 , pop out the value in list")
        if len(l) ==0:
            print("Empty Stack")
        else:    
            p = l.pop()
            print("The pop element",p)
    elif c == 3:
        if len(l) ==0:
            print("Empty Stack")
        else:
            print("The last Element is : ",l[-1] )
    elif c == 4:
        print(" The stack List :",l)
    elif c == 5 :
        break
    else:
        c>6
        print("cant find Your Operation")
    
        
