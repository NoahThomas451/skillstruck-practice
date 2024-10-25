words_count = {} # defining the dictionary

words = input("Create a list of words:   ").split() # takes the input and then splits it into a list
for word in words: #word is an element of the list
    if word not in words_count: # if not in the dictionary,
        print("Not in yet: ", words_count)
        words_count[word] = 0 #assigning add a new key value pair
        print("Just added one: ",words_count)
    words_count[word] += 1 
    print("Just increased the count on one: ", words_count)

# biggest = 0

# for x in words_count.values():
#     if x > biggest:
#         biggest = x

# for n in words_count:
#     if words_count[n] == biggest:
#         print(n)
# a a b a d e e k n o a h n o a h 