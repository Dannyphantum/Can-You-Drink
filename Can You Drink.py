import re


def age():
    print("How old are you?")
    user_age = int(input())
    print("AHH!! So you are " + str(user_age) + " years old?!?")
    if user_age >= 21:
        print("Oh shit! *passes you a bottle*")
    else:
        years = 21 - int(user_age)
        print("Oh man...you need to wait " + str(years) + " years until you can get lit.")

print("Do you know how old you need to be to get lit???")
answer = input()

if answer == 'Yes':
    print("Oh! Well, that's great!")
else:
    print("The age of Littness is 21, dummy!")

age()




