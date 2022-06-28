print("Welcome to the Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

name1 = name1.lower()
name2 = name2.lower()

score1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
score2 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e') + name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

total = str(score1) + str(score2)

if total <'10' or total >'90':
    print(f"Your score is {total}, you go together like coke and mentos!")
elif total <'40' or total >'50':
    print(f"Your score is {total}, you are alright together!")
else:
    print(f"Your score is {total}")
