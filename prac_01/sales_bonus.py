sales = float(input("Enter sales: $ "))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.1
    print(f'your bonus : $ {bonus}')
    sales = float(input("Enter sales: $ "))
print("Invalid Input")