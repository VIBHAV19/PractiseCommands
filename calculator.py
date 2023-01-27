class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))        
obj=cal(a,b)
while True:    
    def menu():
        x = ('1. Add  \n2. Sub \n') 
        print(x)
    menu()
    choice = int(input('Please select one of the following : ')) 
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    else:
        print('Invalid option') 
        break       
print()
