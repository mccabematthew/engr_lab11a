# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: Matthew McCabe, Nick Foley, Alejandro Zertuche, Jaime Reyes
# Section: 102 538
# Assignment: Lab 11a
# Date:
from user import User


# local variables for user setter data entry
x = float(input('Enter the float amount of your loan: '))
y = float(input('Enter the float interest rate percentage: '))
z = input('Enter the file name to store your data: ')

# object instantiation and setters
u1 = User()
u1.set_lamt(x)
u1.set_ir(y)
u1.set_file(z)

# retrieving age using getter
print(u1.get_lamt())
print(u1.get_ir())
print(u1.get_file())
