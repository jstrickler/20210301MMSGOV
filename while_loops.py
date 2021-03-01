
while True:
    user_name = input("Enter your name: ")
    if user_name == 'q':
        break
    if user_name == '':
        print("Please enter a name")
        continue
    print("Hello,", user_name)

