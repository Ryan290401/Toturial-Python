import random
LINE = 6
MIN = 1
MAX = 45

def main():
    print('How many quick picks? ')
    lines = int(input(">>> "))
    while lines <= 0:
        print("Invalid number")
        print('How many quick picks? ')
        lines = int(input(">>> "))

    for i in range(0, lines):
        quick_picks = []
        for j in range(0, LINE):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))

main()