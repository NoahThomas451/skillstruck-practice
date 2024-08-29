ride = {
    'luke' : 115,
    'mason' : 85,
    'reed' : 103,
    'isaac' : 102,
    'jackson' : 78
}
for x in ride.values():
    if x < 100:
        print('This person is too short to ride.')
    elif x >= 100:
        print('This person is tall enough to ride.')
    print(x)