try:

    def create_input():
        name = input("What is your name:    ").strip().lower()
        if name == "quincy":
            print("welcome user \n" + "welcome to cyberweb")
        else:
            print("invalid user")


except ValueError:
    print("oops something went wrong")

create_input()
