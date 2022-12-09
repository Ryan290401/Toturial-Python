e_mail_list = {}

e_mail = input('Email: ')
while e_mail != '':
    pre_mail = e_mail.split('@')[0]
    split_dot = pre_mail.split('.')
    name = ' '.join(split_dot).title()
    check = input(f'Is your name {name}? (Y/N)')
    if check.lower() =='y'or check == '':
        e_mail_list[e_mail] = name
    else:
        name = input('Name: ').title()
        e_mail_list[e_mail] = name
    e_mail = input("Email: ")
for e_mail, name in e_mail_list.items():
    print(f'{name} ({e_mail})')
