import classproject
from colorama import Fore,Style

print("welcome to bank prpject \n")
print("plese enter optios\n1.Create an account\n2.Login to the account\n")
try:
    select=input()
    select=int(select)
    customers=[]

    if (select<0 or select>2):
        while(select<0 or select>2):
            print(Fore.RED+"rwong input ples enter crect number \n"+Style.RESET_ALL)
            select = input()
            select = int(select)
    while(select>0):

        if (select<=2):

            if(select==1):

                nc=classproject.get_info()
                customers.append(nc)
                classproject.massege()
                select=classproject.cunvert()

            if(select==2):
                print("ples enter accnumber \n")
                inputacc=input()
                inputacc=int(inputacc)

                for i,x in enumerate(customers):
                    if(x.get_accnumber()==inputacc):
                        classproject.login(x)
                        break
                classproject.massege()
                select=classproject.cunvert()
        else:
            while (select < 0 or select > 2):
                print(Fore.RED+"rwong input ples enter crect number \n"+Style.RESET_ALL)
                select = input()
                select = int(select)
except:
    print(Fore.RED+"wrong input"+Style.RESET_ALL)













