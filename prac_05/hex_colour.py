HEX_CODE = {"aquamarine1": "#7fffd4", "aureolin": "#fdee00", "baker-miller pink": "#ff91af",
            "bleu de france": "#318ce7", "blueViolet": "#8a2be2", "cadmium yellow": "#fff600",
            "caribbean green": "#00cc99", "celeste": "#b2ffff", "coquelicot": "#ff3800",
            "cream": "#fffdd0"}
user_choice = input("What colour would you like to search for: ")
while user_choice != "":
    while user_choice not in HEX_CODE:
        print("Invalid colour")
        user_choice = input("What colour would you like to search for: ")
    print(f"The colour {user_choice} has the code {HEX_CODE[user_choice]}.")
    user_input = input("What colour would you like to search for: ")
else:
    print("Bye Bye")