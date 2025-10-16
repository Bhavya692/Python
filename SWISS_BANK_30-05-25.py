class SWISSBank():
    minbal=500000
    IFSC='SWISS000420'
    def __init__(self,name,mobno,Aadhar,bal,pin):
        self.name=name
        self.mobno=mobno
        self.Aadhar=Aadhar
        self.bal=bal
        self.pin=pin
    def Details(self):
        print(f'Name           ={self.name}')
        print(f'MobileNumber   ={self.mobno}')
        print(f'Aadharcard     ={self.Aadhar}')
        print(f'Bal            ={self.bal}')
        print(f'IFSC           ={self.IFSC}')
        print(f'Minimum balance={self.minbal}')
    @staticmethod
    def enter_pin():
        password=int(input('enter 4-digit pin:'))
        return password
    def CheckBal(self):
        count=3
        while count>0:
            print(f'No of chances available:{count}')
            if self.enter_pin()==self.pin:
                print(f'Available Balance is {self.bal}')
                break
            else:
                print('Invalid pin')
                print('try again')
                count-=1
        else:
            print('No attempts left')
    def WithDraw(self):
        count=3
        while count>0:
            print(f'No of chances available:{count}')
            if self.enter_pin()==self.pin:
                amount=int(input('enter the amount to withdraw:'))
                if amount<=self.bal:
                    if 500<=amount<=20000:
                        if amount%100==0:
                            self.bal -= amount
                            print('Amount debited Successfully......')
                            print(f'Available Balance is{self.bal}')
                            break
                        else:
                            print('enter valid denomintaions......')
                    else:
                        print('Invalid Limit')
                else:
                    print('Insufficient Balance')
            else:
                print('Invalid Limit')
                print('try again')
                count-=1
    def Deposite(self):
        count=3
        while count>0:
            print(f'No of chances available:{count}')
            if self.enter_pin()==self.pin:
                money=int(input('enter the amount to deposite:'))
                if 100<=money<=50000:
                    if money%100==0:
                        print('Amount Deposited Successfully')
                        print(f'Available Balance is{self.bal}')
                        break
                    else:
                        print('enter valid denominations.....')
                else:
                    print('Liimit Exceeded')
            else:
                print('Invalid Limit')
                print('try again')
                count-=1
        else:
            print('Try again Later')
    @classmethod
    def modifybal(cls):
        cls.minbal=0
cust1=SWISSBank('VijayMalya',8888888888,100010001000,500000001,2409)
cust2=SWISSBank('Ambani',9999999999,999999999999,10000000000,1234)
cust3=SWISSBank('Ratan TATA',9000000000,111111111111,9999999999,1001)
#SWISSBank.Deposite(cust2)
#SWISSBank.Details(cust3)
#cust1.CheckBal()
#cust3.WithDraw()
cust2.Deposite()
