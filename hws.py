class atm :
   
    def __init__(self,name,balance):     #constructor is a special member fumction which we make to initilize a class
        self.name=name
        self.balance=balance
    def display(self):
        print("the acount holder's name -", self.name)
        print("your account balance -", self.balance)
    def add(self, num):
        self.balance += num
    def widhraw(self,num2):
        self.balance -= num2



a=atm("Sakshi", 1000)

while True:

    temp = input('''            -welcome-
    Choose the task  you want to perform
    Enter 1 for viewing your account statement
    Enter 2 for adding amount into your account
    Enter 3 for widtdrawing amount from your account
    Enter 4 if you want to exit.               \n''')

    if(temp=='1'):
        a.display()
        
    elif(temp=='2'):
        amount=int(input("enter the amount you want to add: " ))
        a.add(amount)
        a.display()

    elif(temp=='3'):
        amount=int(input("enter the amount you want to widthdraw: " ))
        if a.balance >= amount :
            a.widhraw(amount)
            a.display()
        else:
            print("Insufficient Balance")
    elif(temp == '4'):
        print("---Thank you for using the ATM.--- ")
        break
    else:
        print("-there is no such choice-")
