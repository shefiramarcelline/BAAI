#
#Shefira
#add subject, grade and calculate average grade of the student
#

#1. Input
print("How many subjects do you have?")

subjects = 0
sum = 0
number = 0
i=0
count = 0

#2. Process
i = int(input(""))
while count < i :
    print("Enter the name of subject: ")
    subject = input("")
    print("Enter the grade for ",subject)
    number = int(input(""))
    sum = sum+number
    count += 1
average = round(sum/i)

#3. Output
print("your average grade is: ",average)