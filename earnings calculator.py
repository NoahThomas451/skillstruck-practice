earningsgoal = input('How much do plan to save this year?')
months = int(earningsgoal)/12
weeks = int(earningsgoal)/48
days = int(earningsgoal)/365

print('To save up ' + earningsgoal + ' dollars in one year, you will need to save ' + str(round(months, 2)) + ' per month.')
print('To save up ' + earningsgoal + ' dollars in one year, you will need to save ' + str(round(weeks, 2)) + ' per week.')
print('To save up ' + earningsgoal + ' dollars in one year, you will need to save ' + str(round(days, 2)) + ' per day.')