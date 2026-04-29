# ASSIGNMENT - 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 250
else:
    print("You have chosen an invalid size.")

if pepperoni == "Y":
    if size == "S":
        bill += 80
    else:
        bill += 119

if extra_cheese == "Y":
    bill += 50

print(f"Your final bill is: Rs{bill}.")

# Assignment -2 :
# Input Marks from user using loop ; Evaluate Pass or Fail and Grades using conditional statements

marks=[]
s = int(input("Enter number of subjects :"))
for i in range(s):
    mark = float(input(f"Enter marks for subject {i+1} :"))
    marks.append(mark)
avg = sum(marks) / s
print(f"Average marks : {avg}")
if any(mark < 40 for mark in marks) :
    print("Result : Fail")
    print("Grade : F")
else :
    print("Result : Pass")
    if avg >=90:
        print("Grade : A+")
    elif avg>=80 :
        print("Grade : A")
    elif avg >=70:
        print("Grade : B")
    elif avg >=60:
        print("Grade : C")
    elif avg >=50:
        print("Grade : D")
    else :
        print("Grade : E")
