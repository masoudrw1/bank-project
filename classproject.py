import random
from colorama import Fore,Style
host_castomers=[]
class custumer ():
    def __init__(self,name,lastname,code,inventory):
        self.name=name
        self.lastname=lastname
        self.code=code
        self.inventory=inventory
    def creat_auunt_bank(self):
        self.ob1=acuunt_bank(self.code,self.inventory)
        self.ob1.get_accnumber()
        self.obf=savefile(self.name,self.ob1.get_accnumber())
    def get_accnumber(self):
        return self.ob1.get_accnumber()
    def show(self):
        print(f"name:{self.name}\nlastname:{self.lastname}\ncode:{self.code}\naccbank:{self.ob1.get_accnumber()}\ninventory:{self.inventory}\n******\n")
    def cash_withdrawal(self,cash):
        new_inventory=self.ob1.cash_withdrawal(cash)
        if(self.inventory!=new_inventory):
            self.inventory=new_inventory
            self.obf.cash_withdrawal(cash,self.inventory)
            return 1
        else:
            return 0
    def Inventory_increase(self,cash):
        self.inventory=self.ob1.Inventory_increase(cash)
        self.obf.Inventory_increase(cash,self.inventory)
        return self.inventory

    def transfer (self,cash):
        new_inventory = self.ob1.cash_withdrawal(cash)
        if (self.inventory != new_inventory):
            self.inventory = new_inventory
            self.obf.tranfer(cash, self.inventory)
            return 1
        else:
            return 0
    def print_history(self):
        self.obf.print_history()

class acuunt_bank():
    def __init__(self,code,inventory):
        self.code=code
        self.code=int(self.code)
        self.inventory=inventory
        self.accnumber=self.code+random.randint(1,1000) #fix it
    def get_accnumber(self):
        return self.accnumber

    def cash_withdrawal(self,inputinventory):
        if (self.inventory>inputinventory):
            self.inventory=self.inventory-inputinventory
            return self.inventory
        else:
            self.inventory=self.inventory-0
            return self.inventory

    def Inventory_increase(self,inputinventory):
        self.inventory=self.inventory+inputinventory
        return self.inventory

class savefile():
    def __init__(self,name,acccode):
        self.name=name
        self.acccode=acccode
        self.file=open(f"D:\softwar\pycharm\\bankproject\\filebankperson\\{self.name,self.acccode}.txt","x")
        self.file.close()
    def cash_withdrawal(self,cash,inventory):
        self.file=open(f"D:\softwar\pycharm\\bankproject\\filebankperson\\{self.name,self.acccode}.txt","a")
        self.file.write(f"Inventory reduction\n-{cash}\naccount balance:{inventory}\nacc number :{self.acccode}\n**********\n")
        self.file.close()
    def Inventory_increase(self,cash,inventory):
        self.file=open(f"D:\softwar\pycharm\\bankproject\\filebankperson\\{self.name,self.acccode}.txt","a")
        self.file.write(f"Inventory increase\n+{cash}\naccunt balance:{inventory}\nacc number :{self.acccode}\n**********\n")
        self.file.close()
    def tranfer(self,cash,inventory):
        self.file=open(f"D:\softwar\pycharm\\bankproject\\filebankperson\\{self.name,self.acccode}.txt","a")
        self.file.write(f"Money transfer\n-{cash}\nacc balance:{inventory}\nacc number : {self.acccode}\n**********\n")
        self.file.close()
    def print_history(self):
        self.file=open(f"D:\softwar\pycharm\\bankproject\\filebankperson\\{self.name,self.acccode}.txt","r")
        print(self.file.read())
        self.file.close()

##############################################################################################

def massege():
    print("welcome to bank prpject \n")
    print("plese enter optios\n1.Create an account\n2.Login to the account\n")
def login(x):
    global cash
    inputoption=massege_login()

    while(inputoption>0):
        if(inputoption==1):
            print("Enter the amount required to withdraw money\n")
            cash=input()
            cash=float(cash)
            rezult=x.cash_withdrawal(cash)
            if (rezult==1):
                print(Fore.GREEN+f"mission accomplished Your new inventory {x.inventory}\n"+Style
                      .RESET_ALL)
            else:
                print(Fore.RED+"Insufficient inventory\n"+Style.RESET_ALL)
            inputoption=massege_login()

        if (inputoption==2):
            print("Enter the amount required to increase the balance\n")
            cash=input()
            cash=float(cash)
            x.Inventory_increase(cash)
            print(Fore.GREEN+f"The required amount has been transferred Your new inventory {x.inventory}"+Style.RESET_ALL)
            inputoption=massege_login()

        if (inputoption==3):
            inputaccnumber=input("Please enter the desired account number to transfer money\n")
            cash=input("Please enter the required amount\n")
            cash=float(cash)
            Host_account=find_accnumbers(inputaccnumber)
            confirmation=input(Fore.GREEN+f"Are you sure to transfer the amount of {cash} dollars to {Host_account.name,Host_account.lastname} account number{Host_account.get_accnumber()} ?(Y/N)\n"+Style.RESET_ALL)
            if (confirmation=='y'):
                rezult = x.transfer(cash)
                if (rezult == 1):
                    Host_account.Inventory_increase(cash)

                    print(Fore.GREEN + f"mission accomplished Your new inventory {x.inventory}\n" + Style
                          .RESET_ALL)
                else:
                    print(Fore.RED + "Insufficient inventory\n" + Style.RESET_ALL)

        inputoption = massege_login()

        if(inputoption==4):
            x.show()
            inputoption=massege_login()

        if (inputoption==5):
            x.print_history()
            inputoption=massege_login()

def cunvert():
    select = input()
    select = int(select)
    return select

def get_info():


    print("ples enter name \n")
    inputname=input()
    print("ples enter lastname\n")
    inputlastname=input()
    print("ples enter code\n")
    inputcode=input()
    print("Enter the required amount for deposit\n")
    inputinventory=input()
    inputinventory=float(inputinventory)
    while(inputinventory<30):
        print("The amount is not enough, it must be at least 30 dollars")
        inputinventory=input()
        inputinventory=float(inputinventory)
    new_person=custumer(inputname,inputlastname,inputcode,inputinventory)
    host_castomers.append(new_person)
    new_person.creat_auunt_bank()
    print(Fore.GREEN+f"Your account was created in the name of {new_person.name ,new_person.lastname} with code {new_person.code} and account number {new_person.get_accnumber()}"+Style.RESET_ALL)

    return new_person

def massege_login():
    print("plese enter option\n1.cash withdrawal\n2.Inventory increase\n3.Money transfer\n4.View inventory\n5.Print transaction history")
    inputoption = input()
    inputoption = int(inputoption)
    return inputoption

def find_accnumbers(accnumber):
    accnumber=int(accnumber)
    for i, x in enumerate(host_castomers):
        if (x.get_accnumber() == accnumber):
            return x