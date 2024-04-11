#Daniel Hoffman

def encode(password):
    encodedpassword = ""
    for char in password:
        newdigit = (int(char) + 3) % 10
        encodedpassword += str(new_digit)
    return encoded_password

#Lucas John
def decoded_password(encodedpassword):
    x=str(encodedpassword)
    decoded_password=''
    for i in x:
        y=int(i)
        y-=3
        p=str(y)
        decoded_password+=p
    return decoded_password

option = 0
while True:
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
    option = int(input("Please enter an option: "))

    if option == 1:
        password = int(input("Please enter your password to encode: "))
        if True:
            print("Your password has been encoded and stored!\n")

    if option == 2:
        print(f"The encoded password is {encodedpassword}, and the original password is {password}.")

    elif option == 3:
        break
