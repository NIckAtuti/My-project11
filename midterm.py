#This is for login process.

print("LOG IN")
Email = input("Enter your E-mail address")
print(Email)
Password = input("Enter your password 8 digit ")
print(Password)
#This is appointment taking process.
print("Take an Appointment")
print("List of Specialists")
print("1. Doctor A")
print("2. Doctor B")
print("3. Doctor C")
print("4. Doctor D")

# This is for Doctor A

select_doctor = input("Choose your doctor")

if select_doctor == "1":

        print("Doctor A \n a. 08:00AM-09:00AM \n b.12:00AM-01:00PM \n c. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 08:00AM-09:00AM")
        elif your_time == "b":
            print("b. 12:00AM-01:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")
#This is for Doctor B

elif select_doctor == "2":

        print("Doctor B \n a. 09:30AM-10:30AM\n b. 01:30PM-02:30PM \n c. 03:30PM-04:30PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 09:30AM-10:30AM")
        elif your_time == "b":
            print("b. 01:30PM-02:30PM")
        elif your_time == "c":
            print("c. 03:30PM-04:30PM")
        else:
            print("Not available")

#This is for Doctor C

elif select_doctor == "3":

        print("Doctor C \n a. 11:00AM-12:00AM \n b. 01:00PM-02:00PM \nc. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")

        if your_time == "a":
            print("a. 11:00AM-12:00AM")
        elif your_time == "b":
            print("b. 01:00PM-02:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")

#This is for Doctor D

elif select_doctor == "4":

        print("Doctor D \n a. 07:30AM-08:30AM \n b. 10:30AM-11:30AM \n c. 04:30PM-05:30PM")

        your_time = input("Favouralbe time")

        if your_time == "a":
            print("a. 07:30AM-08:30AM")
        elif your_time == "b":
            print("b. 10:30AM-11:30AM")
        elif your_time == "c":
            print("c. 04:30PM-05:30PM")
        else:
            print("Not available")


else:
    print("Doctor not available")

print("For cash Enter X")
print("For credit Enter Y")
payment = input("finish the payment")
if payment=="X":
    print("payment done by cash")
    recbill = input("Please enter the receipt for the bill")
    print(recbill)
    print= input("Thank you")
elif payment=="Y":
     print("payment done by credit")
     crebill = input("Please enter the credit card number")
     print(crebill)
     print("Thank you")
else:
    print("not paid and go for payment")

