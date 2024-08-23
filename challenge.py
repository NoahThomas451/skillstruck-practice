number1 = input()
number2 = input()
number3 = input()
if int(number1) < int(number2) < int(number3):
    print(number1)
elif int(number2) < int(number1) < int(number3):
    print(number2)
elif int(number3) < int(number2) < int(number1):
    print(number3)