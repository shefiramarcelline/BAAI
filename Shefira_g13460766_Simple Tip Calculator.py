#
# Shefira
# Calculate total bill calculator with tip
#

amount = 0
sum = 0
total = 0
i = 0
tip = 0

# 1. Input
print("How many people are dining :")
i = int(input(""))

# 2. Process
for count in range(1, i + 1):
    print("Enter the amount spent by person", count, ":")
    amount = int(input(""))
    sum = sum + amount
print("Enter the tip percentage :")
tip = int(input(""))
total = sum + sum*tip/100

# 3. Output
print("The total bill including tip is : $", total)
