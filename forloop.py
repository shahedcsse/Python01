"""
start='*'

for i in range(1,5):
    for j in range(i):
        print('*',end=(""))

    print() """  

"""start=int(input("enter the number:"))

for i in range(start):
        for j in range(i+1):
            print ("*",end="")
        print()    
"""
"""for i in range(1,20):
    print (i)"""

"""row= int(input("enter the Number:"))

for i in range(row):
    for j in range(i,row-1):
        
        
        for z in range(i,row+1):

          print("*",end="")
        print()   
"""
"""row= int(input("enput  the number:"))

for i in range(row ,0,-1):
    for j in range(0,i):
        print("*",end=(""))
    print()    """


row =input("input the value:")
number=1

for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
        number += 1
    print()    