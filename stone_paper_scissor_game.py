''' 
s for stone
p for paper
sc for scissor
'''

import random

s = 's'
p = 'p'
sc = 'sc'

computer = random.choice([s,p,sc])
user = str(input("your choice"))
print(user)
print(computer)

if(computer == s and user == s):
    print("match draw")
elif(computer == s and user == p):
    print("match result : user win , computer loose")
elif(computer == s and user == sc):
    print("match result : computer win , user loose")
elif(computer == p and user == s):
    print("match result : computer win , user loose")
elif(computer == p and user == p):
    print("match draw")
elif(computer == p and user == sc):
    print("match result : user win , computer loose")
elif(computer == sc and user == s):
    print("match result : user win")
elif(computer == sc and user == p):
    print("match result : computer win , user loose")
elif(computer == sc and user == sc):
    print("match draw")
else:
    print("error")