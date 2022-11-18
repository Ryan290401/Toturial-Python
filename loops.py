for a in range(0, 101, 10):
    print(a, end=' ')
print()

for b in range(20, 0, -1):
    print(b, end=' ')
print()

star = int(input('Number of stars: '))
for c in range(0,star):
    print('*',end='')
print()

row = int(input('Number of rows: '))
for d in range(row+1):
    print('*'*d)
print()