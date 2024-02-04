import math

def addition(x, y):
    return x + y

def subtruction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Division operation is undefined (divide by 0 error)"
def squareroot(x):
    return math.sqrt(x)
def exponentiation(x,y):
    return x ** y
def factorial (x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
def absolutevalue(x):
     if(x<0):
         return x * -1 
     else :
         return x
def convertbinary(x):
     return bin( x )

def find_gcd(x,y):
    return math.gcd (x, y)

def find_lcm(x, y):
    return abs(x * y) // math.gcd(x, y) if x and y else 0

def calculate_logarithm(x, base):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))
def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def cotangent(x):
    return 1 / math.tan(math.radians(x))






while True:
    print("\n Select the action you want to take:")
    print("-" * 40)
    print("0. EXIT ")
    print("1. Addition")
    print("2. Subtruction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Exponentiation")
    print("7. Factorial ")
    print("8. Absolute value")
    print("9. Convert binary ")
    print("10. Find GSD ")
    print("11. Find LCM ")
    print ("12. Calculate Logarithm")
    print ("13. Calculate Sine")
    print ("14. Calculate Cosine")
    print ("15. Calculate Tangent")
    print ("16. Calculate Cotangent")



    





    print("-" * 40)

    choice = input("Enter your choice (0-16): ")

    if choice =='0':
        print("Exiting the program...")
        break

    if choice in ( '0','1', '2', '3', '4','6','10','11',):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    if choice in ('5','7','8','9'):
        num1 = int(input("Enter the first number: "))

    print("-" * 40)


    if choice == '1':
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtruction(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    elif choice == '5':
        print(f"{num1} = {squareroot(num1)}")
    elif choice == '6':
        print(f"{num1} ** {num2} = {exponentiation(num1,num2)}")
    elif choice =='7' :
        print (f"{num1} ! = {factorial (num1)}")
    elif choice == '8' :
        print(f"| {num1} | = {absolutevalue(num1)} ")
    elif choice == '9':
        print (f"{num1}  =   {convertbinary (num1)}")
    elif choice == '10':
        print(f"GSD ({num1},{num2}) = {find_gcd(num1,num2)} ")
    elif choice == '11':
        print(f"LCM ({num1} ,{num2}) = {find_lcm(num1,num2)}")
    elif choice =='12':
         num1 = float(input("Enter the number: "))
         base = float(input("Enter the base for the logarithm: "))
         print(f"Logarithm base {base} of {num1} = {calculate_logarithm(num1, base)}")
    elif choice == "13":
        angle = int(input("Enter the angle in degrees: "))
        print(f"Sin({angle}) = {sine(angle)}")
    elif choice == "14":
        angle = int(input("Enter the angle in degrees: "))
        print(f"Cos({angle}) = {cosine(angle)}")
    elif choice == "15":
        angle = int(input("Enter the angle in degrees: "))
        print(f"Tan({angle}) = {tangent(angle)}")
    elif choice == "16":
        angle = int(input("Enter the angle in degrees: "))
        print(f"Cot({angle}) = {cotangent(angle)}")
    else:
        print("Invalid choice !!!. Please try again...")
   