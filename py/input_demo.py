# # range() 

# list_a = list(range(0,5))

# print(list_a)




# #sys

# import sys

# name = sys.argv[1]

# print("How old are you?")
# age = int(input())

# print(name)
# print(age)


# height = 74 # The unit is inches
# if height > 70 :
#     print("You are really tall")




#while loop

# players = 11

# while players >= 5 :
#     print("The remaining players are",players)
#     players -= 1


# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 2 == 0:
#         print(i) # Result 2 4



        
# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 2 == 1:
#         print(i) # Result 1 3 5


# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 5 == 0:
#         print(i)  # Result 5


# players = 11

# while players >= 5:
#     print("The remaining players are", players)
#     players -= 1


# players = 2

# while players <= 5:
#     print("The remaining players are", players)
#     players += 1



#Make a Magic 8 ball
#https://github.com/viljow/magic8/blob/master/main.py

# import time
# import random

# answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy',
#            'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

# print('  __  __          _____ _____ _____    ___  ')
# print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
# print(' | \  / |  /  \ | |  __  | || |      | (_) |')
# print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
# print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
# print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
# print('')
# print('')
# print('')
# print('Hello World, I am the Magic 8 Ball, What is your name?')
# name = input()
# print('hello ' + name)


# def Magic8Ball():
#     print('Ask me a question.')
#     input()
#     print(answers[random.randint(0, len(answers)-1)])
#     print('I hope that helped!')
#     Replay()


# def Replay():
#     print('Do you have another question? [Y/N] ')
#     reply = input()
#     if reply == 'Y':
#         Magic8Ball()
#     elif reply == 'N':
#         exit()
#     else:
#         print('I apologies, I did not catch that. Please repeat.')
#         Replay()


# Magic8Ball()


# # https://github.com/soupyck/Magic8Ball/blob/master/magic8ball.py
# import random
# import time

# eight_ball = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
#               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
#               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
#               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
#               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]


# def question():
#     question = input(
#         "You may ask your yes or no question of the Magic 8 Ball!\n")
#     print("Thinking...")
#     time.sleep(random.randrange(0, 5))
#     print(random.choice(eight_ball))


# while True:
#     question()
#     repeat = input("Would you like to ask another question? (Y or N)")
#     if not (repeat == "y" or repeat == "Y"):
#         print("Come back if you have more questions!")
#         break


# # Import the modules
# import sys
# import random

# ans = True

# while ans:
#     question = (
#         "Ask the magic 8 ball a question: (press enter to quit) ")

#     answers = random.randint(1, 8)

#     if question == "":
#         sys.exit()

#     elif answers == 1:
#         print("It is certain")

#     elif answers == 2:
#         print("Outlook good")

#     elif answers == 3:
#         print("You may rely on it")

#     elif answers == 4:
#         print("Ask again later")

#     elif answers == 5:
#         print("Concentrate and ask again")

#     elif answers == 6:
#         print("Reply hazy, try again")

#     elif answers == 7:
#         print("My reply is no")

#     else:
#         answers == 8
#         print("My sources say no")
#         if answers == 9:
#             break




# import sys
# import random

# ans = True

# while ans:
#    question = input("ask the magic 8 ball a question: (press enter to quit) ")

#    answers = random.randint(1, 8)

#    if question == "":
#     sys.exit()

#    elif answers == 1:
#     print("outlook good")

#    elif answers == 2:
#     print("It is certain")

#    elif answers == 3:
#     print("You may rely on it")

#    elif answers == 4:
#     print("Ask again later")

#    elif answers == 5:
#     print("Concentrate and ask again")

#    elif answers == 6:
#     print("Reply hazy, try again")

#    elif answers == 7:
#     print("My reply is no")

#    elif answers == 8:
#     print("My sources say no")







# break

# number = 7
# while True:
#     print("I love candy " + str(number))
#     number += 1
#     if number == 10:
#         break




# # Continue

# '''
# in a team of members 20, some numbers are taken 
# and want to display the numbers that are not taken
# so others don't pick the picked numbers
# '''

# # taken numbers
# numTaken = [3, 5, 7, 11, 13]

# print("Available numbers")

# # loop
# for i in range(1, 21):
#     if i in numTaken:
#         continue
#     print(i)




# # Lists

# #Joining lists

# list_a = ["a", "b", "c", "d"]
# list_b = [1, 2, 3, 4, 5, 6]

# # Joining list_b to list_a

# list_a.extend(list_b)

# print(list_a) 
# print(list_b)




# # Append

# list_a = ["a", "b", "c", "d"]

# print(list_a)

# list_a.append("e")

# print(list_a)





# list_a = [1, 2, 3, 4, 5]

# list_a.reverse()

# print(list_a)

# list_b = list_a.reverse()

# print(list_b)




# tuple_a = ("a", "b", "c", "d")

# tuple_b = (1, 2, 3, 4, 5,6)

# tuple_c = (1, "west", 34, "longitude")

# tuple_d = tuple(tuple_a)

# print(tuple_d)




# Dictionary 

# # Creating empty dictionaries
# my_dict = {}
# my_dict = dict()

# # Creating a dictionary with keys and values
# my_cat = {'name': 'Mr sniffles', 'age': 18, 'color': 'black'}

# cat_name = my_cat['name']
# cat_age = my_cat['age']
# cat_color = my_cat['color']
# print(cat_name)
# print(str(cat_name) + ' is ' + str(cat_age) + ' years of age' )
# print(str(cat_name) + ' is ' + str(cat_color) + ' in color' )




# birthdays = {"John": "August 1", "Marcus": "April 8"}
# birthdays["mary"] = "September 14" # Here we are ading a key "mary" and asigning it a value "september 14" to the dictionary
# print(birthdays)




# birthday = {"John": "August 1", "Marcus": "April 8", "Mary": "September 14"}

# print(birthday.keys())
# print(list(birthday.keys()))
# print(list(birthday.keys())[0])






