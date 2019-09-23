# 1
user_message_1 = input('please enter message:')
user_message_2 = input('What you what to find: ')
print(user_message_1.count(user_message_2))

# 2
user_message = str(input('please enter message:'))
middle_of_word = int(len(user_message) / 2)
three_digit = user_message[middle_of_word-1:middle_of_word+2]
if len(user_message) < 7:
    print('Error')
elif len(user_message) > 7:
    print(three_digit)

# 3
user_message = int(input('please enter your integer:'))
string_message = str(user_message)
inverted = string_message[::-1]
if string_message == inverted:
    print(True)
else:
    print(False)

# 4
user_message_1 = int(input('please enter your first integer:'))
user_message_2 = int(input('please enter your second integer:'))
if user_message_1 == 10 or user_message_2 == 10:
    print(True)
elif user_message_1 + user_message_2 == 10:
    print(True)
else:
    print(False)

# 5
user_message_1 = int(input('please enter your integer:'))
user_message_2 = str(input('please enter your string:'))
user_message_3 = (user_message_2[:user_message_1] + user_message_2[user_message_1+1:])
print(user_message_3)