def main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars 
(Q)uit"""
    print(MENU)
    choice = input("Choise: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = option_g()
        elif choice == 'P':
            option_p(score)
        elif choice == 'S':
            print('*'*score)
        else:
            print('Invalid choice')
        print(MENU)
        choice = input("Choise: ").upper()
    print('Farewell')


def option_p(score):
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    elif score <= 100:
        print("Excellent")


def option_g():
    score = int(input('Score: '))
    while score < 0 or score > 100:
        print('Score must be 0-100 inclusive')
        score = int(input('Score: '))
    return score


main()