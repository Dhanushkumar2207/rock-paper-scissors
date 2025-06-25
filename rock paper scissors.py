import random
value=input("enter y or n: ")
list=['r','p','s']
if value=='y':
    o=input("enter rock or paper or scissor as r/p/s: ").lower()
    temp=random.choice(list)
    print(temp)
    if o==temp:
        print("the match is draw")
    elif o=='r' and temp=='s':
        print(o," is the winner")
    elif o=='r' and temp=='p':
        print(temp," is the winner")
    elif o=='s' and temp=='r':
        print(temp," is the winner")
    
    elif o=='s' and temp=='p':
         print(o," is the winner")
    elif o=='p' and temp=='r':
          print(o,"is the winner")
    elif o=='p' and temp=='s':
        print(temp," is the winner")
                
elif value=='n':
    print("thanks for playing")
else:
    print("invalid choice")
