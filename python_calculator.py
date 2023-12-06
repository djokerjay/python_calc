def calculate(num1,num2,op):
    match op:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2

def showmenu():
    inputval=""
    while inputval!="e":
        print("Welcome to my calculator")
        print("+ = Addition")
        print("- = Subtraction")                
        print("* = Multiplication")
        print("/ = Division")        
        inputval = input("Enter Operation: ")
        if inputval!="e":
            getinput(inputval)
        
def getinput(operator):
    num1 = float(input("Enter Number #1: "))
    num2 = float(input("Enter Number #2: "))
    ans = calculate(num1,num2,operator)
    print("The answer is " + str(ans) + "\n")

showmenu()
