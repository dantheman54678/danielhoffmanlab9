#Daniel Hoffman

def encode(password):
    encodedpassword = ""
    for char in password:
        newdigit = (int(char) + 3) % 10
        encodedpassword += str(new_digit)
    return encoded_password