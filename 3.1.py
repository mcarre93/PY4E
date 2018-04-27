# 3.1 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types
# numbers properly.

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))
pay = rate * hrs
overtime = (hrs - 40) * (rate * 1.5)

# If the hours are greater than 40, calculate for overtime pay. Otherwise,
# the standard rate of pay variable is used.
if hrs > 40:
    pay = (rate * 40) + overtime
    print(pay)
else:
    print(pay)
