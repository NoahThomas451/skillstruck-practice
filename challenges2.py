number = input()
number2 = input()
if int(number) > int(number2):
    print('The first number is larger.')
elif int(number) < int(number2):
    print('The second number is larger.')
elif int(number) == int(number2):
    print('The numbers are the same.')