TOTAL_PRICE = 0
item = int(input('Number of items: '))
while item < 0:
    print('Invalid number of items!')
    item = int(input('Number of items: '))
for i in range(item):
    price = float(input('Price of item: '))
    TOTAL_PRICE+=price
if TOTAL_PRICE > 100:
    TOTAL_PRICE = TOTAL_PRICE * 0.9
print(f'Total price for {item} items is ${TOTAL_PRICE:.2f}')