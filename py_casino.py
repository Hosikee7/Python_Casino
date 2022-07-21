import random

a = input("숫자를 입력하시오. (1부터 30까지의 수) : ")

lst1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
lst2 = ['Wow!', 'Awsome!', 'Great']
lst3 = ['Oops', 'Try one more!', 'Oh, no']

ai_answer = random.choice(lst1)

print("AI : " + ai_answer + ", You : " + a)

if a == ai_answer:
    a = random.choice(lst2)
    print(a)
else:
    b = random.choice(lst3)
    print(b)