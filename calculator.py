def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multifly(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error ! Divided by zero "
    else:
        return x/y
    
def displa_menu():
       print("Welcome to Calculator") 
       print("1.Add")
       print("2.Subtract")
       print("3.Multifly")
       print("4.Divition")
       print("5.Reset")
       print("6.Exit")
