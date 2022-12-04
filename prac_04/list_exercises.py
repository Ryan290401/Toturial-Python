num_list = []
for i in range(5):
    number = int(input('Number: '))
    num_list.append(number)

print(f'Your first number is {num_list[0]}')
print(f'Your last number is {num_list[4]}')
print(f'Your smallest number is {min(num_list)}')
print(f'Your largest number is {max(num_list)}')
print(f'The average of the numbers is {sum(num_list) / len(num_list)}')

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input('Username: ')
if user_name in usernames:
    print(f'Access Granted')
else:
    print(f'Access Denied')