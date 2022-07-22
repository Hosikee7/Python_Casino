from audioop import add
from os import times_result
import random
import time
from timeit import repeat

money = 1000

a = input("숫자를 입력하시오. (1부터 15까지의 수) : ")

lst1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
lst2 = ['Wow!', 'Awsome!', 'Great']
lst3 = ['Oops', 'Try one more!', 'Oh, no']

ai_answer = random.choice(lst1)

print("AI : " + ai_answer + ", You : " + a)

if a == ai_answer:
    a = random.choice(lst2)
    money+=10
    print(a, "\nYour Pocket :", money)
else:
    b = random.choice(lst3)
    money-=30
    print(b, "\nYour Pocket :", money)

if money == 0:
    print("You can't play casino! You must wait 1 hour!")
    if times_result == 1:
        add(money + 100)

repeat = bool(input('Go on? [Close : Q]'))