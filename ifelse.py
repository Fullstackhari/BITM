'''if(5>10):
    print("yes")
else:
    print("no")'''

email="hari@gmail.com"
pwd=123
otp=134567
uemail=str(input("enter email id:"))
upwd=str(input("enter password:"))

if(email==uemail):
    if(pwd==upwd):
        if(otp==134567):
            print("transcation successful")
        else:
            print("transaction denied")
    else:
        print("login successful")
else:
     print("login failed due to incorrect pwd")
