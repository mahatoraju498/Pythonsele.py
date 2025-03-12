class AccountI:
    def __init__(self):
        self.gender=input("choose 1.'Mr.',2.'Mrs.':")
        if self.gender=="1":
            self.gender = "Mr."
        elif self.gender == "2":
            self.gender = "Mrs."
        else:
            print("invalid choice.please enter 1,2")
        
        # self.name =input("enter your name")

        self.password=input("enter your password")
    

        self.check = int(input("choose an option(0:none, 1:newsletter,2:offer,3:both)"))
        if self.check=="1":
            self.check="newletter"
        elif self.check =="2":
            self.check ="offer"
        elif self.check=="3":
            self.check="both"
        elif self.check =="0":
            self.check="none"
        else:
            print("invalid choice,please enter 1,2,3,")
# account = AccountI()



