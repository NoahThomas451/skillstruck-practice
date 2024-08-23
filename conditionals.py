age = input()
license = True
if int(age) >= 16 and bool(license) == True:
    print('You are old enough to drive.')
else:
    print("You are not able to drive.")