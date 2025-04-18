#Global Scope variables
a=10 
b=5
def addition():
    #Local Scope variables
    a=15
    b=20
    print(a+b)

def sub():
    print(a-b)

addition()
sub()
