def main():
    minimum_password_length = 6
    maximum_password_length = 20
    def get_password(password):
        while len(password) <= minimum_password_length or len(password) >= maximum_password_length:
            print("Invalid Password length (retry)")
            password = input("Password: ")
        else:
            print("*" * len(password))

    password = get_password(str(input("Enter Password: ")))
main()